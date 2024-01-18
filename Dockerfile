FROM python:3.11

COPY requirements.txt ./requirements.txt

RUN cp /usr/share/zoneinfo/Asia/Almaty  /etc/localtime && \
        /usr/local/bin/python -m pip install --upgrade pip && pip install -r /requirements.txt
