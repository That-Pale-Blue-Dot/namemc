FROM python:slim

WORKDIR /app

COPY SRC/ /app  # Copy the contents of the SRC directory to the /app directory in the image

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["python", "/app/bot.py"]
