# Koristimo Python bazni image
FROM python:3.9-slim

# Kopiramo samo skriptu u radni direktorijum
WORKDIR /app
COPY app.py /app/

# Instaliramo potrebne biblioteke
RUN pip install --no-cache-dir Flask scikit-learn pandas

# Port na kojem Flask pokreće aplikaciju
EXPOSE 5000

# Pokrećemo aplikaciju
CMD ["python3", "./app.py"]
