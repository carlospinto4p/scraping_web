"""
Playwright tutorial: explorar X.com con un navegador limpio.

Este script demuestra como usar Playwright para web scraping,
simulando un navegador sin cache, sin cookies y sin sesion previa.

Ejecutar con:
    uv run python scripts/playwright_tutorial.py
"""

from playwright.sync_api import sync_playwright


def main() -> None:
    with sync_playwright() as p:
        # -------------------------------------------------------
        # 1. Lanzar el navegador
        # -------------------------------------------------------
        # headless=False abre una ventana visible para que puedas
        # ver lo que hace el script. En produccion se usa
        # headless=True (por defecto).
        browser = p.chromium.launch(headless=False)

        # -------------------------------------------------------
        # 2. Crear un contexto limpio
        # -------------------------------------------------------
        # Cada contexto es un perfil aislado: sin cookies, sin
        # cache, sin historial. Es como abrir una ventana de
        # incognito.
        context = browser.new_context(
            # Simular un navegador real para evitar bloqueos
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/125.0.0.0 Safari/537.36"
            ),
            viewport={"width": 1280, "height": 800},
            locale="es-ES",
        )

        # -------------------------------------------------------
        # 3. Abrir una pagina nueva y navegar
        # -------------------------------------------------------
        page = context.new_page()

        print("Navegando a x.com...")
        page.goto("https://x.com", wait_until="domcontentloaded")

        # Esperar a que la pagina cargue contenido visible
        page.wait_for_timeout(3000)

        # -------------------------------------------------------
        # 4. Captura de pantalla
        # -------------------------------------------------------
        screenshot_path = "scripts/x_com_screenshot.png"
        page.screenshot(path=screenshot_path, full_page=False)
        print(f"Captura guardada en {screenshot_path}")

        # -------------------------------------------------------
        # 5. Extraer informacion basica de la pagina
        # -------------------------------------------------------
        title = page.title()
        print(f"Titulo de la pagina: {title}")

        url = page.url
        print(f"URL actual: {url}")

        # -------------------------------------------------------
        # 6. Explorar el DOM
        # -------------------------------------------------------
        # Extraer todos los enlaces visibles
        links = page.eval_on_selector_all(
            "a[href]",
            "elements => elements.map(e => ({"
            "  text: e.innerText.trim(),"
            "  href: e.href"
            "}))",
        )

        print(f"\nEnlaces encontrados: {len(links)}")
        for link in links[:15]:
            text = link.get("text", "")[:50]
            href = link.get("href", "")
            if text:
                print(f"  - {text}: {href}")

        # -------------------------------------------------------
        # 7. Extraer textos visibles
        # -------------------------------------------------------
        # Buscar elementos de texto prominentes
        headings = page.eval_on_selector_all(
            "h1, h2, h3, h4",
            "els => els.map(e => e.innerText.trim())",
        )

        if headings:
            print(f"\nEncabezados encontrados: {len(headings)}")
            for h in headings[:10]:
                if h:
                    print(f"  - {h}")

        # -------------------------------------------------------
        # 8. Verificar que no hay cookies previas
        # -------------------------------------------------------
        cookies = context.cookies()
        print(f"\nCookies actuales: {len(cookies)}")
        for cookie in cookies[:5]:
            print(f"  - {cookie['name']}: {cookie['value'][:30]}...")

        # -------------------------------------------------------
        # 9. Obtener el HTML de la pagina
        # -------------------------------------------------------
        html = page.content()
        print(f"\nTamano del HTML: {len(html):,} caracteres")

        # -------------------------------------------------------
        # 10. Cerrar el navegador
        # -------------------------------------------------------
        context.close()
        browser.close()
        print("\nNavegador cerrado. Fin del tutorial.")


if __name__ == "__main__":
    main()
