import requests


def bucar_usuario(usuario):
    """
    Busca o avatar do usuário no GitHub
    :param usuario: str nome com o nome do usuario no github
    :return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']

if __name__ == '__main__':
    print(bucar_usuario('leonardolginfo'))

