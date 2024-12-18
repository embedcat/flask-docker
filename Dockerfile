FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip
COPY . /app
WORKDIR /app 
RUN pip install -r requirements.txt --break-system-packages
ENTRYPOINT ["python3"]
CMD ["app.py"]
