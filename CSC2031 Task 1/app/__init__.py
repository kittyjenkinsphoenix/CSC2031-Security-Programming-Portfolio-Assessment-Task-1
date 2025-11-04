from flask import Flask
from config import Config
import logging
import time
import os

# Function
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Use UTC Timestamps In Log Records
    logging.Formatter.converter = time.gmtime

    logFormatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    app.logger.setLevel(logging.INFO)

    # Try To Write Logs Into The Instance Folder
    try:
        os.makedirs(app.instance_path, exist_ok=True)
        logPath = os.path.join(app.instance_path, 'registration.log')
        fileHandler = logging.FileHandler(logPath)
        fileHandler.setLevel(logging.INFO)
        fileHandler.setFormatter(logFormatter)
        app.logger.addHandler(fileHandler)
    except Exception:
        # Configure The Root Logger So Logs Still Appear
        logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s [%(name)s] %(message)s')


    from .routes import main
    app.register_blueprint(main)

    return app
