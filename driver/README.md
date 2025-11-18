# driver/ folder

English:
- The .exe file is empty, this file is only for documentation purposes it means thhat contains the driver for windows, what means in simple words is that the `drivers` are the binaries that allow the browser to be controlled by the selenium webdriver.
- This folder is optional. With Selenium 4.6+ the recommended approach is to let Selenium Manager download and resolve the appropriate browser driver automatically.
- So you usually do NOT need to place any driver binaries here.
- For that reason the `chromedriver.exe` file is empty.

Spanish:
- El archivo .exe está vacío, este archivo es solo para fines de documentación, lo que significa que contiene el driver para windows, lo que significa en palabras simples que los `drivers` son los binarios que permiten controlar el navegador por el selenium webdriver.
- Esta carpeta es opcional. Con Selenium 4.6+ se recomienda utilizar Selenium Manager para descargar y resolver automáticamente el driver del navegador adecuado.
- Por lo que usualmente NO necesitas colocar binarios aquí.
- Por eso el archivo `chromedriver.exe` está vacío.

---

## When would I place a driver here?
- English: Only if your environment does not allow Selenium Manager to download drivers
  (e.g., offline, restricted network), or you want to pin a specific driver version.
- Spanish: Solo si tu entorno no permite que Selenium Manager descargue drivers
  (p. ej., sin internet, red restringida), o deseas fijar una versión específica.

## Platform notes
- English:
  - On Linux/macOS do NOT use `.exe` files (Windows only). Use a Linux/macOS compatible binary.
  - Ensure the binary has execution permissions (e.g., `chmod +x chromedriver`).
- Spanish:
  - En Linux/macOS NO uses archivos `.exe` (solo Windows). Usa un binario compatible.
  - Asegúrate de que el binario tenga permisos de ejecución (p. ej., `chmod +x chromedriver`).

## How the framework finds a local driver
- English:
  - Set an environment variable to point to your local driver:
    - Chrome: `CHROME_DRIVER_PATH=/absolute/path/to/chromedriver`
    - Firefox: `FIREFOX_DRIVER_PATH=/absolute/path/to/geckodriver`
  - The `utils/browser_manager.py` will use that path; otherwise it falls back to Selenium Manager.
- Spanish:
  - Define una variable de entorno para apuntar a tu driver local:
    - Chrome: `CHROME_DRIVER_PATH=/ruta/absoluta/a/chromedriver`
    - Firefox: `FIREFOX_DRIVER_PATH=/ruta/absoluta/a/geckodriver`
  - `utils/browser_manager.py` usará esa ruta; de lo contrario utilizará Selenium Manager.

## Recommended practice
- English:
  - Prefer Selenium Manager. Keep the repo lightweight and OS-agnostic.
  - If you must commit a driver for teaching/demo, document the platform and version clearly,
    and consider adding OS-specific subfolders (e.g., `driver/linux/`, `driver/windows/`).
- Spanish:
  - Prefiere Selenium Manager. Mantén el repositorio liviano y agnóstico del sistema operativo.
  - Si debes incluir un driver por fines educativos/demostrativos, documenta claramente la plataforma y versión,
    y considera usar subcarpetas por sistema operativo (p. ej., `driver/linux/`, `driver/windows/`).

## Security/Safety note
- English: Avoid committing large binaries and keep drivers out of version control when possible.
- Spanish: Evita commitear binarios grandes y mantén los drivers fuera del control de versiones cuando sea posible.
