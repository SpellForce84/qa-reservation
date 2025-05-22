# 📅 QA Rezervační API – Testovací Projekt

Tento projekt simuluje REST API pro rezervaci služeb jako masáže, konzultace nebo kadeřnické termíny.  
Byl vytvořen za účelem ukázky QA dovedností: návrhu validací, psaní testovacích scénářů, automatizace a kontroly logiky.

---

## 🧪 Co projekt obsahuje

- ✅ FastAPI aplikaci s mock backendem
- ✅ Validaci vstupních údajů (jméno, email, datum, čas, typ služby)
- ✅ Automatizované testy pomocí `pytest` a `TestClient`
- ✅ Ručně napsané test scénáře (`test_cases.md`)
- ✅ GitHub Actions CI pro automatické testování
- ✅ `requirements.txt` a přehledný `README.md`

---

## 🚀 Jak projekt spustit

1. Nainstaluj závislosti:
```bash
pip install -r requirements.txt
Spusť aplikaci:


uvicorn app:app --reload
Otevři API dokumentaci ve webovém prohlížeči:

http://127.0.0.1:8000/docs
Spusť testy:

pytest -v
🔎 Endpoints
Metoda	URL	Popis
POST	/book	vytvoření nové rezervace
GET	/reservations	výpis všech rezervací
DELETE	/reservations/{id}	smazání konkrétní rezervace

🛠 Použité technologie
Python 3.10+

FastAPI

Uvicorn

Pytest

GitHub Actions

🧠 Co tento projekt ukazuje
Schopnost navrhnout a implementovat datové validace

Psaní testovacích scénářů (pozitivní, negativní, hraniční případy)

Automatizaci API testů

Práci s CI/CD (automatické testování při commitu)

Čistou strukturu projektu a orientaci v QA cyklu

🤖 Moje workflow
Při práci na tomto projektu jsem:

návrh API struktury připravil ručně

využil AI jako asistenta pro návrhy validací a formát testů

veškerý výstup jsem sám ověřoval, ladil a testoval

simuloval běžný QA proces jako by šlo o testování reálného backendu

Síla není v tom nepoužívat nástroje – ale v tom umět je správně použít.

✅ CI status

📂 Struktura složek
.
├── app.py                  # FastAPI API
├── validator.py            # Validace vstupů
├── test_api.py             # Automatizované testy
├── test_cases.md           # Manuální test scénáře
├── requirements.txt        # Závislosti
├── README.md               # Tento soubor
└── .github/workflows/test.yml  # CI
📌 Poznámka
Tento projekt byl navržen jako samostatná QA ukázka – není připojen k databázi, vše běží na mock datech v paměti.