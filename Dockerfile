# FROM python:3.10
# WORKDIR /apphome
# COPY . /apphome
# RUN pip3 install --no-cache-dir -r requirements.txt
# EXPOSE 5000
# CMD [ "python3", "./app.py" ]

FROM python:3
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]