 # Logging centralizado con formato, timestamp y niveles (info, error, debug)


import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

logger.info("Logger initialized")

logger.debug("Logger initialized")
logger.info("Logger initialized")
logger.warning("Logger initialized")
logger.error("Logger initialized")
logger.critical("Logger initialized")

