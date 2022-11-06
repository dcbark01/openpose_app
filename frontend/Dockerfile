FROM python:3.10.1-slim

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./src/* ./

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]