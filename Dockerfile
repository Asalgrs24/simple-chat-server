FROM ubuntu

WORKDIR /app

RUN apt-get update && apt-get install -y python3

COPY server3.py /app

EXPOSE 5006

CMD ["python3", "/app/server3.py"]


# docker build --tag 'image_name' .