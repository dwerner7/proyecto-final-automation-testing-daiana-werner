# Proyecto de Pruebas Automatizadas con Pytest y Selenium WebDriver 

## Propósito 🌟
Este proyecto tiene como objetivo implementar pruebas automatizadas de UI para la página web "https://www.saucedemo.com/" implementando **Page Object Model**, manejo de datos externos, generación de reportes HTML, logging y capturas automática de pantalla, y pruebas automatizadas de **API** sobre "https://jsonplaceholder.typicode.com/" utilizando **Requests**. 


## Tecnologías Utilizadas 🌟
- Python 3.x
- Pytest
- Selenium WebDriver
- Git & GitHub
- Faker
- Logging
- CSV / JSON
- Request (API)


## Instalación de dependencias 🌟
```bash
pip install -r requirements.txt
```

## Reportes y logs 🌟
El proyecto genera tres tipos principales de resultados durante la ejecución de las pruebas: **reporte HTML**, **capturas de pantalla**, **archivo de log**

### Reporte HTML
Se genera un reporte HTML detallado con el nombre de ```reporte.hmtl``` en la **carpeta raiz** del proyecto

### Logs de ejecución
Se genera un log con información detallada de toda la ejecución de las pruebas en la siguiente ubicación: ```logs/suite.log```

### Capturas de pantalla
Se realizan capturas de pantalla por cada test que haya fallado. Estas se encuentran en la siguiente ubicación: ```reports/screens```

## Ejecución de pruebas 🌟
Para iniciar la ejecución de las pruebas se debe ejecutar la siguiente línea:
```bash
python -m run_test.py -v
```


## Interpretación de reportes generados 🌟
Al ejecutar `run_test.py`, se genera un archivo HTML en la carpeta raiz, se registra información en el archivo de logs y se realizan capturas de pantalla en caso de que la prueba falle.

- **Reporte HTML**: este contiene:
    - Lista completa de tests ejecutados.
    - Estado de cada prueba.
    - Duración de cada test.

- **Capturas de pantalla** para pruebas fallidas

- **Logging**: incluyen información sobre:
    - Mensajes de inicio y finalización de pruebas.
    - Errores encontrados durante la ejecución.
    - Interacciones con la interfaz de usuario y las APIs.


## Pruebas incluidas 🌟
- Login exitoso y fallido
- Login exitoso y fallido usando faker
- Comportamiento de la página de inventario
- Comportamiento de la página del carrito
- API (JSONPlaceholder): GET users, POST create user, DELETE user, validaciones de cádigos HTTP, validaciones de estructura JSON.


## Manejo de datos de prueba 🌟
- En la carpeta `datos` se incluyen archivos como:
    - `data_login.csv` -> datos de usuarios válidos o inválidos
    - `productos.json` -> datos de productos para validación


## Conclusión 🌟
Este proyecto ofrece una estructura organizada y escalable para automatizar pruebas de API utilizando Python y Pytest. Incluye un flujo simple de ejecución mediante `run_test.py` y generación automática de reporte HTML facilitando el análisis de las pruebas.

La arquitectura del proyecto está pensada para agregar nuevos casos de prueba y configuraciones sin modificar el núcleo del proyecto, manteniendo buenas prácticas y permitiendo su escalabilidad en el tiempo.