# 🎲 Snake & Ladder Game (CLI Version)

A simple two-player Snake and Ladder game implemented in Python.

This project is a command-line based simulation of the classic board game where two players compete to reach position 100 first.

---

## 📌 Features

- Two-player turn-based gameplay
- Random dice roll (1–6)
- Snakes and ladders logic implemented using dictionaries
- Extra turn when rolling a 6
- Prevents movement if the dice roll exceeds position 100
- Clear terminal output for game progress

---

## 🧠 Concepts Used

This project demonstrates understanding of:

- Python dictionaries
- Conditional statements
- Loops
- Functions
- Global state management
- Random number generation (`random` module)
- Basic game logic implementation

---

## 🎮 Game Rules

- Both players start at position 1.
- Players take turns rolling a dice.
- If a player lands on:
  - A ladder → they climb up.
  - A snake → they slide down.
- If a player rolls a 6:
  - They get an extra turn.
- The first player to reach exactly position 100 wins.
- A move that exceeds 100 is ignored.

---

## 🚀 How to Run

Make sure you have Python 3 installed.

Run the game using:

```bash
python game.py
