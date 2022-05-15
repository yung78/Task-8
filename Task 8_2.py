import requests
import os


class YaUploader:
    host = 'https://cloud-api.yandex.net:443'

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        file_name = os.path.basename(file_path)
        url = f'{self.host}/v1/disk/resources/upload/'
        headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {token}'}
        params = {'path': f'/{file_name}', 'overwrite': True}
        upload_link = requests.get(url, params=params, headers=headers).json().get('href')
        response = requests.put(upload_link, data=open(file_path, 'rb'), headers=headers)
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    file_path = input(r"Введите путь к загружаемому файлу: ")
    token = ''
    uploader = YaUploader(token)
    uploader.upload(file_path)
