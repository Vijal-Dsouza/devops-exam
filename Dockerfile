FROM python:3.13-slim

COPY requirements.txt .

RUN pip install requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]

