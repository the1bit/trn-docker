# Docke példa webalkalmazás

## Python/Flask alkalmazás

Projekt struktúra:

```
.
├── Dockerfile
├── requirements.txt
└── app.py
```

## Projekt változatok:

### Alap változat

Csak a kezőlapon jelenik meg egy üzenet.

- Kezdő mappa:

```bash
cd Kod2/01
```

- Építés:

```bash
docker build --tag python-flask-app:1.0 .
```

- Futtatás:

```bash
docker run -d -p 8001:8000 python-flask-app:1.0
```

- Használat:

  Böngészőben: http://localhost:8001

### Helló változat

A kezdőlapon és a `/hello` útvonalon is megjelenik egy üzenet.

- Kezdő mappa:

```bash
cd Kod2/02
```

- Építés:

```bash
docker build --tag python-flask-app:2.0 .
```

- Futtatás:

```bash
docker run -d -p 8002:8000 python-flask-app:2.0
```

- Használat:

  Böngészőben: http://localhost:8002

### Paraméterek használata

A kezdőlapon, a `/hello` és a `/name` útvonalon is megjelenik egy üzenet. A `/name` útvonalon a `name` paraméter értékét jeleníti meg.

- Kezdő mappa:

```bash
cd Kod2/03
```

- Építés:

```bash
docker build --tag python-flask-app:3.0 .
```

- Futtatás:

```bash
docker run -d -p 8003:8000 python-flask-app:3.0
```

- Használat:

  Böngészőben: http://localhost:8003
