# Gewichterfassung || Weight recording

## Setup

### 1. Create and activate a new virtual environment

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
### 2. Install dependencies

 ```bash
 pip install -r requirements.txt
 ```
---
### 3. Create a `.env` file based on the `.env.example`:

 ```plaintext
FLASK_ENV=development
FLASK_APP=run.py
SQLALCHEMY_DATABASE_URI=sqlite:///example.db
TEST_DATABASE_URI=sqlite:///:memory:
SECRET_KEY=your_generated_secret_key
 ```
---
### 4. Create a new secret key and replace the placeholder

 ```python
import secrets

print(secrets.token_hex(24))
 ```

---
### 5. Run the application:
 ```bash
 python run.py
 ```
---

## Running Tests

To run all tests, use:
```bash
pytest
```
---
## Technologies

- Python 3.12
- Flask
- SQLite
- SQLAlchemy
- Flask-Migrate
- Tkinter
- Matplotlib
- python-dotenv
- pytest

---

### 4. Database migrations
#### 1. Initialise the migration:
```bash
flask db init
```

#### 2. Create a new migration:
```bash
flask db migrate -m "Initial migration."
```

#### 3. Start the migration:
```bash
flask db upgrade
```
---
