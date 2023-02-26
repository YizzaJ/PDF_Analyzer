FROM python:3.9

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

WORKDIR /app

COPY . /app

RUN /root/.poetry/bin/poetry install --no-dev

CMD ["python", "practica_1/analyze.py"]
