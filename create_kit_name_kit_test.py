import data
import sender_stand_request


# Функция меняет содержимое тела ответа успешно созданного набора
def get_kit_body(name):
    current_kit_body = data.created_kit_str_name.copy()
    current_kit_body["name"] = name
    return current_kit_body

# Функция получения токена
def get_new_user_token():
    created_token_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = created_token_response.json()["authToken"]
    return auth_token

# Функция позитивной проверки
def positive_assert(kit_body):
    auth_token = get_new_user_token()
    created_token_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert created_token_response.status_code == 201
    assert created_token_response.json()["name"] == kit_body['name']

# Функция негативной проверки
def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    created_token_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert created_token_response.status_code == 400

# Тест 1.
# Допустимое количество символов (1)
# ОР: Код ответа - 201
def test_create_kit_1_symbol_in_name_get_successful_response():
    kit_body = get_kit_body("а")
    positive_assert(kit_body)

# Тест 2.
# Допустимое количество символов (511)
# ОР: Код ответа - 201
def test_create_kit_511_symbols_in_name_get_successful_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body)

# Тест 3.
# Количество символов меньше допустимого (0)
# ОР: Код ответа - 400
def test_create_kit_0_symbols_in_name_get_error_response():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

# Тест 4.
# Количество символов больше допустимого (512)
# ОР: Код ответа - 400
def test_create_kit_512_symbols_in_name_get_error_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert_code_400(kit_body)

# Тест 5.
# Разрешены английские буквы (QWErty)
# ОР: Код ответа - 201
def test_create_kit_english_letters_in_name_get_successful_response():
    kit_body = get_kit_body("QWErty")
    positive_assert(kit_body)

# Тест 6.
# Разрешены русские буквы (Мария)
# ОР: Код ответа - 201
def test_create_kit_russian_letters_in_name_get_successful_response():
    kit_body = get_kit_body("Мария")
    positive_assert(kit_body)

# Тест 7.
# Разрешены спецсимволы ("№%@",)
# ОР: Код ответа - 201
def test_create_kit_special_symbols_in_name_get_successful_response():
    kit_body = get_kit_body('"№%@",')
    positive_assert(kit_body)

# Тест 8.
# Разрешены пробелы ( Человек и КО )
# ОР: Код ответа - 201
def test_create_kit_spaces_are_allowable_in_name_get_successful_response():
    kit_body = get_kit_body(" Человек и КО ")
    positive_assert(kit_body)

# Тест 9.
# Разрешены цифры ("123")
# ОР: Код ответа - 201
def test_create_kit_numbers_are_allowable_in_name_get_successful_response():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

# Тест 10.
# Параметр не передан в запросе (kit_body = {})
# ОР: Код ответа - 400
def test_create_no_parameter_in_name_get_error_response():
    kit_body = {}
    negative_assert_code_400(kit_body)

# Тест 11.
# Передан другой тип параметра (число) (123)
# ОР: Код ответа - 400
def test_create_another_type_of_parameter_in_name_get_error_response():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)
