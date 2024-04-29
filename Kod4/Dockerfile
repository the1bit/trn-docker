# Képfájl alapként a Python 3.11-es verziójának hivatalos Docker képét használjuk
FROM python:3.11-slim-buster

# Állítsuk be a munkakönyvtárat
WORKDIR /app

# Másoljuk az alkalmazás fájljait a konténerbe
COPY . .

# Telepítsük a szükséges csomagokat a requirements.txt fájl alapján
RUN pip install -r requirements.txt

# Exponáljuk az 80-es portot
EXPOSE 80

# Indítsuk el az alkalmazást
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=80", "--server.address=0.0.0.0"]