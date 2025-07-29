FROM python:3.11-slim

WORKDIR /app

COPY run.sh /run.sh
COPY oauth.py /app/oauth.py
COPY requirements.txt /app/requirements.txt

RUN chmod +x /run.sh && \
    pip install --no-cache-dir -r /app/requirements.txt

CMD ["/run.sh"]
