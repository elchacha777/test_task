# test_task


### Docker

Create .env 
```bash
docker-compose build
docker-compose up
```
### Without Docker
Activate virtual enviroment

```bash
. venv/bin/activate
```

Install requirements

```bash
pip3 install -r requirements.txt
```

Create .env



```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

Run
```bash
python3 manage.py runserver
```
