import pytest
import requests
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("API_TOKEN")
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
HEADERS = {"Authorization": f"Bearer {token}"}
baseUrl = "https://ru.yougile.com/api-v2/"


@pytest.fixture
def create_and_delete_project():
    # Создание проекта
    payload = {"title": "Новый проект"}
    r = requests.post(f"{baseUrl}projects", json=payload, headers=HEADERS)
    assert r.status_code == 201
    project_id = r.json().get("id")

    yield project_id

    # Удаление проекта
    payload = {"deleted": True}
    delete_response = requests.put(
        f"{baseUrl}projects/{project_id}", json=payload, headers=HEADERS)
    assert delete_response.status_code == 200, "Failed to delete project"


@pytest.fixture
def company_ID():
    bodyID = {
        'login': login,
        'password': password
    }
    company_ID = requests.post(f"{baseUrl}auth/companies", json=bodyID)
    assert company_ID.status_code == 200, company_ID.text

    response_json = company_ID.json()
    company_ID = response_json['content'][0]['id']
    print(company_ID)
    assert isinstance(company_ID, str)
    return company_ID


# Авторизация


def test_company_ID():
    bodyID = {
        'login': login,
        'password': password
    }
    company_ID = requests.post(f"{baseUrl}auth/companies", json=bodyID)
    assert company_ID.status_code == 200, company_ID.text

    response_json = company_ID.json()
    company_ID = response_json['content'][0]['id']
    print(company_ID)
    assert isinstance(company_ID, str)


def test_key_token(company_ID):
    company_id = company_ID

    creds = {
        'login': login,
        'password': password,
        'companyId': company_id
    }
    key = requests.post(f"{baseUrl}auth/keys", json=creds)
    assert key.status_code == 201, key.text
    print(key.text)

    response_json = key.json()
    key = response_json['key']

    assert isinstance('key', str)

def test_get_key_all(company_ID):
    company_id = company_ID
    creds = {
        'login': login,
        'password': password,
        'companyId': company_id
    }
    key_all = requests.post(f"{baseUrl}auth/keys/get", json=creds)
    assert key_all.status_code == 200, key_all.text
    print(key_all.text)

    response_json = key_all.json()
    keys = [item['key'] for item in response_json]
    for key in keys:
        print(key)




# Создание нового проекта


def test_create_project_positive(create_and_delete_project):
    project_id = create_and_delete_project
    print("Created project ID:", project_id)


def test_create_project_neg():
    payload_neg = {
        "title": ""
    }
    negat = requests.post(f"{baseUrl}projects",
                          json=payload_neg,
                          headers=HEADERS,
                          )
    assert negat.status_code == 400, negat.text
    zero = negat.json()
    assert "title should not be empty" in zero.get("message", [])

    # Изменение проекта


def test_change_project_positive(create_and_delete_project):
    project_id = create_and_delete_project
    new_title = {"title": "Создание и изменение"}
    new = requests.put(f"{baseUrl}projects/{project_id}",
                       json=new_title,
                       headers=HEADERS)
    assert new.status_code == 200, new.text
    change = new.json()
    assert isinstance(change.get("id"), str)
    assert change["id"]


def test_change_project_neg(create_and_delete_project):

    change_new_title = {
        'title': 'Изменение проекта не верным методом'
    }
    change = create_and_delete_project
    new_neg = requests.post(f"{baseUrl}projects/{change}",
                            json=change_new_title,
                            headers=HEADERS,
                            )
    assert new_neg.status_code == 404, new_neg.text
    new_change = new_neg.json()
    assert "Cannot POST" in new_change.get("message", [])

# Получение ID проекта


def test_get_id_positive(create_and_delete_project):
    progect_id = create_and_delete_project
    title = {"title": "Python8"}
    id_posit = requests.get(f"{baseUrl}projects/{progect_id}",
                            headers=HEADERS)
    assert id_posit.status_code == 200, id_posit.text
    id_posit = id_posit.json()


def test_get_id_negative(create_and_delete_project):
    project_id = create_and_delete_project
    title = {"title": "Python8"}
    neg_id = requests.get(f"{baseUrl}projects/invalid_id_123",
                          headers=HEADERS)
    assert neg_id.status_code == 404, neg_id.text
    new_change = neg_id.json()
    assert "Проект не найден" in new_change.get("message", [])
