FROM python:3.9-slim
WORKDIR /code
COPY app.py .
CMD [ "python", "./app.py"]
