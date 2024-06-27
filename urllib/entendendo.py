import os
import requests


def get_bibbucket_credentials_zshrc():

    user_name_bitbucket = os.getenv('BITBUCKET_USERNAME')
    user_password_bitbucket = os.getenv('BITBUCKET_APP_PASSWORD')
    bitbucket_workspace = os.getenv('BITBUCKET_WORKSPACE')

    return user_name_bitbucket, user_password_bitbucket, bitbucket_workspace


def get_list_repos(repo_slug):
    credentials_all = get_bibbucket_credentials_zshrc()

    user_name_bitbucket_formated = credentials_all[0]
    user_password_bitbucket_formated = credentials_all[1]
    bitbucket_workspace_formated = credentials_all[2]

    url = f"https://api.bitbucket.org/2.0/repositories/{bitbucket_workspace_formated}/{repo_slug}"
    get_repo_api = requests.get(url, auth=(user_name_bitbucket_formated,
                                           user_password_bitbucket_formated,))

    return get_repo_api


if __name__ == '__main__':
    get_bibbucket_credentials_zshrc()
    repo_slug = input("Digite o nome do repositório: ")
    url = get_list_repos(repo_slug)
    print(url.content)
