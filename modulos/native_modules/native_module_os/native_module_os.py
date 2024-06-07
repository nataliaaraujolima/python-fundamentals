import os
# Obter o caminho do diretório atual:


def get_current_directory():
    current_directory = os.getcwd()
    return current_directory


def get_os_inf():
    os_info = os.uname()
    return os_info
