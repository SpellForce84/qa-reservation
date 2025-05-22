import re
from datetime import datetime, date, time
from typing import Union

allowed_services = ["masáž", "konzultace", "kadeřník"]

def is_valid_name(name: str) -> Union[bool, tuple[bool, str]]:
    if not (2 <= len(name) <= 16):
        return False, "Jméno musí mít 2 až 16 znaků"
    if not re.fullmatch(r"[A-Za-zÁČĎÉĚÍŇÓŘŠŤÚŮÝŽáčďéěíňóřšťúůýž\-'\s]+", name):
        return False, "Jméno může obsahovat jen písmena, pomlčky a apostrofy"
    return True

def is_valid_email(email: str) -> Union[bool, tuple[bool, str]]:
    if not re.fullmatch(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email):
        return False, "Neplatný formát emailu"
    return True

def is_valid_datetime(res_date: str, res_time: str) -> Union[bool, tuple[bool, str]]:
    try:
        date_obj = datetime.strptime(res_date, "%Y-%m-%d").date()
        time_obj = datetime.strptime(res_time, "%H:%M").time()
    except ValueError:
        return False, "Špatný formát data nebo času (očekává se YYYY-MM-DD a HH:MM)"
    
    today = date.today()
    if date_obj < today:
        return False, "Datum rezervace nemůže být v minulosti"
    
    return True

def is_valid_service(service: str) -> Union[bool, tuple[bool, str]]:
    if service not in allowed_services:
        return False, f"Služba '{service}' není dostupná"
    return True
