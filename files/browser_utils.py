"""
browser_utils.py
=================
Wspólne narzędzie dla wszystkich scraperów: otwiera stronę w PRAWDZIWEJ
przeglądarce Chromium (sterowanej programistycznie, bez widocznego okienka -
tzw. "headless"), czeka aż strona się załaduje, i zwraca gotowy HTML.

Dlaczego to jest trudniejsze do wykrycia niż zwykłe "requests"?
- To NAPRAWDĘ jest Chromium - wykonuje JavaScript, ma prawdziwy silnik
  renderowania, prawdziwe "odciski palca" przeglądarki (fingerprint).
- Dodatkowo maskujemy kilka sygnałów, po których strony rozpoznają
  automatyzację (np. navigator.webdriver = true).

To NIE jest w 100% niewykrywalne - najlepsze systemy antybotowe (jak
DataDome na Vinted) czasem i tak to rozpoznają, ale mamy dużo większe
szanse niż z samym "requests".
"""

from playwright.sync_api import sync_playwright
from config import USER_AGENT

# Skrypt wstrzykiwany do każdej strony PRZED jej załadowaniem - maskuje
# najbardziej oczywiste ślady automatyzacji.
STEALTH_SCRIPT = """
Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
Object.defineProperty(navigator, 'languages', { get: () => ['pl-PL', 'pl', 'en-US', 'en'] });
Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3, 4, 5] });
window.chrome = { runtime: {} };
"""

# Ustaw na False, żeby ZOBACZYĆ jak przeglądarka faktycznie działa (przydatne
# do debugowania - widzisz na żywo co bot "klika" i widzi).
HEADLESS = True


# Typowe przyciski banerów "Akceptuję cookies" - jeśli się pojawią, klikamy
# je automatycznie, bo inaczej mogą zasłaniać treść strony.
COOKIE_ACCEPT_SELECTORS = [
    "button#onetrust-accept-btn-handler",
    "button[data-testid='cookie-accept']",
    "button:has-text('Akceptuję')",
    "button:has-text('Zaakceptuj')",
    "button:has-text('Accept')",
    "button:has-text('Zgadzam się')",
]


def _dismiss_cookie_banner(page):
    for selector in COOKIE_ACCEPT_SELECTORS:
        try:
            button = page.locator(selector).first
            if button.is_visible(timeout=1500):
                button.click(timeout=1500)
                page.wait_for_timeout(500)
                return
        except Exception:
            continue


def get_rendered_html(url: str, wait_selector: str = None, scroll: bool = False, wait_ms: int = 2000) -> str:
    """
    Otwiera url w przeglądarce i zwraca wyrenderowany HTML (po wykonaniu JS).

    wait_selector: opcjonalny selektor CSS, na który czekamy zanim uznamy,
                   że strona się załadowała (np. kontener z ogłoszeniami).
    scroll: jeśli True, przewija stronę w dół, żeby doładować treści
            ładowane "przy przewijaniu" (typowe dla Vinted).
    wait_ms: dodatkowy czas oczekiwania (w milisekundach) po załadowaniu,
             na wszelki wypadek gdyby coś jeszcze dogrywało się w tle.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=HEADLESS,
            args=[
                "--disable-blink-features=AutomationControlled",
            ],
        )
        context = browser.new_context(
            user_agent=USER_AGENT,
            viewport={"width": 1366, "height": 900},
            locale="pl-PL",
        )
        context.add_init_script(STEALTH_SCRIPT)
        page = context.new_page()

        try:
            page.goto(url, timeout=30000, wait_until="domcontentloaded")
            _dismiss_cookie_banner(page)

            if wait_selector:
                try:
                    page.wait_for_selector(wait_selector, timeout=10000)
                except Exception:
                    # nie znaleziono selektora w czasie - i tak spróbujemy
                    # zwrócić to co jest, main.py obsłuży pustą listę wyników
                    pass

            if scroll:
                for _ in range(4):
                    page.mouse.wheel(0, 2000)
                    page.wait_for_timeout(800)

            page.wait_for_timeout(wait_ms)
            html = page.content()
        finally:
            browser.close()

        return html
