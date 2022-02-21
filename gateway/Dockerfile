FROM python:3.8
workdir /microservices/gateway
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5001
EXPOSE 3231
CMD ["python3", "-u", "gateway.py"]