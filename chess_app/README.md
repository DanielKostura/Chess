# ♟️ Python Chess App

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GUI-Tkinter-green.svg?style=for-the-badge" alt="Tkinter">
  <img src="https://img.shields.io/badge/Type--Checking-Mypy-informational.svg?style=for-the-badge" alt="Mypy">
</p>

---

## 📖 O projekte

Komplexná šachová aplikácia vyvinutá v jazyku Python so zameraním na čistú architektúru a modulárnosť. Aplikácia poskytuje nielen hru samotnú, ale aj nástroje pre analýzu otvorení a správu herného času.

### ✨ Kľúčové vlastnosti
* **Modularita:** Oddelená logika hry, grafické rozhranie a pomocné moduly.
* **Chess Openings:** Špecializovaný modul pre prácu so šachovými otvoreniami.
* **Integrovaný časovač:** Presné sledovanie času pre oboch hráčov.
* **E-mail Modul:** Pripravená infraštruktúra pre zdieľanie výsledkov.
* **Type Safety:** Kód využíva Python Type Hinting pre vyššiu stabilitu.

---

## 📂 Štruktúra projektu

```bash
chess_app/
├── main.py             # Hlavný vstupný bod aplikácie
├── logic/              # Pravidlá hry, pohyb figúrok a validácia
├── gui/                # Definícia okien a grafických komponentov
├── game/               # Správa herného stavu a cyklu
├── openings/           # Databáza a UI pre šachové otvorenia
├── timer/              # Logika herných hodín
├── email/              # Modul pre e-mailovú komunikáciu
├── resources/          # Obrázky figúrok, zvuky a ikony
└── utils/              # Pomocné funkcie a konštanty