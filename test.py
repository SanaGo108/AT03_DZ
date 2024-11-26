import unittest
from unittest.mock import patch
from main import get_random_cat_image

class TestGetRandomCatImage(unittest.TestCase):

    @patch("requests.get")
    def test_successful_request(self, mock_get):
        # Создаем mock-ответ
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"url": "https://example.com/cat.jpg"}]
        mock_get.return_value = mock_response

        # Проверяем успешный вызов
        result = get_random_cat_image()
        self.assertEqual(result, "https://example.com/cat.jpg")

    @patch("requests.get")
    def test_unsuccessful_request(self, mock_get):
        # Создаем mock-ответ с ошибкой
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Проверяем, что функция возвращает None при ошибке
        result = get_random_cat_image()
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
