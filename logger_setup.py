import logging
import os

# pipeline.log file ka path setup
LOG_FILE = os.path.join(os.path.dirname(__file__), "pipeline.log")

# Logger configuration
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger("ML_Pipeline")