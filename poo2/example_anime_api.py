import requests
from http import HTTPStatus


class AnimeApi:

    BASE_URL = 'https://jsonplaceholder.typicode.com'

    def __init__(self):
        pass

    def get_animes_api(self):
        """
        Buscar todos os animes
        """
        url = f"{self.BASE_URL}/posts"

        try:
            response = requests.get(url)
            if response.status_code == HTTPStatus.OK:
                return response.json()
            else:
                return {"error": "Erro ao buscar animes", "status_code": response.status_code}
        except requests.RequestException as e:
            return {"error": str(e)}

    def get_anime_by_id(self, id):
        """
        Buscar anime pelo id
        """
        url = f"{self.BASE_URL}/posts/{id}"

        try:
            response = requests.get(url)
            if response.status_code == HTTPStatus.OK:
                return response.json()
            else:
                return {"error": "Erro ao buscar anime", "status_code": response.status_code}
        except requests.RequestException as e:
            return {"error": str(e)}


anime_api = AnimeApi()
list_anime_by_id = anime_api.get_anime_by_id(1)
list_all_animes = anime_api.get_animes_api()

print(list_anime_by_id)
print(list_all_animes)
