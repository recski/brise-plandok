import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(format="%(asctime)s : %(module)s (%(lineno)s) - %(levelname)s - %(message)s")
