from fastapi.testclient import TestClient
from app import app, reservations
from datetime import date, timedelta

client = TestClient(app)

def get_tomorrow_date():
    return (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")

# 🔹 1. Úspěšná rezervace
def test_successful_booking():
    reservations.clear()
    response = client.post("/book", data={
        "name": "Jan Novak",
        "email": "jan@example.com",
        "date": get_tomorrow_date(),
        "time": "10:00",
        "service": "masáž"
    })
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert "reservation" in response.json()

# 🔹 2. Neplatný email
def test_invalid_email():
    response = client.post("/book", data={
        "name": "Eva Novaková",
        "email": "evanovakova.com",
        "date": get_tomorrow_date(),
        "time": "11:00",
        "service": "masáž"
    })
    assert response.json()["success"] is False
    assert "email" in response.json()["message"].lower()

# 🔹 3. Datum v minulosti
def test_past_date():
    yesterday = (date.today() - timedelta(days=1)).strftime("%Y-%m-%d")
    response = client.post("/book", data={
        "name": "Karel",
        "email": "karel@example.com",
        "date": yesterday,
        "time": "12:00",
        "service": "masáž"
    })
    assert response.json()["success"] is False
    assert "minulosti" in response.json()["message"].lower()

# 🔹 4. Kolize času
def test_time_conflict():
    reservations.clear()
    # první rezervace
    client.post("/book", data={
        "name": "Alice",
        "email": "alice@example.com",
        "date": get_tomorrow_date(),
        "time": "13:00",
        "service": "konzultace"
    })
    # pokus o kolizi
    response = client.post("/book", data={
        "name": "Bob",
        "email": "bob@example.com",
        "date": get_tomorrow_date(),
        "time": "13:00",
        "service": "konzultace"
    })
    assert response.json()["success"] is False
    assert "obsazený" in response.json()["message"].lower()

# 🔹 5. Více rezervací stejným emailem
def test_duplicate_user_booking():
    reservations.clear()
    client.post("/book", data={
        "name": "Eva",
        "email": "eva@example.com",
        "date": get_tomorrow_date(),
        "time": "14:00",
        "service": "masáž"
    })
    response = client.post("/book", data={
        "name": "Eva",
        "email": "eva@example.com",
        "date": get_tomorrow_date(),
        "time": "15:00",
        "service": "masáž"
    })
    assert response.json()["success"] is False
    assert "aktivní rezervaci" in response.json()["message"].lower()

# 🔹 6. Neexistující služba
def test_invalid_service():
    response = client.post("/book", data={
        "name": "Tomas",
        "email": "tomas@example.com",
        "date": get_tomorrow_date(),
        "time": "16:00",
        "service": "lékař"
    })
    assert response.json()["success"] is False
    assert "není dostupná" in response.json()["message"].lower()

# 🔹 7. Výpis rezervací
def test_list_reservations():
    response = client.get("/reservations")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# 🔹 8. Smazání rezervace
def test_delete_reservation():
    reservations.clear()
    post_response = client.post("/book", data={
        "name": "Delete Me",
        "email": "delete@example.com",
        "date": get_tomorrow_date(),
        "time": "17:00",
        "service": "masáž"
    })
    res_id = post_response.json()["reservation"]["id"]
    delete_response = client.delete(f"/reservations/{res_id}")
    assert delete_response.status_code == 200
    assert delete_response.json()["success"] is True

# 🔹 9. Smazání neexistující rezervace
def test_delete_nonexistent():
    response = client.delete("/reservations/12345")
    assert response.status_code == 200
    assert response.json()["success"] is False
