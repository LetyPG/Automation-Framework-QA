 # Logging centralizado con formato, timestamp y niveles (info, error, debug)


import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)