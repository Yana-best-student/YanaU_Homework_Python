import requests
import pytest


base_url = "https://ru.yougile.com/api-v2"
token = ""
heders = {"Authorization": f"Bearer {token}"}


def test_create_project_post():
    payload = {
        "title": "autotest"
    }
    r = requests.post(
        f"{url}/projects",
        json=payload,
        headers=heders,
    )
    assert r.status_code == 201, r.text
    body = r.json()
    assert isinstance(body.get("id"), str)
    assert body["id"]
