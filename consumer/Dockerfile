FROM python:3.8
workdir /microservices/consumer
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 3231
CMD ["python3", "-u", "consumer.py"]