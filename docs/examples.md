# Examples work with PUT/POST

## send data
```bash
curl -X 'POST' http://127.0.0.1:8081/catcher/tests -d '{"test" : "test"}'
```

## structure
`http://` schema

`127.0.0.1` ip

`8081` port

`/catcher` endpoint webhookcatcher

`/tests` table for save data in webhook.json ( using tinydb )

If you change your endpoint path like /catcher/foo `foo` will be used as table in webhook.json

## result
```bash
{
    "uuid":"aea8599a-54e0-4f6a-82c6-af80f6a2399f",
    "date_received":"2022-09-27T20:19:01.152141",
    "headers": {
        "host":"127.0.0.1:8081",
        "user-agent":"curl/7.82.0",
        "accept":"*/*",
        "content-length":"17",
        "content-type":"application/x-www-form-urlencoded"
        },
    "request": {
        "test":"test"
        }
}
```

## retreive data
```bash
curl -X 'GET' \
  'http://127.0.0.1:8081/catcher/tests?limit=10' \
  -H 'accept: application/json'
```

## more

[Swagger](http://127.0.0.1:8081/docs)

[Redoc](http://127.0.0.1:8081/redoc)