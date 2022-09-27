# Instructions

## Python3
### Clone repo
```bash
git clone https://github.com/odgon/WebhookCatcher
cd WebhookCatcher/src/app
```

### Install requirements
```bash
pip install -r requirements.txt
```

### Launch the api
```bash
uvicorn main:app --port 8081 --reload
```


## Docker
### Clone repo
```bash
git clone https://github.com/odgon/WebhookCatcher
cd WebhookCatcher
```

### Use docker-compose
```bash
docker-compose build
docker-compose up
```