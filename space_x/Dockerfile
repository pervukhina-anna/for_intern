FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
CMD ["uvicorn", "space_x.main:app", "--host", "0.0.0.0", "--port", "80"]
#CMD ["python", "grahql_to_postgre.py"]
