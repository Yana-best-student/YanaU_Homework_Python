import allure
from sqlalchemy import create_engine
from sqlalchemy.sql import text


class CompanyTable:
    __scripts = {
        "select": text("SELECT * FROM company WHERE deleted_at IS NULL"),
        "select_active": text("SELECT * FROM company "
                              "WHERE \"is_active\" = true AND deleted_at IS NULL"),
        "delete_by_id": text("DELETE FROM company WHERE id = :id_to_delete"),
        "insert_new": text("INSERT INTO company(name, description) values (:name, :description)"),
        "get_max_id": text("SELECT MAX(\"id\") FROM company WHERE deleted_at IS NULL"),
        "select by id": text("SELECT * FROM company "
                             "WHERE id =:select_id AND deleted_at IS NULL")
    }

    def __init__(self, connection_string):
        self.db = create_engine(connection_string).connect()


    @allure.step("БД. Запросить список организаций")
    def get_companies(self):
        query = self.db.execute(self.__scripts["select"])
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()        

    @allure.step("БД. Запросить список активных организаций")
    def get_active_companies(self):
        query = self.db.execute(self.__scripts["select_active"])
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()

    
    @allure.step("БД. Удалить организацию по {id}") # Добавили ID из параметра
    def delete(self, id):
        query = self.db.execute(self.__scripts["delete_by_id"], id_to_delete=id)
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)


    @allure.step("БД. Создать организацию с названием {name}")
    def create(self, name, description):
        with self.db.connect() as conn:
            query = conn.execute(self.__scripts["insert_new"],
                             {"name": name, "description": description})
            allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)    
    
    
    # @allure.step("БД. Создать организацию с названием {name}")
    # def create(self, name, description):
    #     with self.begin() as conn:
    #         conn.execute(self.__scripts["insert_new"], {
    #                      "name": name, "description": description})

    @allure.step("БД. Получить максимальный id организации")
    def get_max_id(self):
        query = self.db.execute(self.__scripts["get_max_id"])
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()[0][0]

    
# def __init__(self, connection_string):
    #     self.__db = create_engine(connection_string)


# @allure.step("БД.Запросить список организаций")
    # def get_companies(self):
    #     return self.__db.execute(self.__scripts["select"]).fetchall()
    
# @allure.step("БД. Запросить организацию по {id}") # Добавили ID из параметра
# def get_company_by_id(self, id):
    #     return self.__db.execute(self.__scripts["select by id"], select_id=id).fetchall()

# @allure.step("БД. Удалить организацию по {id}") # Добавили ID из параметра
    # def delete(self, id):
    #     self.__db.execute(self.__scripts["delete_by_id"], id_to_delete=id)