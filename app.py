from fastapi import FastAPI, Form
from validator import is_valid_name, is_valid_email, is_valid_datetime, is_valid_service
from typing import List
import uuid

app = FastAPI()

# mock databáze
reservations = []

@app.post("/book")
def book(
    name: str = Form(...),
    email: str = Form(...),
    date: str = Form(...),
    time: str = Form(...),
    service: str = Form(...)
):
    for check_func in [is_valid_name(name), is_valid_email(email), is_valid_datetime(date, time), is_valid_service(service)]:
        if check_func is not True:
            return {"success": False, "message": check_func[1]}

    for r in reservations:
        if r["date"] == date and r["time"] == time:
            return {"success": False, "message": "Tento termín je již obsazený"}
        if r["email"] == email:
            return {"success": False, "message": "Uživatel již má aktivní rezervaci"}

    new_reservation = {
        "id": str(uuid.uuid4()),
        "name": name,
        "email": email,
        "date": date,
        "time": time,
        "service": service
    }
    reservations.append(new_reservation)
    return {"success": True, "message": "Rezervace vytvořena", "reservation": new_reservation}

@app.get("/reservations")
def get_reservations():
    return reservations

@app.delete("/reservations/{res_id}")
def delete_reservation(res_id: str):
    global reservations
    for r in reservations:
        if r["id"] == res_id:
            reservations = [x for x in reservations if x["id"] != res_id]
            return {"success": True, "message": "Rezervace zrušena"}
    return {"success": False, "message": "Rezervace nenalezena"}