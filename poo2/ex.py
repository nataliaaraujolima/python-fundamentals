from dataclasses import dataclass
from typing import List, Optional
import requests
from http import HTTPStatus


@dataclass
class Anime:
    user_id: int
    id: int
    title: str
    body: str


class AnimeApi:
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    @staticmethod
    def get_animes() -> List[Anime]:
        url = f"{AnimeApi.BASE_URL}/posts"

        try:
            response = requests.get(url)
            if response.status_code == HTTPStatus.OK:
                data = response.json()
                return [Anime(**anime_data) for anime_data in data]
            else:
                return []
        except requests.RequestException as e:
            print(f"Erro ao buscar animes: {e}")
            return []

    @staticmethod
    def get_anime_by_id(anime_id: int) -> Optional[Anime]:
        url = f"{AnimeApi.BASE_URL}/posts/{anime_id}"

        try:
            response = requests.get(url)
            if response.status_code == HTTPStatus.OK:
                anime_data = response.json()
                return Anime(**anime_data)
            else:
                return None
        except requests.RequestException as e:
            print(f"Erro ao buscar anime por ID {anime_id}: {e}")
            return None


# Exemplo de uso da classe AnimeApi
anime_by_id = AnimeApi.get_anime_by_id(2)
if anime_by_id:
    print("Anime por ID:", anime_by_id)
else:
    print("Anime não encontrado ou erro na requisição.")

all_animes = AnimeApi.get_animes()
print("Todos os animes:")
for anime in all_animes:
    print(anime)
