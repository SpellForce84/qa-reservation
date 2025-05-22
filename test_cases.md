# 🧪 Test Scénáře – Rezervační API

## Cíl testování
Ověřit správnou funkčnost API pro správu rezervací služeb (vytvoření, výpis, mazání) včetně validace vstupních dat a logiky.

---

## 🔹 Test Case 1 – Úspěšná rezervace

- **Název**: Rezervace správně zadaných údajů
- **Kroky**:
  1. Odešli `POST /book` s:
     - name: "Jan Novak"
     - email: "jan@example.com"
     - date: zítřejší datum
     - time: "10:00"
     - service: "masáž"
- **Očekávaný výsledek**: HTTP 200, `success: true`, vrácená rezervace s ID

---

## 🔹 Test Case 2 – Neplatný email

- **Název**: Chybně zadaný email
- **Vstup**: `email: janexample.com`
- **Očekávaný výsledek**: `success: false`, zpráva obsahuje "formát emailu"

---

## 🔹 Test Case 3 – Datum v minulosti

- **Název**: Rezervace včerejšího data
- **Vstup**: `date: včerejší datum`
- **Očekávaný výsledek**: `success: false`, zpráva obsahuje "minulosti"

---

## 🔹 Test Case 4 – Kolize času

- **Předpoklad**: Existuje rezervace na "2025-05-24" v "14:00"
- **Vstup**: Nová rezervace se stejným datem a časem
- **Očekávaný výsledek**: `success: false`, zpráva obsahuje "již obsazený"

---

## 🔹 Test Case 5 – Více rezervací jedním uživatelem

- **Předpoklad**: Už existuje rezervace pro `email: eva@example.com`
- **Vstup**: Další rezervace stejným emailem
- **Očekávaný výsledek**: `success: false`, zpráva obsahuje "má aktivní rezervaci"

---

## 🔹 Test Case 6 – Neexistující služba

- **Vstup**: `service: "lékař"`
- **Očekávaný výsledek**: `success: false`, zpráva obsahuje "není dostupná"

---

## 🔹 Test Case 7 – Výpis rezervací

- **Akce**: `GET /reservations`
- **Očekávaný výsledek**: seznam aktuálních rezervací

---

## 🔹 Test Case 8 – Smazání rezervace

- **Akce**: `DELETE /reservations/{id}`
- **Očekávaný výsledek**: `success: true`, zpráva o úspěšném smazání

---

## 🔹 Test Case 9 – Smazání neexistující rezervace

- **Akce**: `DELETE /reservations/neexistujici-id`
- **Očekávaný výsledek**: `success: false`, zpráva o nenalezení

---

## ✍️ Poznámky
- Časy testovat v různých formátech (`10:00`, `10:0`, `1000`)
- Jména s apostrofy a pomlčkami
- E-maily s podtržítky, čísly, více doménami