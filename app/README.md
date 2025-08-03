# Environment variables
## Required
    CELERY_REDIS_URL - Redis connection url for celery. Example: 'redis://localhost:6379/0'
    DATABASE_NAME - Postgresql database name. Example: 'test_db'
    DATABASE_HOST - Postgresql database host. Example: 'localhost
    DATABASE_PORT - Postgresql database port. Example: 5432
    DATABASE_USER - Postgresql database user. Example: 'root'
    DATABASE_PASSWORD - Postgresql database password. Example: 'pass123'
    FTSESSION_S_COOKIE - Financial times account session cookie value.
    FTSESSION_S_COOKIE_EXPIRES - Financial times account session cookie expire timestamp

# How to run application
## 1. Install Postgresql
### Ubuntu
    1. Update index
        sudo apt update
    2. Install Postgresql
        sudo apt install postgresql postgresql-contrib
    3. Check that service is running
        sudo systemctl status postgresql
### Windows
    1. Install from official site (https://www.postgresql.org/download/windows/)
## 2. Install Python
### Ubuntu
    1. Add PPA repository
        sudo apt update
        sudo apt upgrade
        sudo add-apt-repository ppa:deadsnakes/ppa
        sudo apt update
    2. Install python
        sudo apt install python3.10 python3.10-venv python3.10-dev
    3. Check
        python3.10 --version
### Windows
    1. Install from official site (https://www.python.org/downloads/release/python-3100/)
## 3. Install dependencies
    1. Create virtual environment
        python3.10 -m venv venv
    2. activate environment
        Ubuntu: source venv/bin/activate
        Windows: venv\Scripts\activate
    3. install dependencies
        cd app
        pip install -r requirements.txt
        playwright install
        playwright install-deps
## 4. Set environment variables
        set REQUIRED env variables in terminal or in .env file inside app folder
## 5. Run application
        While virtual environment active and inside app folder:
            1. Run Celery worker in terminal:
                celery -A celery_app worker --loglevel=info
            2. In other terminal run Celery beat, to schedule periodic task:
                celery -A celery_app beat --loglevel=info
            3. Optional. In other terminal run API:
                uvicorn main:py
