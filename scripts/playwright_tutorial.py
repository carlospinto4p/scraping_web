"""
Playwright tutorial: explorar X.com con un navegador limpio.

Este script demuestra cómo usar Playwright para web scraping,
simulando un navegador sin caché, sin cookies y sin sesión previa.

Ejecutar con:
    uv run python scripts/playwright_tutorial.py
"""

import logging

from playwright.sync_api import (
    BrowserContext,
    Page,
    Playwright,
    sync_playwright,
)

logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(message)s",
        datefmt="%H:%M:%S",
    )
    with sync_playwright() as pw:
        explore_x(pw)


# ================================================================
# Función principal de exploración
# ================================================================


def explore_x(pw: Playwright) -> None:
    """Explora `x.com` con un navegador limpio."""
    # -----------------------------------------------------------
    # 1. Lanzar el navegador
    # -----------------------------------------------------------
    # `headless=False` abre una ventana visible para que puedas
    # ver lo que hace el script.
    # En producción se usa `headless=True` (por defecto).
    browser = pw.chromium.launch(headless=False)

    # -----------------------------------------------------------
    # 2. Crear un contexto limpio
    # -----------------------------------------------------------
    # Cada contexto es un perfil aislado: sin cookies, sin
    # caché, sin historial. Es como abrir una ventana de incógnito.
    context = browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/125.0.0.0 Safari/537.36"
        ),
        viewport={"width": 1280, "height": 800},
        locale="es-ES",
    )

    # -----------------------------------------------------------
    # 3. Navegar a x.com
    # -----------------------------------------------------------
    page = context.new_page()

    logger.info("Navegando a x.com...")
    page.goto("https://x.com", wait_until="domcontentloaded")

    # Esperar a que la página cargue contenido visible.
    # Nota: usamos `wait_for_timeout` como demostración.
    # En producción se usarían señales como selectores visibles
    # o eventos de red. De la documentación de la función:
    # > Note that `page.waitForTimeout()` should only be used for debugging.
    # > Tests using the timer in production are going to be flaky.
    # > Use signals such as network events, selectors becoming visible
    # > and others instead.
    page.wait_for_timeout(3_000)

    # -----------------------------------------------------------
    # 4. Para extraer información de la página (antes de cookies)
    # -----------------------------------------------------------
    get_page_info(
        page,
        context,
        screenshot_path="x_com_01_antes_cookies.png",
        label="antes de aceptar cookies",
    )

    # -----------------------------------------------------------
    # 5. Aceptar cookies
    # -----------------------------------------------------------
    # `X.com` muestra un banner de cookies en la parte inferior.
    # Buscamos el botón por su texto.
    logger.info("Buscando botón de aceptar cookies...")

    cookie_btn = page.get_by_role("button", name="Aceptar todas las cookies")

    if cookie_btn.is_visible():
        logger.info("Botón encontrado. Haciendo clic...")
        cookie_btn.click()

        # Esperar a que la página cargue tras aceptar.
        # Usamos "load" en vez de "networkidle" porque sitios
        # como `x.com` mantienen conexiones abiertas (streaming,
        # websockets) y "networkidle" nunca se alcanza.
        # "load" espera al evento `window.onload` del navegador.
        page.wait_for_load_state("load")
        logger.info("Página estabilizada tras aceptar cookies.")
    else:
        logger.warning("No se encontró el banner de cookies.")

    # -----------------------------------------------------------
    # 6. Segunda recogida de información (después de cookies)
    # -----------------------------------------------------------
    get_page_info(
        page,
        context,
        screenshot_path="x_com_02_cookies_aceptadas.png",
        label="después de aceptar cookies",
    )

    # -----------------------------------------------------------
    # 7. Pulsar "Crear cuenta"
    # -----------------------------------------------------------
    logger.info("Buscando botón de crear cuenta...")

    # Usamos un locator con `get_by_role` y `exact=True` para
    # que coincida solo con "Crear cuenta" y no con textos
    # parciales como "Crear cuenta con Google".
    create_btn = page.get_by_role("link", name="Crear cuenta", exact=True)

    if create_btn.is_visible():
        logger.info("Botón encontrado. Haciendo clic...")
        create_btn.click()

        # Esperamos a que aparezca el diálogo de registro.
        # `wait_for_selector` bloquea hasta que el selector
        # sea visible en el DOM, con un timeout configurable.
        # Es más fiable que `wait_for_timeout` porque reacciona
        # al contenido real en vez de a un tiempo fijo.
        page.wait_for_selector("[aria-modal='true']", timeout=10_000)
        logger.info("Diálogo de registro visible.")
    else:
        logger.warning("No se encontró el botón de crear cuenta.")

    # -----------------------------------------------------------
    # 8. Pausa para que los estudiantes vean el diálogo
    # -----------------------------------------------------------
    logger.info("Esperando 5 segundos...")
    page.wait_for_timeout(5_000)

    # -----------------------------------------------------------
    # 9. Tercera recogida de información (diálogo de registro)
    # -----------------------------------------------------------
    get_page_info(
        page,
        context,
        screenshot_path="x_com_03_crear_cuenta.png",
        label="diálogo de crear cuenta",
    )

    # -----------------------------------------------------------
    # 10. Cerrar el navegador
    # -----------------------------------------------------------
    context.close()
    browser.close()
    logger.info("Navegador cerrado. Fin del tutorial.")


# ================================================================
# Funciones auxiliares reutilizables
# ================================================================


def get_screenshot(page: Page, path: str) -> None:
    """Guarda una captura de pantalla de la página actual."""
    page.screenshot(path=path, full_page=False)
    logger.info("  Captura guardada en %s", path)


def get_links(page: Page, limit: int = 15) -> list[dict]:
    """Extrae todos los enlaces visibles de la página."""
    links: list[dict] = page.eval_on_selector_all(
        "a[href]",
        "elements => elements.map(e => ({"
        "  text: e.innerText.trim(),"
        "  href: e.href"
        "}))",
    )
    logger.info("  Enlaces encontrados: %d", len(links))
    for link in links[:limit]:
        text = link.get("text", "")[:50]
        href = link.get("href", "")
        if text:
            logger.info("    - %s: %s", text, href)
    return links


def get_buttons(page: Page, limit: int = 15) -> list[dict]:
    """Extrae todos los botones visibles de la página."""
    buttons: list[dict] = page.eval_on_selector_all(
        "button, [role='button']",
        "elements => elements.map(e => ({"
        "  text: e.innerText.trim(),"
        "  type: e.type || '',"
        "  ariaLabel: e.ariaLabel || ''"
        "}))",
    )
    logger.info("  Botones encontrados: %d", len(buttons))
    for btn in buttons[:limit]:
        text = btn.get("text", "")[:50]
        label = btn.get("ariaLabel", "")
        display = text or label or "(sin texto)"
        logger.info("    - %s", display)
    return buttons


def get_headings(page: Page, limit: int = 10) -> list[str]:
    """Extrae los encabezados (h1-h4) de la página."""
    headings: list[str] = page.eval_on_selector_all(
        "h1, h2, h3, h4",
        "els => els.map(e => e.innerText.trim())",
    )
    if headings:
        logger.info("  Encabezados encontrados: %d", len(headings))
        for h in headings[:limit]:
            if h:
                logger.info("    - %s", h)
    return headings


def get_cookies(context: BrowserContext, limit: int = 10) -> list:
    """Lista las cookies actuales del contexto."""
    cookies = context.cookies()
    logger.info("  Cookies actuales: %d", len(cookies))
    for cookie in cookies[:limit]:
        logger.info(
            "    - %s: %s...",
            cookie["name"],
            cookie["value"][:30],
        )
    return cookies


def get_page_info(
    page: Page,
    context: BrowserContext,
    screenshot_path: str,
    label: str = "",
) -> None:
    """Recopila un resumen de la información de la página actual."""
    suffix = f" ({label})" if label else ""
    header = f"=== Información de la página{suffix} ==="
    logger.info("\n%s", header)

    logger.info("  Título: %s", page.title())
    logger.info("  URL: %s", page.url)

    html = page.content()
    logger.info(
        "  Tamaño del HTML: %s caracteres",
        f"{len(html):,}",
    )

    get_screenshot(page, screenshot_path)
    get_links(page)
    get_buttons(page)
    get_headings(page)
    get_cookies(context)

    logger.info("%s\n", "=" * len(header))


if __name__ == "__main__":
    main()
