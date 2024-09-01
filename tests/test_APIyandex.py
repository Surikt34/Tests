import unittest
import requests

TOKEN = 'xxx'
BASE_URL = 'https://cloud-api.yandex.net/v1/disk/resources'

headers = {
    'Authorization': f'OAuth {TOKEN}'
}

class TestYandexDiskAPI(unittest.TestCase):

    def test_create_folder_success(self):
        """Проверяем успешное создание папки."""
        folder_path = '/test_folder'
        params = {'path': folder_path}

        # Создание папки
        response = requests.put(BASE_URL, headers=headers, params=params)

        # Проверяем, что код ответа 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Проверяем, что папка действительно создана
        response = requests.get(BASE_URL, headers=headers, params=params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['name'], 'test_folder')

    def test_create_existing_folder(self):
        """Проверяем создание уже существующей папки."""
        folder_path = '/test_folder'
        params = {'path': folder_path}

        # Пытаемся создать ту же папку второй раз
        response = requests.put(BASE_URL, headers=headers, params=params)

        # Проверяем, что код ответа 409, так как папка уже существует
        self.assertEqual(response.status_code, 409)

    def test_create_folder_with_invalid_name(self):
        """Проверяем создание папки с некорректным именем."""
        folder_path = '/invalid/folder/name'  # '/' в имени не допустим
        params = {'path': folder_path}

        # Пытаемся создать папку с некорректным именем
        response = requests.put(BASE_URL, headers=headers, params=params)

        # Проверяем, что код ответа 400 (Bad Request), так как имя некорректное
        self.assertEqual(response.status_code, 400)

    def test_create_folder_unauthorized(self):
        """Проверяем создание папки без авторизации (неверный токен)."""
        folder_path = '/unauthorized_folder'
        params = {'path': folder_path}

        # Используем неверный токен для проверки
        headers_invalid = {'Authorization': 'OAuth неверный_токен'}
        response = requests.put(BASE_URL, headers=headers_invalid, params=params)

        # Проверяем, что код ответа 401
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()
