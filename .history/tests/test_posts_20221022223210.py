def test_get_every_post(authorized_client):
    response = authorized_client.get('/posts/')
    print(response.json())
    assert response.status_code == 200
