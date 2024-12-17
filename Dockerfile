FROM python:3.10

COPY requirements.txt .
COPY .env .  
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir --use-pep517

RUN mkdir /app
WORKDIR /app

COPY static/ /app/static/
COPY templates/ /app/templates/
COPY server.py .
COPY end_point_sripts.py . 


ENTRYPOINT [ "python3", "server.py"]
