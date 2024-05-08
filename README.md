# Docker gyakorlati példák

Képzési anyag a Docker használatához.

Ha elakadtál, vagy kérdésed van, írj nekünk: [Hibajelenség / Kérdés](https://github.com/cloudsteak/mentor-klub-cloud/issues/new/choose)

## Tartalomjegyzék

- [Docker alapok](#docker-alapok)
- [Docker Desktop telepítése](#docker-desktop-telepítése)
- [Docker parancsok](#docker-parancsok)
- [Konténer adatainak ellenőrzése, naplózás](#konténer-adatainak-ellenőrzése-naplózás)
- [Konténer indítása, leállítása](#konténer-indítása-leállítása)
- [Konténer hálózatok](#konténer-hálózatok)
- [Docker fájlrendszer](#docker-fájlrendszer)
- [Parancsok futtatása konténerben](#parancsok-futtatása-konténerben)
- [Képek kezelése (letöltés, címkézés)](#képek-kezelése-letöltés-címkézés)
- [Képek létrehozása (docker build)](#képek-létrehozása-docker-build)
- [Docker Compose](#docker-compose)
- [Docker alapú alkalmazás saját képből](#docker-alapú-alkalmazás-saját-képből)
- [Képek tárolása Azure-ban (ACR)](#képek-tárolása-azure-ban-acr)
- [Azure erőforrások létrehozása Docker képből](#azure-erőforrások-létrehozása-docker-képből)
- [DevOps CI/CD pipeline alkalmazása](#devops-cicd-pipeline-alkalmazása)
- [Azure Webalkalmazás létrehozása Docker képből](#azure-webalkalmázás-létrehozása-docker-képből)
- Példák:
  - [Kód 1 - Alap python példa](./Kod1/kod1.md)
  - [Kód 2 - API példa](./Kod2/README.md)
  - [Kód 3 - Docker Compose példa (web + sql)](./Kod3/README.md)
  - [Kód 4 - Webalkalmazás példa](./Kod4/README.md)

## Hasnos linkek

- [Docker desktop letöltése](https://www.docker.com/products/docker-desktop)
- [Git](https://git-scm.com/download/win)
- [Visual Studio Code](https://code.visualstudio.com/Download)
- [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?tabs=azure-cli)

## Docker alapok

A Docker egy innovatív eszköz, amely segít a fejlesztőknek és rendszergazdáknak az alkalmazások gyors kifejlesztésében, telepítésében és skálázásában konténerizált környezetben. Konténerek segítségével a Docker lehetővé teszi az alkalmazások csomagolását és futtatását izolált környezetben, ami nagyban hozzájárul a platformok közötti kompatibilitáshoz és az infrastruktúra hatékonyságának növeléséhez.

- **Miért Docker?**

  - **Konzisztencia**: A Docker garantálja, hogy az alkalmazás ugyanúgy fut minden környezetben, legyen szó fejlesztői gépről vagy termelési környezetről.
  - **Izoláció**: Minden konténer izoláltan működik, így a szoftverek kölcsönös zavarása nélkül futtathatók.
  - **Biztonság**: Az izoláció révén a Docker javítja az alkalmazások biztonságát, mivel a konténerek korlátozzák a hozzáférést és erőforrás-használatot.
  - **Skálázhatóság és menedzsment**: A Docker lehetővé teszi az alkalmazások könnyű skálázását és kezelését, ami ideálissá teszi őket mikroszolgáltatások architektúrájában.

- **Alapvető fogalmak**

  - **Docker képfájlok**: A Docker képek a szoftvercsomagok állóképei, amelyek tartalmazzák az alkalmazások futtatásához szükséges minden fájlt és könyvtárat.
  - **Konténerek**: Az indított Docker képekből létrehozott futtatható példányok, amelyek tartalmazzák az alkalmazást és annak futtatásához szükséges környezetet.
  - **Docker Hub**: A Docker saját registry-je, ahol a fejlesztők feltölthetik és letölthetik a különböző Docker képeket.

A Docker alapos megértése kulcsfontosságú a modern szoftverfejlesztési és telepítési folyamatokban. Reméljük, ez a rövid bevezető segít megérteni a Docker alapjait és előnyeit, ami alapozza majd a további mélyebb ismeretek elsajátítását.

## Docker Desktop telepítése

Telepítési link (Mac, Linux, Windows): https://www.docker.com/products/docker-desktop

Linux és Mac esetén a Docker Desktop telepítése egyszerű, csak letöltjük a telepítőt, és követjük a telepítési utasításokat. Windows esetén a telepítéshez szükség van a WSL 2 (Windows Subsystem for Linux) telepítésére is.

- **Windows telepítési lépések**

Ha Azure VM-en szeretnénk használni a Docker Desktop-ot, akkor a WSL 2 telepítése szükséges. Ehhez olyan géptípusra van szükségünk, amely támogatja a virtualizációt. Ilyen például az Azure Dv3 vagy Ev3 virtuális gépek.

1. A létrehozásnál az alábbiakra kell figyelni (másképpen, nem fog működni a Docker Desktop):
   - Biztonság típua: **Standard**
   - Kép:
      - **Windows Server 2022 Datacenter - x64 Gen2**
      - **Windows 11**
   - Méret: például **Standard D2s v3**   

2. Lépj be a gépbe RDP-n keresztül.
3. Nyiss egy PowerShell-t rendszergazdaként.
4. WSL engedélyezése. Futtasd le az alábbi parancsot:

```PowerShell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

5. Virtális gép funkció engedélyezése. Futtasd le az alábbi parancsot:

```PowerShell
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

6. Indítsd újra a gépet. (`Restart-Computer`)
7. Töltsd le a WSL 2 kernel frissítést a Microsoft oldaláról: https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi
   vagy PowerShell-ben futtasd le az alábbi parancsot:

```PowerShell
wget -Uri https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi -OutFile "$env:USERPROFILE\Downloads\wsl_update_x64.msi"
```

8. Telepítsd a WSL 2 kernel frissítést.

   ```PowerShell
   cd $env:USERPROFILE\Downloads
   .\wsl_update_x64.msi
   ```

9. Nyiss egy PowerShell-t rendszergazdaként. Állítsd be a WSL 2-t alapértelmezett verzióként. Futtasd le az alábbi parancsot:

```PowerShell
wsl --set-default-version 2
```

10. Frissítsd a WSL 2 verzióját. Futtasd le az alábbi parancsot:

```PowerShell
wsl --update
```

11. Telepítsd az Ubuntu 24.04 Linux disztribúciót

```PowerShell
wsl --install -d Ubuntu-24.04
```

12. A telepítés során kérni fogja a felhasználónevet és a jelszót. Ezeket add meg.
13. Töltsd le a Docker Desktop telepítőt a hivatalos weboldalról. (https://www.docker.com/products/docker-desktop)
14. Indítsd el a telepítőt, és kövesd az utasításokat.
15. A telepítés során válaszd ki a WSL 2-t is.
16. Telepítés után kéri, hogy jelentkezz ki a felhasználókkal. Újra indítás a legbiztosabb megoldás, hogy minden rendben legyen.
17. Használatba vehető a Docker Desktop.

- **Miért Docker Desktop?**

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
docker rmi {image neve}:{tag}
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
docker rm {konténer azonosító}
```

- Docker konténer törlése (erőltetve):

```bash
docker rm {konténer azonosító} --force
```

- Image építése Dockerfile alapján:

```bash
docker build --tag {namespace vagy author}/{image neve}:{verzió} .
```

Megjegyzés:

- Ha az image fájlt Apple Silicon processzoros gépen készítem, de utána Intel processzoros gépen használom, akkor a fenti parancshoz adjuk hozzá ezt: `--platform linux/amd64`
- Több platformos build: `docker buildx build --tag {kép neve címkével} --push . --platform linux/amd64,linux/arm64,linux/arm/v7`

## Konténer adatainak ellenőrzése, naplózás

### Konténer adatainak ellenőrzése

```bash
docker inspect {konténer azonosító}
```

### Napló ellenőrzése

```bash
docker logs {konténer azonosító}
```

Megjegyzés:

- Ha a naplót folyamatosan szeretnénk látni, akkor használjuk a `-f` kapcsolót: `docker logs -f {konténer azonosító}`

## Konténer indítása, leállítása

### Konténer indítása

```bash
docker start {konténer azonosító}
```

### Konténer leállítása

```bash
docker stop {konténer azonosító}
```

## Konténer hálózatok

Hálózatkezelése hasonlít a hagyományos hálózatkezeléshez, de a konténerek izoláltak, és saját IP-címmel rendelkeznek.

## Docker fájlrendszer

A fájlrendszer a konténerben a Docker image-ből indul ki, és a konténer futása során módosítható. A fájlrendszer a konténerben lévő fájlokat és könyvtárakat tartalmazza, és lehetővé teszi az alkalmazások számára az adatok tárolását és kezelését.

## Parancsok futtatása konténerben

### Interaktív mód

```bash
docker exec -it {konténer azonosító} bash
```

### Parancs futtatása

```bash
docker exec {konténer azonosító} {parancs}
```

## Képek kezelése (letöltés, címkézés)

### Docker kép letöltése

```bash
docker pull {kép neve}:{verzió}
```

### Docker kép címkézése

```bash
docker tag {kép neve}:{verzió} {új név}:{új verzió}
```

## Képek létrehozása (docker build)

Képeket a progtamkódunk alapján készíthetünk el a Dockerfile segítségével. A Dockerfile egy szöveges fájl, amely tartalmazza azokat az utasításokat, amelyekre a Docker Engine építi a képet.

## Docker Compose

- **Mi az a Docker Compose?**

Docker Compose egy eszköz, amely lehetővé teszi több Docker konténer egyszerű definícióját és indítását egyetlen konfigurációs fájl segítségével. Kifejezetten hasznos fejlesztői környezetekben, teszteléshez és staging környezetekben.

- **Miért hasznos a Docker Compose?**

- **Egyszerűség**: Egyetlen `docker-compose.yml` fájlban kezelhető az összes szolgáltatás, ami egyszerűsíti a konfigurációt.
- **Automatizálás**: Parancssorból egyszerű parancsokkal indíthatók és állíthatók le a szolgáltatások.
- **Környezet konzisztencia**: Biztosítja, hogy a fejlesztői környezet megegyezzen a termelésivel, csökkentve a "nálam működik" típusú problémákat.

- **Hogyan működik a Docker Compose?**

A `docker-compose.yml` fájlban definiálod a szükséges szolgáltatásokat, hálózatokat és tárolókat. A `docker compose up` parancs futtatásával elindítja a definiált konténereket és szolgáltatásokat. A `docker compose down` parancs leállítja és eltávolítja a szolgáltatásokat, hálózatokat és konténereket.

- **Első lépések**

1. Telepítsd a Docker Compose-t (Docker Desktop telepíti).
2. Készíts egy `docker-compose.yml` fájlt, amely tartalmazza a futtatni kívánt szolgáltatásokat.
3. Használd a `docker compose up` parancsot a szolgáltatások indításához.
4. Használd a `docker compose down` parancsot a szolgáltatások leállításához.

_Megjegyzés: `docker compose up -d` kapcsolóval a konténerek a háttérben futnak._

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

Jelenleg Azure Container Registry (ACR) szolgáltatásban tároljuk a Docker képeket, amelyeket a GitHub Actions segítségével automatizáltan telepítünk az Azure Webalkalmazásba.


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

- **Admin Account engedélyezése az ACR-ben**

Ha frissen hoztunk létre egy Azure Container Registry-t, akkor az alapértelmezett beállítások miatt nem tudunk hozzáférni az ACR-hez webalkalmazásból.
Ezért engedélyeznunk kell az Admin Account-ot az ACR-ben. Ennek lépései azure-cli segítségével:

1. Jelentkezzünk be az ACR-be:

```bash
az acr login --name {ACR név}

```

2. Engedélyezzük az Admin Account-ot:

```bash
az acr update -n {ACR név} --admin-enabled true
```

### Docker kép feltöltése az ACR-be

1. Bejelentkezés az ACR-be:

```bash
az acr login --name {ACR név}
```

2. Docker kép címkézése:

```bash
docker tag {kép neve} {ACR név}.azurecr.io/{kép neve}:{verzió}
```

_Megjegyzés: `latest` verziót minden esetben töltsünk fel, hogy egyszerűbb legyen az automatizáció._

3. Docker kép feltöltése:

```bash
docker push {ACR név}.azurecr.io/{kép neve}:{verzió}
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

### GitHub Actions Workflow

- **Mi az a GitHub Actions?**

GitHub Actions egy automatizálási eszköz, amely lehetővé teszi szoftverfejlesztési feladatok automatizálását közvetlenül a GitHub repository-kon belül. Felhasználható tesztek futtatására, build-ek készítésére, deploy folyamatok kezelésére és még sok másra.

- **Miért hasznos a GitHub Actions?**

- **Integráció**: Közvetlenül integrálható a GitHub-al, nem szükséges külső CI/CD eszközöket használni.
- **Rugalmas**: Tetszőleges workflow-k létrehozhatók, amelyek megfelelnek a projekt specifikus igényeinek.
- **Közösségi támogatás (community)**: Hozzáférés számos előre készített "action"-höz, amelyeket a közösség osztott meg.

- **Hogyan működik a GitHub Actions?**

Workflow fájlok (általában `.github/workflows` mappában található YAML fájlok) definiálják a műveleteket, amelyeket egy esemény (például `push`, `pull request`) vált ki. Minden workflow tartalmaz egy vagy több job-ot, amelyek futtathatók ugyanazon runner-en vagy különböző runner-eken. Az Actions lehetővé teszi a folyamatok parallelizálását és az erőforrások hatékony kezelését.

- **Első lépések**

1. Készíts egy `.github/workflows` mappát a repository-ban.
2. Hozz létre egy YAML fájlt, ami leírja a workflow-d (például `build.yml`).
3. Definiálj eseményeket, job-okat és lépéseket a fájlban, amelyek meghatározzák, mi történjen automatizálás során.
4. Commitold és pushold a változásokat, hogy aktiváld a workflow-t.

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
   - Secret: {az ACR felhasználóneve}
9. Ismételje meg az 5-7 lépéseket a következő adatokkal:
   - Name: ACR_PASSWORD
   - Secret: {az ACR password vagy password2}

### ACR használata GitHub Actions-ben

1. Clone-ozzuk le a repository-t a gépünkre.
2. Hozzunk létre egy `.github/workflows` mappát a repository gyökérkönyvtárában.
3. Hozzunk létre egy `elso-github-action.yml` fájlt a `.github/workflows` mappában.
4. Készítsük el a megfelelő CI/CD pipeline-t a fájlban. (nem szükséges a teéjes folyamatot egy fájlban megvalósítani. Lehetséges, hogy egy nagy CI/CD folyamatot több fájlban valósítunk meg.)

Példák:

- [.github/workflows/pelda.yml](/.github/workflows/pelda.yaml)
- [.github/workflows](/.github/workflows)

## Azure Webalkalmazás létrehozása Docker képből

- Webalkalmazás létrehozásánál a Docker képet az Azure Container Registry-ből használjuk. Az Azure Webalkalmazás lehetővé teszi a konténerek gyors és egyszerű telepítését, skálázását és kezelését a felhőben.
- Webalkalmazás módosítása

  1.  Üzembehelyezési központban állítsuk át a `Folyamatos telepítés` értékés `Bekalcsolva`-ra.
  2.  Konfiguráció > Általános beállítások > Mindig bekapcsolva: Be
