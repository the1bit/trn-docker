# Docker gyakorlati példák



Képzési anyag a Docker használatához.

## Docker alapok

A Docker egy innovatív eszköz, amely segít a fejlesztőknek és rendszergazdáknak az alkalmazások gyors kifejlesztésében, telepítésében és skálázásában konténerizált környezetben. Konténerek segítségével a Docker lehetővé teszi az alkalmazások csomagolását és futtatását izolált környezetben, ami nagyban hozzájárul a platformok közötti kompatibilitáshoz és az infrastruktúra hatékonyságának növeléséhez.

### Miért Docker?

- **Konzisztencia**: A Docker garantálja, hogy az alkalmazás ugyanúgy fut minden környezetben, legyen szó fejlesztői gépről vagy termelési környezetről.
- **Izoláció**: Minden konténer izoláltan működik, így a szoftverek kölcsönös zavarása nélkül futtathatók.
- **Biztonság**: Az izoláció révén a Docker javítja az alkalmazások biztonságát, mivel a konténerek korlátozzák a hozzáférést és erőforrás-használatot.
- **Skálázhatóság és menedzsment**: A Docker lehetővé teszi az alkalmazások könnyű skálázását és kezelését, ami ideálissá teszi őket mikroszolgáltatások architektúrájában.

### Alapvető fogalmak

- **Docker képfájlok**: A Docker képek a szoftvercsomagok állóképei, amelyek tartalmazzák az alkalmazások futtatásához szükséges minden fájlt és könyvtárat.
- **Konténerek**: Az indított Docker képekből létrehozott futtatható példányok, amelyek tartalmazzák az alkalmazást és annak futtatásához szükséges környezetet.
- **Docker Hub**: A Docker saját registry-je, ahol a fejlesztők feltölthetik és letölthetik a különböző Docker képeket.

A Docker alapos megértése kulcsfontosságú a modern szoftverfejlesztési és telepítési folyamatokban. Reméljük, ez a rövid bevezető segít megérteni a Docker alapjait és előnyeit, ami alapozza majd a további mélyebb ismeretek elsajátítását.


## Docker Desktop telepítése

Telepítési link (Mac, Linux, Windows): https://www.docker.com/products/docker-desktop

Miért Docker Desktop?

- Egyszerűen telepíthető
- Minden szükséges komponenst feltelepít
- Erőforrásszükséglet a futtató géphez szabható
- Teljes Docker funkcionalitás (images, DockerHub)
- Helyi Kubernetes (K8s) szerver
- Kiegészítők (monitorozás, egyéb cluster megoldások)

## Docker parancsok

- `docker pull <kép>`: Letölt egy Docker képet a registry-ből.
- `docker run <kép>`: Létrehoz és indít egy konténert a megadott képből.
- `docker ps`: Megjeleníti az aktív konténereket.
- `docker stop <konténer>`: Megállít egy futó konténert.


- Verzió:

```bash
docker version
```

- Docker image lista:

```bash
docker images
```

- Image törlés:

```bash
docker rmi [image neve]:[tag]
```

- Docker konténer futtatása:

```bash
docker run -d -p 80:80 docker/getting-started
```

- Futó Docker konténerek listázása:

```bash
docker ps
```

- Összes Docker konténer listázása:

```bash
docker ps -a
```

- Docker konténer törlése (csak ha le van állítva):

```bash
docker rm [konténer azonosító]
```

- Docker konténer törlése (erőltetve):

```bash
docker rm [konténer azonosító] --force
```


- Image építése Dockerfile alapján:

```bash
docker build --tag [namespace vagy author]]/[image neve]:[verzió] .
```

Megjegyzés: 
- Ha az image fájlt Apple Silicon processzoros gépen készítem, de utána Intel processzoros gépen használom, akkor a fenti parancshoz adjuk hozzá ezt: `--platform linux/amd64`
- Több platformos build: `docker buildx build --tag [kép neve címkével] --push . --platform linux/amd64,linux/arm64,linux/arm/v7`

## Első Docker konténer

## Konténer adatainak ellenőrzése, naplózás

### Konténer adatainak ellenőrzése

```bash
docker inspect [konténer azonosító]
```

### Napló ellenőrzése

```bash
docker logs [konténer azonosító]
```

Megjegyzés: 
- Ha a naplót folyamatosan szeretnénk látni, akkor használjuk a `-f` kapcsolót: `docker logs -f [konténer azonosító]`

## Konténer indítása, leállítása

### Konténer indítása

```bash
docker start [konténer azonosító]
```

### Konténer leállítása

```bash
docker stop [konténer azonosító]
```

## Konténer hálózatok



## Docker fájlrendszer



## Parancsok futtatása konténerben
## Képek kezelése (letöltés, címkézés)
## Képek létrehozása (docker build)

## Docker Compose

### Indítás építéssel

```bash
docker-compose up --build
```

### Indítás

```bash
docker-compose up -d
```

_Megjegyzés: `-d` kapcsolóval a konténerek a háttérben futnak._

### Leállítás

```bash
docker-compose down
```

## Docker alapú alkalmazás saját képből
## Képek tárolása Azure-ban (ACR)

Azure Container Registry (ACR) egy Docker képtároló, amely lehetővé teszi a Docker képek tárolását és kezelését a felhőben. Az ACR használatával a fejlesztők könnyen kezelhetik a Docker képeket, és biztonságosan oszthatják meg őket a csapat tagjaival.

### Azure Container Registry létrehozása (portálból)

1. Lépjen be az Azure Portalba.
2. Keresse meg a "Tárolóregisztrációs adatbázis" szolgáltatást.
3. Kattintson az "Létrehozás" gombra.
4. Adja meg a következő adatokat:
   - Registry name: egyedi név az ACR-hez
   - Subscription: az Azure előfizetése
   - Resource group: az erőforrás csoport neve
   - Location: a régió, ahol az ACR tárolva lesz
   - SKU: az ACR ártervezési modellje

### Docker kép feltöltése az ACR-be

1. Bejelentkezés az ACR-be:

```bash
az acr login --name [ACR név]
```

2. Docker kép címkézése:

```bash
docker tag [kép neve] [ACR név].azurecr.io/[kép neve]:[verzió]
```

_Megjegyzés: `latest` verziót minden esetben töltsünk fel, hogy egyszerűbb legyen az automatizáció._

3. Docker kép feltöltése:

```bash
docker push [ACR név].azurecr.io/[kép neve]:[verzió]
```

## Azure erőforrások létrehozása Docker képből

### Azure Docker instance létrehozása

1. Lépjünk be az Azure Portalba.
2. Keressünk rá a "Tárolópéldányok" szóra a képernyő tetején található keresőmezőben.
3. Kattints a "Tárolópéldányok" lehetőségre.
4. Kattintsunk a "Létrehozás" gombra.
5. Adja meg a következő adatokat:
   - Tároló neve: egyedi név a tárolóhoz
   - Location: a régió, ahol az tároló létrejön
   - Kép forrása: Azure Container Registry
   - Lemezkép: a korábban feltöltött kép
   - Lemezkép-címke: a `latest` vagy a verziószám
   - Operációs rendszer: Linux
   - Méret: 1 vCPU, 1 GB RAM, 0 gpu
6. Kattintsunk a "Következő" gombra.
7. DNS-névcímke: maradhat üresen
8. Portok: 80
9. Kattintsunk a "Következő" gombra.
10. Újraindítási szabályzat: Mindig
11. Kattintsunk a "Következő" gombra.
12. Kattintsunk a "Következő" gombra.
13. Kattintsunk a "Létrehozás" gombra.


## DevOps CI/CD pipeline alkalmazása

### GitHub Actions



### Secrets kezelése GitHub repository-ban, ACR hozzáféréshez

1. Lépjünk be a GitHub repository-ba.
2. Menjünk a "Settings" fülre.
3. Kattintsunk a "Secrets and variables" menüpontra.
4. Válasszuk az "Actions" lehetőséget.
5. Kattintsunk a "New repository secret" gombra.
6. Adja meg a következő adatokat:
   - Name: ACR_LOGIN_SERVER
   - Secret: mentorklub.azurecr.io
7. Kattints az "Add secret" gombra.
8. Ismételje meg az 5-7 lépéseket a következő adatokkal:
   - Name: ACR_USERNAME
   - Secret: [az ACR felhasználóneve]
9. Ismételje meg az 5-7 lépéseket a következő adatokkal:
   - Name: ACR_PASSWORD
   - Secret: [az ACR password vagy password2]


### ACR használata GitHub Actions-ben

1. Clone-ozzuk le a repository-t a gépünkre.
2. Hozzunk létre egy `.github/workflows` mappát a repository gyökérkönyvtárában.
3. Hozzunk létre egy `elso-github-action.yml` fájlt a `.github/workflows` mappában.
4. Másoljuk be a következő kódot a fájlba:

```yaml
```




## Azure Webalkalmazás létrehozása Docker képből

