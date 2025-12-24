import pytest
from sqlalchemy import create_engine, text
from sqlalchemy import inspect

db_connection_string = "postgresql://postgres:****@localhost/QA"
db = create_engine(db_connection_string)


@pytest.fixture
def db_connection():
    engine = create_engine(db_connection_string)
    connection = engine.connect()

    transaction = connection.begin()
    yield connection
    transaction.rollback()
    connection.close()


def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    assert 'subject' in names


def test_insert_new_subject_title(db_connection):
    transaction = db_connection.begin()
    insert_sql = text(
        "INSERT INTO subject(subject_id, subject_title) VALUES(:id, :title)")
    my_params = {'id': 17, 'title': 'Physical Education'}
    db_connection.execute(insert_sql, my_params)
    transaction.commit()
    select_sql = text(
        "SELECT * FROM subject WHERE subject_id = :id AND subject_title = :title")
    select_result = db_connection.execute(select_sql, my_params)
    row = select_result.fetchone()
    assert row['subject_id'] == 17
    assert row['subject_title'] == 'Physical Education'


def test_update_new_subject_title(db_connection):
    transaction = db_connection.begin()
    insert_sql = text(
        "INSERT INTO subject(subject_id, subject_title) VALUES(:id, :title)")
    my_params = {'id': 17, 'title': 'Physical Education'}
    db_connection.execute(insert_sql, my_params)
    transaction.commit()
    select_sql = text(
        "SELECT * FROM subject WHERE subject_id = :id AND subject_title = :title")
    select_result = db_connection.execute(select_sql, my_params)
    row = select_result.fetchone()
    assert row['subject_id'] == 17
    assert row['subject_title'] == 'Physical Education'
    # # меняем название предмета
    update_sql = text(
        "UPDATE subject SET subject_title = :new_title WHERE subject_id = :id")
    update_params = {'id': 17, 'new_title': 'Art'}
    db_connection.execute(update_sql, update_params)
    transaction.commit()
    select_sql = text("SELECT * FROM subject WHERE subject_id = :id")
    select_result = db_connection.execute(select_sql, {'id': 17})
    row = select_result.fetchone()
    assert row['subject_title'] == 'Art'


def test_delete_subject_title(db_connection):
    initial_count = db_connection.execute(
        text("SELECT COUNT(*) FROM subject")).scalar()
    db_connection.execute(text("INSERT INTO subject (subject_id, subject_title) VALUES (:new_id, :new_title)"), {
                          'new_id': 17, 'new_title': 'Physical Education'})
    db_connection.execute(
        text("DELETE FROM subject WHERE subject_id = :new_id"), {"new_id": 17})
    final_count = db_connection.execute(
        text("SELECT COUNT(*) FROM subject")).scalar()
    assert initial_count == final_count
