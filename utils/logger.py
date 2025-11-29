import logging
import pathlib

# Creamos una carpeta llamada 'logs'
audit_dir = pathlib.Path('logs')

# Se verifica si ya existe la carpeta, sino es creada
audit_dir.mkdir(exist_ok=True)

# Creamos un archivo dentro de 'logs'
log_file = audit_dir/ 'suite.log'

# Definimos a este archivo como logger
logger = logging.getLogger("TalentoTech")
# Tipo de logger / tipo de mensaje a transmitir
logger.setLevel(logging.INFO)

# Si ya existe un archivo log con estas caracteristicas, no va a crear otro
if not logger.handlers:
    # Se agrega cada log a continuación del anterior
    file_handler = logging.FileHandler(log_file,mode="a",encoding="utf-8")

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Aplicamos el formato
    file_handler.setFormatter(formatter)

    # Aplicamos todo al logger
    logger.addHandler(file_handler)
