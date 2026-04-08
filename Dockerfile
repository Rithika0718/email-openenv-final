FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV HF_TOKEN=dummy_key

CMD ["python", "inference.py"]