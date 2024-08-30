FROM python:3.9-slim

# radni direktorijum
WORKDIR	/app

COPY kfold_cv.py .

# potrebne biblioteke
RUN pip install --no-cache-dir pandas scikit-learn

CMD ["python3", "./kfold_cv.py"]
