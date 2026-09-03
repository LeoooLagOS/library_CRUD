# 📚 CLI Library Management System

A professional, modular Command-Line Interface (CLI) application for library management, built with Python. This project implements a robust CRUD architecture with transactional logic for borrowing and returning books, while enforcing database engineering principles at the application level.

## ✨ Features

- **Database Normalization:** Enforces First Normal Form (1NF) on the `User` model by strictly separating atomic attributes (First Name, Paternal Last Name, Maternal Last Name).
- **Transactional Logic:** Simulates database transactions during the loan/return process, ensuring data integrity across both `users.json` and `books.json` simultaneously.
- **Internationalization (i18n):** Fully bilingual UI (English / Spanish) decoupled from the core logic using a custom namespace-based dictionary engine.
- **Advanced CLI UX:** Rich terminal interface with interactive menus, color-coded status tables, automated ID generation, and robust input validation (with `:q` abort protocols).
- **Persistent Storage:** OS-agnostic JSON file storage for lightweight, reliable data persistence.

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **UI Rendering:** [Rich](https://github.com/Textualize/rich) (Terminal formatting and tables)
- **Data Persistence:** JSON (Standard Library)

## 🗂️ Project Structure

The project follows a clean separation of concerns:

```text
.
├── core/               # Business logic, models, and data access
│   ├── models.py       # Data classes (User, Book)
│   └── storage.py      # JSON Read/Write operations
├── data/               # Persistent data files
│   ├── books.txt       # Book catalog (JSON format)
│   └── users.txt       # User registry (JSON format)
├── ui/                 # View layer and UI rendering
│   ├── i18n.py         # Bilingual translation engine
│   ├── menus.py        # Interactive CLI menus and controllers
│   └── tables.py       # Rich table generation
├── main.py             # Application orchestrator
└── requirements.txt    # Project dependencies
```

## 🚀 Installation & Setup
Clone the repository:
```Bash
    git clone https://github.com/LeoooLagOS/library_CRUD
```

Create and activate a virtual environment:
```Bash
    python -m venv .venv
    source .venv/bin/activate
```

Install dependencies:
```Bash
    pip install -r requirements.txt
```

Run the application:
```Bash
    python main.py
```