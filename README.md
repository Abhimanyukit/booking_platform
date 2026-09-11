# booking_platform

## Create Virtual Environment 


```
    python3 -m venv .venv
```
## activate virtual environment 

```
    source .venv/bin/activate
```

## Run the server 

```
    uvicorn app.main:app --reload
```

## The format is:
```
    uvicorn <module>:<variable>
```
## SO
```
    app.main:app
   ↑      ↑
   │      └── FastAPI object
   └──────── Python module

```


