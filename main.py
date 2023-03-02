import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файл на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Content-Type': 'application/json',
            'Authorization':  f'OAuth {self.token}'
        }
        params = {'path': f'/netology/{file}', 'overwrite': 'true'}
        res1 = requests.get(url=url, headers=headers, params=params)
        res = res1.json()
        with open(file_path, 'rb') as f:
            requests.put(res['href'], files={'file': f})


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    file = '23. Windows Logo 2.jpg'
    path_to_file = fr'C:\Users\user\Pictures\Фоновые изображения рабочего стола\{file}'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
