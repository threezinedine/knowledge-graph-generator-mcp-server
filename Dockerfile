FROM python:3.11-alpine

WORKDIR /app

COPY . .

RUN pip install "mcp[cli]"

CMD ["python", "main.py"]
