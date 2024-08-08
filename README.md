# Gewichterfassung || Weight recording

## Table of Contents
1. [General Info](#general-info)
2. [Technologies](#technologies)
3. [Installation](#installation)
4. [Running Tests](#running-tests)
5. [Side information](#side-information)

### General Info
***
This is a small project for personal use. I use it to track my weight.

There is still some things to do like documenting the code and a writing a few tests.

## Technologies
***
Used technologies within the project:
* Python 3.12 & PIP
* Virtual Environment: Venv
* Database: SQLite3
* ORM-Framework: SQLAlchemy
* GUI-Toolkit: Tkinter
* Visualization library: Matplotlib
* Database migration tool: Alembic
* Security: Environment File (.env) & Python-Dotenv (library)
* Testing: Pytest

## Installation
***
### 1. Navigate to a new directory and clone the repository
```bash
git clone https://github.com/SebastianKoehler/MealMaster.git
```
### 2. Create and activate a new virtual environment
#### Windows > CMD | PowerShell

1. Create a new virtual environment:
    ```bash
    python -m venv .venv
    ```

2. Activate the new virtual environment:
    - CMD:
        ```bash
        .\.venv\Scripts\activate
        ```
    - PowerShell:
        ```bash
        .\.venv\Scripts\Activate.ps1
        ```

#### macOS / Linux

1. Open the terminal
2. Create a new virtual environment

    ```bash
    python3 -m venv .venv
    ```

3. Activate the new virtual environment

    ```bash
    source ./.venv/bin/activate
    ```
---
### 3. Install dependencies

 ```bash
 pip install -r requirements.txt
 ```
---
### 4. Database migrations
1. Initialize the migration:
    ```bash
    alembic init alembic
    ```
2. Create a new migration:
    ```bash
    alembic revision --autogenerate -m "Initial migration"
    ```
3. Start the migration:
    ```bash
    alembic upgrade head
    ```

---

### 5. Run the application:
 ```bash
 python main.py
 ```
---


## Running Tests

To run all tests, use:
```bash
pytest
```
---

## Side Information
``` 
To use the project you need to create a .env file and customize it,
as example see the .env.example file
```
[Back to Start](#table-of-contents)