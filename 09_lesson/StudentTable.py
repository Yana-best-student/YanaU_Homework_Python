from sqlalchemy import create_engine
from sqlalchemy.sql import text




class StudentTable:
    db_connection_string = "postgresql://myuser:mypassword@localhost:5432/mydatabase"
    
    # __scripts = {
    #     "select": text("SELECT * FROM student WHERE deleted_at IS NULL"),
    #     "select_active": text("SELECT * FROM student "
    #                           "WHERE \"is_active\" = true AND deleted_at IS NULL"),
    #     "delete_by_id": text("DELETE FROM company WHERE id = :id_to_delete"),
    #     "insert_new": text("INSERT INTO company(name, description) values (:name, :description)"),
    #     "get_max_id": text("SELECT MAX(\"id\") FROM company WHERE deleted_at IS NULL"),
    #     "select by id": text("SELECT * FROM company "
    #                          "WHERE id =:select_id AND deleted_at IS NULL")
    # }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_companies(self):
        return self.__db.execute(self.__scripts["select"]).fetchall()

    def get_active_companies(self):
        return self.__db.execute(self.__scripts["select_active"]).fetchall()

    def delete(self, id):
        self.__db.execute(self.__scripts["delete_by_id"], id_to_delete=id)

    def create(self, name, description):
        with self.__db.begin() as conn:
            conn.execute(self.__scripts["insert_new"], {
                         "name": name, "description": description})

    def get_max_id(self):
        return self.__db.execute(self.__scripts["get_max_id"]).fetchall()[0][0]

    def get_company_by_id(self, id):
        return self.__db.execute(self.__scripts["select by id"], select_id=id).fetchall()