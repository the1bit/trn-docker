# Kód 3 - Webalkalmazás adatbázissal

## Projekt leírása

## Projekt struktúra

```bash
.
├── backend
│   └── Dockerfile
│
├── frontend
│   ├── Dockerfile
│   ├── app.py
└── └── requirements.txt
 

```

## Hálózat

```bash
docker network create mt-network
```

## Adatbázis

- Építés

```bash
docker build --tag mt-db:latest .
```

### Adattárolás a konténeren belül

```bash
docker run --name adatbazis --network mt-network -d mt-db:latest
```

### Adattárolás a konténeren kívül (persistent volume)

## Perzisztens lemez

```bash
docker volume create mariadb_data
```

```bash
docker run --name adatbazis --network mt-network -d -v mariadb_data:/var/lib/mysql mt-db:latest
```

## Webalkalmazás

- Építés

````bash
docker build --tag mt-web:latest .

```bash
docker run --name web --network mt-network -p 8000:5000 -d -e DB_HOST='adatbazis' -e DB_USER='root' -e DB_PASS='2NUW-a5QdH-8fAXy' -e DB_NAME='adatbazis' mt-web:latest
````
