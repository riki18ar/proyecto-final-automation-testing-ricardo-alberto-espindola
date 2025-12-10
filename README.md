Propósito del proyecto

Este proyecto es un Framework de Automatización de Pruebas completo desarrollado en Python. 
1. Combina Selenium WebDriver (UI)  
2. Requests (API). 
3. Utiliza el patrón Page Object Model (POM) para código mantenible. 
4. Demuestra técnicas sólidas de testing y genera reportes visuales de resultados.

Tecnologías utilizadas: 
1. Python como lenguaje de programación principal.
2. Pytest como framework de pruebas unitarias sencillas así como también para pruebas funcionales más complejas para la ejecución y generación de informes de casos de prueba.
3. Selenium WebDriver para automatización de la interacción del browser.
4. webdriver-manager que gestiona automáticamente la descarga y uso del chromedriver compatible. 
5. Git y GitHub para control de versiones
6. Biblioteca request.

Instrucciones de instalación de dependencias
1.  Como prerrequisito tener instalado python3 en tu sistema operativo y navegador Google Chrome.
2.  Clonar el repositorio con el siguiente comando : git clone https://github.com/riki18ar/proyecto-final-automation-testing-ricardo-alberto-espindola.git
3.  Instalar las dependencias con las librerías necesarias (Selenium, Pytest, webdriver-manager, request, faker) con el siguiente comando : pip install selenium pytest webdriver-manager

Comando para ejecutar las pruebas 
Una vez instaladas las dependencias, de las pruebas podrán ejecutarse con el siguiente comando  para pruebas de navegacion en saucedemo: 
python3 -m pytest ./test -v --html=reports/reporte_final.html --self-contained-html
Los resultados y evidencia por cada prueba que pase, genera una captura de pantalla y un reporte html.  
Y para las pruebas de API, ejecutar el siguiente comando.
python3 -m pytest ./apis --tb=no -v  
