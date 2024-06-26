from dataclasses import dataclass
from typing import List, Optional
import requests
from http import HTTPStatus


@dataclass
class Anime:  # tipagem
    user_id: int
    id: int
    title: str
    body: str


class animeApi:
    BASE_URL = 'https://jsonplaceholder.typicode.com'


@staticmethod
def get_animes() -> List[Anime]:
    url = f"{Anime.BASE_URL}/posts"

    try:
        response = requests.get(url)
        if response.status_code == HTTPStatus.OK:
            data = response.json()
            # cria uma lista onde cada elemento é um objeto Anime, criado a partir dos dados contidos em data.
            return [Anime(**anime_data) for anime_data in data]

        else:
            return []
    except requests.RequestException as e:
        print(f"Erro ao buscar animes: {e}")
        return []


def get_anime_by_id(anime_id: int) -> Optional[Anime]:
    url = f"{Anime.BASE_URL}/posts/{id}"

    try:
        response = requests.get(url)
        if response.status_code == HTTPStatus.OK:
            anime_data = response.json()
            return Anime(**anime_data)

        else:
            return {"error": "Anime não encontrado", "status_code": response.status_code}
    except requests.RequestException as e:
        return {"error": str(e)}


anime_by_id = Anime.get_anime_by_id(2)
print(anime_by_id)

all_anime = Anime.get_animes()
print("todos os animes")
for anime in all_anime:
    print(anime)
