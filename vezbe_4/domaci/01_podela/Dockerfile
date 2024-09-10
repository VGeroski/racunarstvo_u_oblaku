FROM python:3.9-slim

WORKDIR /app

COPY split.py /app/

RUN pip install --no-cache-dir pandas scikit-learn

ENTRYPOINT ["python3", "/app/split.py"]
