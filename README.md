
## Scraping web

Contenido práctico de la clase de web scraping de abril de 2025 
realizada en el Máster en Ingeniería de Datos y Big Data de la Escuela 
Superior de Estudios de Empresa 
[Esesa IMF](https://www.esesa.eu/programa/master-ingenieria-de-datos-big-data).

## Instalación

### 1. Instalar dependencias

```bash
uv sync --all-extras
```

### 2. Instalar navegadores de Playwright

Playwright necesita descargar los navegadores (Chromium, Firefox y
WebKit) antes de poder usarse. Este paso es obligatorio y solo hay
que hacerlo una vez:

```bash
uv run playwright install
```

Si solo necesitas un navegador concreto, puedes instalarlo
individualmente:

```bash
uv run playwright install chromium
```

> **Nota**: La descarga puede tardar unos minutos ya que los
> navegadores ocupan varios cientos de MB en total.
