FROM python

WORKDIR /app
COPY requirements.txt .
RUN pip install -U pip -r requirements.txt

COPY . .

CMD [ "python", "-m", "mp" ]