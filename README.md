# mp
> ReST API for storing and retrieving moutain peaks.

assessment to apply for 'lead python dev' job: _MFI_.

## Table of Contents
* [General Info](#general-information)
* [Dependencies](#dependencies)
* [Requirements](#requirements)
* [Build Image](#build-image)
* [Run Demo](#run-demo)
* [Contact](#contact)


## General Information
CRUD operations on mountain peaks and listing of peaks inside a bounding box


## Dependencies
- python - version: 3.10.6 (tested)
- fastapi - version: 0.89.1
- uvicorn - version: 0.20.0
- sqlalchemy - version: 1.4.46
- python-dotenv - version: 0.21.1
- psycopg2-binary - version: 2.9.5


## Requirements
- <a href="https://docs.docker.com/engine/install/">docker-ce</a>
- <a href="https://docs.docker.com/compose/install/linux/">docker compose plugin</a>


## Build Image
1. clone the repo
>```bash
> # shell
> git clone https://github.com/mbt101/mp.git
> cd mp
> ```
2. build the image
>```bash
> # shell
> docker build -t mp:1.0.0 .
> ```
3. check image
>```bash
> # shell
> docker images
> # output:
> # REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
> # mp           1.0.0     ...            ...                  ...
> ```
> **NB**: <p> _this image can be pushed to a private/public image repository(f.e. <a href="https://hub.docker.com/search?q=">docker hub</a>) to be pulled later at deployment
> otherwise this building step is required before each deployment if local image is not available._</p>


## Run Demo
1. start services using docker compose plugin
> ```bash
> # shell
> docker compose -f docker-compose.yml up
> ```
2. check services are running, look for api(mp:1.0.0 as image) container and a postgres container(postgres as image)
> ```bash
> # shell
> docker ps
> # output:
> # CONTAINER ID   IMAGE     COMMAND   CREATED  STATUS   PORTS                    NAMES
> # ...            mp:1.0.0  ...       ...      ...      0.0.0.0:8000->8000/tcp   mp-mp-...
> # ...            postgres  ...       ...      ...      0.0.0.0:5432->5432/tcp   mp-db-...
> ```
> **NB**: <p>_the docker-compose.dev.yml declares an extra service(adminer) that makes it easy to observe database changes
> due to API calls_</p>
3. open a browser tab and navigate to http://localhost:8000/swagger:
![swagger screenshot](./images/mp.png)
## Contact
Developed by [Mohamed Ben Thabet](mailto:mohamed.ben.thabet.teams@outlook.com)
