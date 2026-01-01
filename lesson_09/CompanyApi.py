import allure
import requests


class CompanyApi:
    """Класс предоставляет методы для работы с сервером приложения"""

   
    def __init__(self, url):
        self.url = url

    @allure.step("API.Получить список компаний") 
    def get_company_list(self, params_to_add=None):
        resp = requests.get(self.url+'/company/list', params=params_to_add)
        return resp.json()

    @allure.step("api. Получить токен авторизации для пользователя {user}:{password}")
    def get_token(self, user: str ='harrypotter', password: str ='expelliarmus') -> str:
        """
        Получить токен авторизации
        :param user(str): логин пользователя
        :param pasword(str): пароль пользователя
        
        :reteurn: str: токен
        """
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["user_token"]

    @allure.step("api. Получить компанию по {id}") #Передаем id из параметра
    def get_company(self, id):
        resp = requests.get(self.url + '/company/' + str(id))
        return resp.json()
    
    
    @allure.step("api. Создать компанию {name} ({description})")
    def create_company(self, name, description=""):
        company = {
            "name": name,
            "description": description
        }

        my_headers= {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company/create',
                             json=company)
        return resp.json()
    
    

    @allure.step("api. Редактировать компанию {new_id}. {new_name} ({new_descr})")
    def edit_company(self, new_id, new_name, new_descr):
        client_token = self.get_token()
        url_with_token = f"{self.url}/company/update/{new_id}?client_token={client_token}"
        company = {
            "name": new_name,  # Новое имя компании
            "description": new_descr  # Новое описание компании
        }
        resp = requests.patch(url_with_token, json=company)
        return resp.json()
   
    @allure.step("api. Удалить компанию {id}")
    def delete_company(self, id):
        client_token = self.get_token()
        url_with_token = f"{self.url}/company/{id}?client_token={client_token}"

    # Метод отправляет DELETE-запрос
        resp = requests.delete(url_with_token)

    # Возвращаем JSON-ответ
        return resp.json()


     # В названии степа — id (де)активированной компании и ее статус
    @allure.step("api. (Де)активировать компанию {id} -> {isActive}")
    def set_active_state(self, id, is_active):
        client_token = self.get_token()
        url_with_token = f"{self.url}/company/status_update/{id}?client_token={client_token}"
        resp = requests.patch(url_with_token, json={"is_active": is_active})
        return resp.json()
