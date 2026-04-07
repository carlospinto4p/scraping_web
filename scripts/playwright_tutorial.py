"""
Playwright tutorial: explorar X.com con un navegador limpio.

Este script demuestra como usar Playwright para web scraping,
simulando un navegador sin cache, sin cookies y sin sesion previa.

Ejecutar con:
    uv run python scripts/playwright_tutorial.py
"""

from __future__ import annotations

from playwright.sync_api import (
    BrowserContext,
    Page,
    sync_playwright,
    Playwright,
)


# ================================================================
# Funciones auxiliares reutilizables
# ================================================================


def get_screenshot(page: Page, path: str) -> None:
    """Captura una screenshot de la pagina actual."""
    page.screenshot(path=path, full_page=False)
    print(f"  Captura guardada en {path}")


def get_links(page: Page, limit: int = 15) -> list[dict]:
    """Extrae todos los enlaces visibles de la pagina."""
    links: list[dict] = page.eval_on_selector_all(
        "a[href]",
        "elements => elements.map(e => ({"
        "  text: e.innerText.trim(),"
        "  href: e.href"
        "}))",
    )
    print(f"  Enlaces encontrados: {len(links)}")
    for link in links[:limit]:
        text = link.get("text", "")[:50]
        href = link.get("href", "")
        if text:
            print(f"    - {text}: {href}")
    return links


def get_buttons(page: Page, limit: int = 15) -> list[dict]:
    """Extrae todos los botones visibles de la pagina."""
    buttons: list[dict] = page.eval_on_selector_all(
        "button, [role='button']",
        "elements => elements.map(e => ({"
        "  text: e.innerText.trim(),"
        "  type: e.type || '',"
        "  ariaLabel: e.ariaLabel || ''"
        "}))",
    )
    print(f"  Botones encontrados: {len(buttons)}")
    for btn in buttons[:limit]:
        text = btn.get("text", "")[:50]
        label = btn.get("ariaLabel", "")
        display = text or label or "(sin texto)"
        print(f"    - {display}")
    return buttons


def get_headings(page: Page, limit: int = 10) -> list[str]:
    """Extrae los encabezados (h1-h4) de la pagina."""
    headings: list[str] = page.eval_on_selector_all(
        "h1, h2, h3, h4",
        "els => els.map(e => e.innerText.trim())",
    )
    if headings:
        print(f"  Encabezados encontrados: {len(headings)}")
        for h in headings[:limit]:
            if h:
                print(f"    - {h}")
    return headings


def get_cookies(context: BrowserContext, limit: int = 10) -> list:
    """Lista las cookies actuales del contexto."""
    cookies = context.cookies()
    print(f"  Cookies actuales: {len(cookies)}")
    for cookie in cookies[:limit]:
        print(f"    - {cookie['name']}: {cookie['value'][:30]}...")
    return cookies


def get_page_info(
    page: Page,
    context: BrowserContext,
    screenshot_path: str,
    label: str = "",
) -> None:
    """Recopila toda la informacion de la pagina actual."""
    header = (
        f"=== Informacion de la pagina{f' ({label})' if label else ''} ==="
    )
    print(f"\n{header}")

    print(f"  Titulo: {page.title()}")
    print(f"  URL: {page.url}")

    html = page.content()
    print(f"  Tamano del HTML: {len(html):,} caracteres")

    get_screenshot(page, screenshot_path)
    get_links(page)
    get_buttons(page)
    get_headings(page)
    get_cookies(context)

    print(f"{'=' * len(header)}\n")


# ================================================================
# Funcion principal de exploracion
# ================================================================


def explore_x(pw: Playwright) -> None:
    """Explora x.com con un navegador limpio."""
    # -----------------------------------------------------------
    # 1. Lanzar el navegador
    # -----------------------------------------------------------
    # `headless=False` abre una ventana visible para que puedas
    # ver lo que hace el script.
    # En produccion se usa `headless=True` (por defecto).
    browser = pw.chromium.launch(headless=False)

    # -----------------------------------------------------------
    # 2. Crear un contexto limpio
    # -----------------------------------------------------------
    # Cada contexto es un perfil aislado: sin cookies, sin
    # cache, sin historial. Es como abrir una ventana de
    # incognito.
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

    print("Navegando a x.com...")
    page.goto("https://x.com", wait_until="domcontentloaded")

    # Esperar a que la pagina cargue contenido visible.
    # Nota: usamos wait_for_timeout solo con fines didacticos.
    # En produccion se usarian senales como selectores visibles
    # o eventos de red.
    page.wait_for_timeout(3_000)

    # -----------------------------------------------------------
    # 4. Primera recogida de informacion (antes de cookies)
    # -----------------------------------------------------------
    get_page_info(
        page,
        context,
        screenshot_path="scripts/x_com_01_antes_cookies.png",
        label="antes de aceptar cookies",
    )

    # -----------------------------------------------------------
    # 5. Aceptar cookies
    # -----------------------------------------------------------
    # X.com muestra un banner de cookies en la parte inferior.
    # Buscamos el boton por su texto visible.
    print("Buscando boton de aceptar cookies...")

    cookie_btn = page.get_by_role("button", name="Aceptar todas las cookies")

    if cookie_btn.is_visible():
        print("Boton encontrado. Haciendo clic...")
        cookie_btn.click()

        # Esperar a que la pagina se estabilice tras aceptar.
        # Usamos "load" en vez de "networkidle" porque sitios
        # como X.com mantienen conexiones abiertas (streaming,
        # websockets) y "networkidle" nunca se alcanza.
        # "load" espera al evento window.onload del navegador.
        page.wait_for_load_state("load")
        print("Pagina estabilizada tras aceptar cookies.\n")
    else:
        print("No se encontro el banner de cookies.\n")

    # -----------------------------------------------------------
    # 6. Segunda recogida de informacion (despues de cookies)
    # -----------------------------------------------------------
    get_page_info(
        page,
        context,
        screenshot_path="scripts/x_com_02_despues_cookies.png",
        label="despues de aceptar cookies",
    )

    # -----------------------------------------------------------
    # 7. Cerrar el navegador
    # -----------------------------------------------------------
    context.close()
    browser.close()
    print("Navegador cerrado. Fin del tutorial.")


def main() -> None:
    with sync_playwright() as pw:
        explore_x(pw)


if __name__ == "__main__":
    main()
