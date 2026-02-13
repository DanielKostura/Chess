# ♟️ Python Chess App

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GUI-Tkinter-green.svg?style=for-the-badge" alt="Tkinter">
  <img src="https://img.shields.io/badge/Type--Checking-Mypy-informational.svg?style=for-the-badge" alt="Mypy">
</p>

---

## 📖 Overview

This is a comprehensive chess application developed in **Python**, focusing on clean architecture and modular design. The application provides a full gameplay experience alongside specialized tools for opening analysis and game-time management.

### ✨ Key Features
* **Modular Architecture:** Strict separation between game logic, graphical interface, and utility modules.
* **Chess Openings Module:** A dedicated system for exploring and studying chess opening theory.
* **Integrated Timer:** Precise dual-clock tracking for competitive match styles (Blitz/Rapid).
* **Email Integration:** Built-in infrastructure to share game results or records via email.
* **Type Safety:** The codebase is fully annotated with Python Type Hinting and verified via `mypy`.

---

## 📂 Project Structure



```bash
chess_app/
├── main.py             # Main entry point of the application
├── logic/              # Core rules, piece movement, and move validation
├── gui/                # UI definitions and graphical components
├── game/               # Game state management and main loop
├── openings/           # Database and UI for chess openings
├── timer/              # Game clock logic and countdowns
├── email/              # Module for email communication and notifications
├── resources/          # Assets: piece images, sounds, and icons
└── utils/              # Helper functions, constants, and shared utilities