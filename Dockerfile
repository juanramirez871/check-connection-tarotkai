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
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /src/../

RUN pip install --no-cache-dir -r /src/../requirements.txt

COPY ./src /src

ENV CHROME_BIN=/usr/bin/chromium \
    CHROME_DRIVER=/usr/bin/chromedriver \
    PASSWORD=xd \
    USER=xd \
    LOGIN_URL=https://xd \
    PANEL_URL=https://xd/index.php?menu=control_panel

CMD ["python", "/src/main.py"]
