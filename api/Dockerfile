FROM python:3.9

WORKDIR /app

COPY src/requirements.txt ./
COPY bank.db /app/data/

RUN pip install -r requirements.txt

COPY src /app

EXPOSE 8000

CMD [ "uvicorn", "main:app", "--reload", "--host", "0.0.0.0" ]
