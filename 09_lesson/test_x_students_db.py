from sqlalchemy import create_engine, inspect, text
import pytest
db_connection_string = "postgresql://postgres:123@localhost/postgres"
db = create_engine(db_connection_string)

def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert names[7] == 'group_student'

def test_insert_new_subject():
    connection = db.connect()
    transaction = connection.begin()

    # создаем новый предмет с номером и названием
    sql = text("insert into subject (subject_id, subject_title) values (:new_id, :new_title)")
    connection.execute(sql, {'new_id': 17,'new_title': 'Latin'})
    # удаляем за собой новый предмет
    sql = text("DELETE FROM subject WHERE subject_id = :new_id")
    connection.execute(sql, {"new_id": 17})

    transaction.commit()
    connection.close()