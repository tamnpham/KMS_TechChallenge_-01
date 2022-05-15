FROM python:3.10.3

RUN apt update
RUN apt install -y git curl gawk

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
