# Python 3.11
FROM python:3.11-slim-buster

# Kiinduló munkakönyvtár beállítása
WORKDIR /app

# Fájlok másolása
COPY . .

# Függőségek telepítése
RUN pip install -r requirements.txt

# Port definiálása
EXPOSE 8000

# Flask alkalmazás beállítása
ENV FLASK_APP=app.py


# Flask alkalmazás indítása
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "8000"]