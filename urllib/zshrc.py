import os
import subprocess


def get_bitbucket_credentials():
    username = os.getenv('BITBUCKET_USERNAME')
    app_password = os.getenv('BITBUCKET_APP_PASSWORD')
    if not username or not app_password:
        raise Exception(
            "Credenciais do Bitbucket não encontradas. Por favor, configure as variáveis de ambiente 'BITBUCKET_USERNAME' e 'BITBUCKET_APP_PASSWORD'.")
    return username, app_password


def clone_repo(repo_url, target_dir):
    username, app_password = get_bitbucket_credentials()
    auth_repo_url = repo_url.replace(
        "https://", f"https://{username}:{app_password}@")
    subprocess.run(['git', 'clone', auth_repo_url, target_dir], check=True)


if __name__ == '__main__':
    # Exemplo de uso:
    REPO_URL = "https://bitbucket.org/cli-python-typer/cli-python-typer.git"

    # Caminho para a pasta Downloads no macOS
    home_dir = os.path.expanduser('~')
    target_dir = os.path.join(home_dir, 'Downloads', 'seu-repositorio')

    try:
        clone_repo(REPO_URL, target_dir)
        print(f"Repositório clonado com sucesso em {target_dir}!")
    except Exception as e:
        print(f"Erro ao clonar o repositório: {e}")
