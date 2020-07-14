FROM python:3-alpine

EXPOSE 8080
ADD server.py /server.py
ENTRYPOINT ["python3", "server.py"]
