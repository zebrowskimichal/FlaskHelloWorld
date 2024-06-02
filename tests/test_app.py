def test():
    response = client.get("/")
    assert response.status_code == 200 //request has been succeded
