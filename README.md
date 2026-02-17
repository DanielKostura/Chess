# ♟️ Python Chess App

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12+-blue.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/GUI-Tkinter-green.svg?style=for-the-badge" alt="Tkinter">
  <img src="https://img.shields.io/badge/Type--Checking-Mypy-informational.svg?style=for-the-badge" alt="Mypy">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="License">
</p>

---

## 📖 Overview

This is a comprehensive chess application developed in **Python**, focusing on clean architecture and modular design. The application provides a full gameplay experience alongside specialized tools for opening analysis and game-time management.

### ✨ Key Features
* **Modular Architecture:** Strict separation between game logic, graphical interface, and utility modules.
* **Smart AI Opponent:** A built-in AI module that allows players to test their skills against the computer using decision-making algorithms.
* **Chess Openings Module:** A dedicated system for exploring and studying chess opening theory.
* **Integrated Timer:** Precise dual-clock tracking for competitive match styles (Blitz/Rapid).
* **Move Validation:** Robust implementation of chess rules and legal move calculations.
* **Type Safety:** The codebase is fully annotated with Python Type Hinting for better maintainability.

---

## 🤖 AI Engine
The application features a Simple AI that uses a Minimax-based approach to evaluate the board state. It considers:

**1. Material Weight:** Assigning values to pieces (Pawn=100, Knight=320, etc.).

**2. Positional Advantage:** Evaluating piece placement for better control of the center.

**3. Move Search:** Analyzing potential future moves to find the most optimal response.

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
└── utils/              # Helper functions, constants, and shared utilities