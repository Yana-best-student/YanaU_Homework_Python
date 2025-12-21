from sqlalchemy import create_engine
from sqlalchemy.sql import text




class SubjectTable:
    
    

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_subject(self):
        return self.db.execute("SELECT * FROM subject").fetchall()

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