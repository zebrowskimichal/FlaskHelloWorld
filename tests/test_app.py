from FlaskHelloWorld import app
client = app.test_client()
def test():
    response = client.get("/")
    assert response.status_code == 200 #request has been succeded
