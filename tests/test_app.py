import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) #code enables pytest to import the app.py

from app import app
client = app.test_client()
def test():
    response = client.get("/")
    assert response.status_code == 200 #request has been succeeded
