FROM python:3.9.16-slim-buster
COPY . .
RUN pip3 install -r requirements.txt
RUN pip3 install --upgrade tensorflow
CMD ["python", "telegram_app.py"]