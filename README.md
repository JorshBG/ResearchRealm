# Requirements
- Python `3.11.5` or Docker
- Code editor

# Instructions
### With docker
In the root, run the next
```sh
docker-compose build
docker-compose up -d
```

Create a sqlite db in the root project 

`/ResearchRealm/db.sqlite3`

Attach a terminal into docker container and run.
```sh
python manage.py makemigrations
python manage.py migrate
```

### No Docker
Create a virtual Environment and activate
```sh
python -m venv venv
./venv/Scripts/activate
```

Install requirements
```sh
pip install -r requirements.txt
```

Create a sqlite db in the root project 

`/ResearchRealm/db.sqlite3`

Run the migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

Run the server
```sh
python manage.py runserver
```
