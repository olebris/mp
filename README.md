# mp
> ReST API for storing and retrieving moutain peaks(demo for assessment)

## Table of Contents
* [General Info](#general-information)
* [Dependencies](#dependencies)
* [Requirements](#requirements)
* [Build Image](#build-image)
* [Run Demo](#run-demo)
* [Shutdown](#shutdown)
* [Settings](#settings)
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

**NB**: 
_this image can be pushed to a private/public image repository(f.e. <a href="https://hub.docker.com/search?q=">docker hub</a>) to be pulled later at deployment otherwise this building step is required before each deployment if local image is not available._</p>


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
3. open a browser tab and navigate to http://localhost:8000/swagger
4. you can use the swagger to interact with the API, the mountain peaks are persisted across services restarts.
> the /peaks/retrieve endpoint accepts two extra query params 'skip' and 'limit' to paginate fetched moutain peaks
> - skip: how many peaks to skip before rendering result
> - limit: how much peaks to include in result

## Shutdown
gracefully shutdown the services:
> ```bash
> # shell
> docker compose -f docker-compose.yml down
> ```


## Settings
- the .env file lists the API settings
```
DATABASE_URL = "postgresql+psycopg2://mp:s3kr3t!@db/peaks"
# 1. !!! production environment: this URL must be encrypted !!!
# 2. (mp,          ,'s3kr3t!'         , db           and peaks) maps respectively to 
#    (POSTGRES_USER, POSTGRES_PASSWORD, service name and POSTGRES_DB) in docker-compose files

ECHO_SQL = False # True/False whether to log SQL queries or Not
```
- the API service in docker-compose files recognizes a set of environment variables:
UVICORN_HOST, UVICORN_WORKER and UVICORN_PORT
```
  mp:
    image: mp:1.0.0
    restart: always
    environment:
      UVICORN_WORKER: <number of workers: defaults to 1 + 2 * 'cpu number'
      UVICORN_PORT: <port: defaults to 8000>
    ports:
      - 8000:8000
``
