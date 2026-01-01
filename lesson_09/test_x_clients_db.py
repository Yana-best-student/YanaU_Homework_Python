import allure
from time import sleep
from CompanyApi import CompanyApi
from CompanyTable import CompanyTable


@allure.epic("компании") 
@allure.severity("blocker")
@allure.suite("Тесты на работу с компаниями")
class TestCompany:
    api = CompanyApi("http://5.101.50.27:8000")
    db = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")

    # api = CompanyApi("https://x-clients-be.onrender.com")
    # db = CompanyTable("postgresql://x_clients_user:x7ngHjC1h08a85bELNifgKmqZa8KIR40@dpg-cn1542en7f5s73fdrigg-a.frankfurt-postgres.render.com/x_clients_xxet")
    
    @allure.id("SKYPRO-1")
    @allure.story("Получение списка компаний")
    @allure.feature("READ")
    @allure.title("Получение полного списка организаций")
    def test_get_companies(self):
        api_result = self.api.get_company_list()
        db_result = self.db.get_companies()

        with allure.step("Сравнить размеры двух списков"):
            assert len(api_result) == len(db_result)
        
    @allure.id("SKYPRO-2")
    @allure.story("Получение списка компаний")
    @allure.feature("READ")
    @allure.title("Получение списка активных организаций")
    @allure.description("Запрос организаций с параметром active = true")
    @allure.severity("trivial")
    def test_get_active_companies(self):
        filtered_list = self.api.get_company_list(params_to_add={'active': 'true'})
        db_list = self.db.get_active_companies()
        assert len(filtered_list) == len(db_list)
        
    @allure.id("SKYPRO-3")
    @allure.story("Создание компании")
    @allure.feature("CREATE")
    @allure.title("Создание организации")
    def test_add_new_one(self):
        body = self.db.get_companies()
        len_before = len(body)
        name = "Autotest"
        descr = "Descr"
        result = self.api.create_company(name, descr)
        new_id = result["id"]

        body = self.db.get_companies()
        len_after = len(body)    

        with allure.step("Проверить, что список ДО меньше списка после на 1"):    
            assert len_after - len_before == 1    

        with allure.step("Проверить поля новой организации. Корректно заполнены"):    
            for company in body:
                if company["id"] == new_id:
                    assert company["name"] == name
                    assert company["description"] == descr
                    assert company["id"] == new_id       
        
        self.db.delete(new_id)

    @allure.id("SKYPRO-4")
    @allure.story("Получение  компании по id")
    @allure.title("Получение организации по id")
    def test_get_one_company(self):
        name = "Skypro"
        description = "descr"
        self.db.create(name, description)
        max_id = self.db.get_max_id()
        new_company = self.api.get_company(max_id)
        self.db.delete(max_id)
        
        assert new_company["name"] == name
        assert new_company["description"] == description
        assert new_company["is_active"] is True


    # def test_create_new_company(self):
    #     body = self.db.get_companies()
    #     len_before = len(body)
    #     name = "Autotest"
    #     descr = "Descr"
    #     result = self.api.create_company(name, descr)
    #     new_id = result["id"]
    #     body = self.db.get_companies()
    #     len_after = len(body)
    #     assert len_after - len_before == 1
    #     for company in body:
    #         if company["id"] == new_id:
    #             assert company["name"] == name
    #             assert company["description"] == descr
    #             assert company["id"] == new_id
    #             break
    #         self.db.delete(new_id)




# def test_edit():
#     name = "Skypro"
#     description = "descr"
#     db.create(name, description)
#     max_id = db.get_max_id()

#     new_name = "Updated"
#     new_descr = "_upd_"

#     edited = api.edit_company(max_id, new_name, new_descr)

#     db.delete(max_id)

#     # Проверяем, что название компании поменялось
#     assert edited["name"] == new_name
#     # Проверяем, что описание компании поменялось
#     assert edited["description"] == new_descr


# def test_delete():
#     # Добавили компанию через базу:
#     name = "Skypro"
#     description = "descrf"
#     db.create(name, description)
#     max_id = db.get_max_id()

#     # Удалили компанию:
#     deleted = api.delete_company(max_id)

#     assert deleted["company_id"] == max_id
#     assert deleted["detail"] == "Компания успешно удалена"

#     # Проверили по ID, что компании нет в базе:
#     rows = db.get_company_by_id(max_id)
#     assert len(rows) == 0


# def test_deactivate():
#     # Добавили компанию через базу:
#     name = "Skypro"
#     description = "descr"
#     db.create(name, description)
#     max_id = db.get_max_id()

#     # Деактивируем компанию
#     body = api.set_active_state(max_id, False)

#     # Удалили компанию:
#     deleted = api.delete_company(max_id)

#     # Проверяем, что у компании статус «неактивная»
#     assert body["is_active"] is False


# def test_deactivate_and_activate_back():
#     name = "Skypro"
#     description = "descr"
#     db.create(name, description)
#     max_id = db.get_max_id()

#     # Деактивируем компанию с помощью параметра False
#     api.set_active_state(max_id, False)
#     # Активируем компанию с помощью параметра True
#     body = api.set_active_state(max_id, True)
#     deleted = api.delete_company(max_id)
#     # Проверяем, что компания активная
#     assert body["is_active"] is True
