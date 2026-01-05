<<<<<<< HEAD
FROM python:3.9 
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . . 
=======
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
>>>>>>> 296ad6650222a786eb98c7a05bbf7e7ed03bd999
EXPOSE 5000
CMD ["python", "app.py"]
