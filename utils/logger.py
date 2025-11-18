 # English: Centralized logging with formatting, timestamp, levels (info, error, debug), file output, and log rotation
# Spanish: Logging centralizado con formato, timestamp, niveles (info, error, debug), salida a archivo y rotación de logs

import logging
import os
from datetime import datetime
from pathlib import Path

# English: Create logs directory if it doesn't exist
# Spanish: Crear directorio de logs si no existe
LOGS_DIR = Path(__file__).parent.parent / "logs"
LOGS_DIR.mkdir(exist_ok=True)

# English: Generate log filename with timestamp
# Spanish: Generar nombre de archivo de log con timestamp
log_filename = f"test_execution_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
log_filepath = LOGS_DIR / log_filename

# English: Configure log format
# Spanish: Configurar formato de log
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s'
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# English: Get log level from environment or default to INFO
# Spanish: Obtener nivel de log desde el entorno o usar INFO por defecto
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()

def setup_logger(name: str = __name__, level: str = LOG_LEVEL) -> logging.Logger:
    """
    English: Setup and return a configured logger instance
    Spanish: Configurar y retornar una instancia de logger configurada
    
    Args:
        name: Logger name (usually __name__ from calling module)
        level: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    
    # English: Avoid adding handlers multiple times
    # Spanish: Evitar agregar handlers múltiples veces
    if logger.handlers:
        return logger
    
    logger.setLevel(getattr(logging, level))
    
    # English: Console Handler - outputs to terminal
    # Spanish: Console Handler - salida a la terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter(LOG_FORMAT, DATE_FORMAT)
    console_handler.setFormatter(console_formatter)
    
    # English: File Handler - outputs to log file
    # Spanish: File Handler - salida a archivo de log
    file_handler = logging.FileHandler(log_filepath, mode='a', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)  # Capture all levels in file
    file_formatter = logging.Formatter(LOG_FORMAT, DATE_FORMAT)
    file_handler.setFormatter(file_formatter)
    
    # English: Add handlers to logger
    # Spanish: Agregar handlers al logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger

# English: Create default logger instance for direct import
# Spanish: Crear instancia de logger por defecto para importación directa
logger = setup_logger()

# English: Log the initialization
# Spanish: Registrar la inicialización
logger.info(f"Logger initialized - Log file: {log_filepath}")
