FROM python:3.12-slim

WORKDIR /app
COPY ../src /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]
