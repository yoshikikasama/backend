import json


def test_create_job(client, normal_user_token_headers):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    response = client.post(
        "/jobs/create-job", data=json.dumps(data), headers=normal_user_token_headers)
    assert response.status_code == 200
    assert response.json()["company"] == "doogle"
    assert response.json()["description"] == "python"


def test_retreive_job_by_id(client, normal_user_token_headers):
    data = {
        "title": "SDE 1 Yahoo",
        "company": "testhoo",
        "company_url": "https://www.fdj.com",
        "location": "USA,NY",
        "description": "Testing",
        "data_posted": "2022-07-20"
    }

    client.post("/jobs/create-job", json.dumps(data), headers=normal_user_token_headers)
    response = client.get("/jobs/get/2")
    print(vars(response))
    assert response.status_code == 200
    assert response.json()["title"] == "SDE 1 Yahoo"
