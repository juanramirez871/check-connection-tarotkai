FROM python:3.12-slim

WORKDIR /src

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    libxrender1 \
    libxtst6 \
    libxi6 \
    libxrandr2 \
    unzip \
    wget \
    cron \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /src/../

COPY .env /src/../

RUN pip install --no-cache-dir -r /src/../requirements.txt

COPY ./src /src

ENV CHROME_BIN=/usr/bin/chromium \
    CHROME_DRIVER=/usr/bin/chromedriver 

RUN echo "*/30 * * * * python3 /src/main.py >> /var/log/cron.log 2>&1" > /etc/cron.d/my-cron-job

RUN chmod 0644 /etc/cron.d/my-cron-job

RUN crontab /etc/cron.d/my-cron-job

RUN touch /var/log/cron.log

CMD export $(cat /src/.env | xargs) && cron && tail -f /var/log/cron.log