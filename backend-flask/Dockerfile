FROM python:3.10-slim-buster

# Inside Container
WORKDIR /backend-flask

# Local host filesystem that has repo -> Container filesystem
COPY requirements.txt requirements.txt

# Inside Container
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_ENV=development

EXPOSE ${PORT}
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]