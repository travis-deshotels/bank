FROM python:3.9

WORKDIR /app

COPY src/requirements.txt ./

RUN pip install -r requirements.txt

COPY src /app

EXPOSE 5000

CMD [ "flask", "--app", "app", "run", "--host", "0.0.0.0" ]
