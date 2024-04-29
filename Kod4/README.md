# Docker példa webalkalmazás



## Python/Streamlint alkalmazás

Projekt struktúra:

```
.
├── .dockerignore
├── Dockerfile
├── requirements.txt
└── app.py
```


## Építés és futtatás

- Kezdő mappa:

```bash
cd Kod4
```

- Építés:

```bash
docker build --tag python-streamlit-webapp:1.0 .
```

- Futtatás:

```bash
docker run -d -p 8081:8501 python-streamlit-webapp:1.0
```

- Használat:

  Böngészőben: http://localhost:8081

