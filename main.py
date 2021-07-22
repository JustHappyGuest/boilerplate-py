#!flask/bin/python
import os
from dotenv import load_dotenv

from app.core.app import create_app

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

PORT = os.environ.get("PORT")

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=PORT, debug=True)
