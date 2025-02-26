import logging
import os
from datetime import datetime

# Define log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Ensure the logs directory exists
logs_dir = os.path.join(os.getcwd(), "logs")  # Create the logs folder
os.makedirs(logs_dir, exist_ok=True)  # Ensure the directory exists

# Define the full path for the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,  
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


if __name__== "__main__":
    logging.info("Logging has started")
