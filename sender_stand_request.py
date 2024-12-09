# Импорт настроек из модуля/файла configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration
# Импорт библиотеки requests для выполнения HTTP-запросов
import requests
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# POST-ЗАПРОСЫ
# Функция для отправки POST-запроса, на создание Нового Пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

# Функция для отправки POST-запроса, на создание Набора Нового Пользователя
def post_new_client_kit(kit_body, auth_token):
    headers_kit = data.headers.copy()
    headers_kit["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.MAIN_KITS_PATH,
                         json=kit_body,
                         headers=headers_kit)