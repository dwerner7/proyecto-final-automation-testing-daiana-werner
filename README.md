# Proyecto de Pruebas Automatizadas con Pytest y Selenium WebDriver

## Descripción
Este proyecto tiene como objetivo implementar pruebas automatizadas para una página web ("https://www.saucedemo.com/") utilizando **Pytest** y **Selenium + Selenium WebDriver**. Las pruebas automatizadas son esenciales para garantizar la calidad y el funcionamiento adecuado de la aplicación web, permitiendo detectar errores y problemas de rendimiento de manera temprana en el ciclo de desarrollo.


## Propósito
El propósito de este proyecto es:
- **Automatizar pruebas funcionales**: Verificar que las funcionalidades de la página web se comporten como se espera.
- **Aumentar la eficiencia**: Reducir el tiempo y esfuerzo requerido para realizar pruebas manuales.
- **Facilitar la integración continua**: Permitir la ejecución de pruebas de manera automática en cada cambio de código.
- **Mejorar la calidad del software**: Identificar y corregir errores antes de que lleguen a producción.


## Tecnologías Utilizadas
- **Python**: Lenguaje de programación utilizado para escribir las pruebas.
- **Pytest**: Framework de testing que permite estructurar y ejecutar las pruebas de manera sencilla.
- **Pytest-HTML**: Generación de reportes detallados en formato HTML.
- **Selenium + Selenium WebDriver**: Herramienta que permite controlar un navegador web de forma programática, facilitando la interacción con la interfaz de usuario.
- **WebDriver Manager**: Gestión automática de los drivers del navegador (ej. ChromeDriver).
- **Git & GitHub**: Sistema de control de versiones y hosting del código fuente.


## Instalación de dependencias
En consola:
- **Pytest**: pip install pytest
- **Selenium**: pip install selenium
- **WebDriver**: pip install webdriver-manager
- **Reporte HTML**: pip install pytest-html


## Ejecución de pruebas
Para ejecutar las pruebas se debe abrir la consola, ubicarse sobre el proyecto a testear y con el comando:
    py -m pytest run_tests.py -v

Ejecutando este archivo se correrán todos los tests del proyecto y se creará un reporte HTML.


En caso de querer ejecutar los tests individualmente se debe usar el siguiente comando (ejemplo con test_login):
    py -m pytest test/test_login.py 
- Si se quiere obtener más detalles de la ejecución agregar al final del comando: -v
- Si se quiere un reporte HTML agregar al final del comando: --html=reporte.html
