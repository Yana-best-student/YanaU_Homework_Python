from CompanyApi import CompanyApi
from CompanyTable import CompanyTable


api = CompanyApi("http://5.101.50.27:8000")
db = CompanyTable("postgresql://qa:skyqa@5.101.50.27:5432/x_clients")


def test_get_companies():
    # Шаг1: получить список компаний через API:
    api_result = api.get_company_list()

    # Шаг2: получить список компаний из БД:
    db_result = db.get_companies()

    # Шаг2: проверить, что списки равны
    assert len(api_result) == len(db_result)


def test_get_active_companies():
    filtered_list = api.get_company_list(params_to_add={'active': 'true'})
    db_list = db.get_active_companies()
    assert len(filtered_list) == len(db_list)


def test_add_new_one():
    body = api.get_company_list()
    len_before = len(body)

    name = "Autotest"
    descr = "Descr"
    result = api.create_company(name, descr)
    new_id = result["id"]

    body = api.get_company_list()
    len_after = len(body)

    db.delete(new_id)

    assert len_after - len_before == 1
    names = [company["name"] for company in body]
    assert name in names


def test_add_new():
    body = db.get_companies()
    len_before = len(body)

    name = "Autotest"
    descr = "Descr"
    result = api.create_company(name, descr)
    new_id = result["id"]

    body = db.get_companies()
    len_after = len(body)

    assert len_after - len_before == 1

    for company in body:
        if company["id"] == new_id:
            assert company["name"] == name
            assert company["description"] == descr
            assert company["id"] == new_id
            break

    db.delete(new_id)


def test_get_one_company():
    name = "Skypro"
    description = "descr"
    db.create(name, description)
    max_id = db.get_max_id()

    # Получение компании
    new_company = api.get_company(max_id)

    # Удаление
    db.delete(max_id)

    # Проверим название, описание и статус новой компании:
    assert new_company["name"] == name
    assert new_company["description"] == description
    assert new_company["is_active"] is True


def test_edit():
    name = "Skypro"
    description = "descr"
    db.create(name, description)
    max_id = db.get_max_id()

    new_name = "Updated"
    new_descr = "_upd_"

    edited = api.edit_company(max_id, new_name, new_descr)

    db.delete(max_id)

    # Проверяем, что название компании поменялось
    assert edited["name"] == new_name
    # Проверяем, что описание компании поменялось
    assert edited["description"] == new_descr


def test_delete():
    # Добавили компанию через базу:
    name = "Skypro"
    description = "descrf"
    db.create(name, description)
    max_id = db.get_max_id()

    # Удалили компанию:
    deleted = api.delete_company(max_id)

    assert deleted["company_id"] == max_id
    assert deleted["detail"] == "Компания успешно удалена"

    # Проверили по ID, что компании нет в базе:
    rows = db.get_company_by_id(max_id)
    assert len(rows) == 0



def test_deactivate():
    # Добавили компанию через базу:
    name = "Skypro"
    description = "descr"
    db.create(name, description)
    max_id = db.get_max_id()

    # Деактивируем компанию
    body = api.set_active_state(max_id, False)

    # Удалили компанию:
    deleted = api.delete_company(max_id)

    # Проверяем, что у компании статус «неактивная»
    assert body["is_active"] is False


def test_deactivate_and_activate_back():
    name = "Skypro"
    description = "descr"
    db.create(name, description)
    max_id = db.get_max_id()
   
    # Деактивируем компанию с помощью параметра False
    api.set_active_state(max_id, False)
    # Активируем компанию с помощью параметра True
    body = api.set_active_state(max_id, True)
    deleted = api.delete_company(max_id)
    # Проверяем, что компания активная    
    assert body["is_active"] is True  
