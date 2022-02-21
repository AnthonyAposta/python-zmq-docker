FROM python:3.8
workdir /microservices/crawler
COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5001
CMD ["python3", "-u",  "crawler.py"]