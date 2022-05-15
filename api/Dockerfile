FROM python:3.10.3

RUN apt update
RUN apt install -y git curl gawk

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "5000"]
