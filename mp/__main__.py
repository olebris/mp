from uvicorn import run
from os import getenv
from multiprocessing import cpu_count


def one_master_process_and_for_each_cpu_two_workers():
    return 1 + 2 * cpu_count()

UVICORN_HOST = getenv("UVICORN_HOST", "0.0.0.0")
UVICORN_PORT = int(getenv("UVICORN_PORT", 8000))
UVICORN_WORKER = int(getenv("UVICORN_WORKER", one_master_process_and_for_each_cpu_two_workers()))

run(
    "mp:app",
    host=UVICORN_HOST,
    port=UVICORN_PORT,
    workers=UVICORN_WORKER
)
