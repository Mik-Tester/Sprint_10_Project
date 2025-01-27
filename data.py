# Заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON.
headers = {
    "Content-Type": "application/json"
}

# Данные пользователя для создания новой записи пользователя в системе, содержат: имя, телефон и адрес пользователя.
user_body = {
    "firstName": "Анатолий",  # Имя пользователя
    "phone": "+79995553322",  # Контактный телефон пользователя
    "address": "г. Москва, ул. Пушкина, д. 10"  # Адрес пользователя
}

# Тело ответа успешно созданного набора.
created_kit_str_name = {
       "name": "Мой набор",
       "card": {
           "id": 1,
           "name": "Под ситуацию"
       },
       "productsList": "null",
       "id": 7,
       "productsCount": 0
   }
