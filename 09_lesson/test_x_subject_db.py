from sqlalchemy import create_engine, text
from sqlalchemy import inspect

db_connection_string = "postgresql://postgres:0511@localhost/QA"
db = create_engine(db_connection_string)


def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert 'subject' in names


def test_insert_new_subject_title():
    db = create_engine(db_connection_string)
    # создаем новый предмет с номером и названием
    insert_sql = text(
        "INSERT INTO subject(\"subject_id\", \"subject_title\") values(:id, :title)")
    my_params = {
        'id': 17,
        'title': 'Physical Education'
    }
    with db.begin() as connection:
        connection.execute(insert_sql, my_params)
        select_sql = text("SELECT * FROM subject WHERE subject_id = :id AND subject_title = :title")
        select_result = connection.execute(select_sql, my_params)
        row = select_result.fetchone()
        assert row['subject_id'] == 17
        assert row['subject_title'] == 'Physical Education'
        delete_sql = text("DELETE FROM subject WHERE subject_id = :id AND subject_title = :title") # удаляем  новый предмет
        connection.execute(delete_sql, my_params)


def test_update_new_subject_title():

    # создаем новый предмет с номером и названием
    sql = text(
        "INSERT INTO subject (subject_id, subject_title) values (:new_id, :new_title)")
    rows = (sql, {'new_id': 17, 'new_title': 'Physical Education'})

    # меняем название предмета
    sql = text(
        "UPDATE subject SET (subject_id, subject_title) values (:new_id, :new_title)")
    rows = (sql, {'new_id': 17, 'new_title': 'Art'})

    # удаляем за собой новый предмет
    sql = text("DELETE FROM subject WHERE subject_id = :new_id")
    rows = db.execute(sql, {"new_id": 17})
