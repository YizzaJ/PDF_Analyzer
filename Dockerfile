FROM python:3.9

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir output

CMD ["python", "practica_1/extract.py"]
