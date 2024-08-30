FROM python:3.9

# radni direktorijum
WORKDIR	/app

COPY kfold_cv.py .

# potrebne biblioteke
RUN pip install pandas scikit-learn

CMD ["python3", "./kfold_cv.py"]
