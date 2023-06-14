FROM python:slim
WORKDIR /app
COPY SRC/requirements.txt .
RUN pip install -r requirements.txt
COPY SRC .
CMD [ "python", "main.py" ]
