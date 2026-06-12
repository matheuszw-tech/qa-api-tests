import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

class TestPosts:

    def test_listar_posts_retorna_200(self):
        response = requests.get(f"{BASE_URL}/posts")
        assert response.status_code == 200

    def test_listar_posts_retorna_lista(self):
        response = requests.get(f"{BASE_URL}/posts")
        data = response.json()
        assert isinstance(data, list)
        assert len(data) > 0

    def test_buscar_post_por_id(self):
        response = requests.get(f"{BASE_URL}/posts/1")
        data = response.json()
        assert response.status_code == 200
        assert data["id"] == 1
        assert "title" in data
        assert "body" in data

    def test_criar_post(self):
        payload = {
            "title": "Meu post de teste",
            "body": "Conteúdo do post",
            "userId": 1
        }
        response = requests.post(f"{BASE_URL}/posts", json=payload)
        data = response.json()
        assert response.status_code == 201
        assert data["title"] == payload["title"]

    def test_post_inexistente_retorna_404(self):
        response = requests.get(f"{BASE_URL}/posts/99999")
        assert response.status_code == 404