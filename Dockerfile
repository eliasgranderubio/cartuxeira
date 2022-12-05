FROM python:3.9-slim
COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt
COPY cartuxeira /opt/app
COPY ./dockerfiles/run.sh /
RUN chmod +x /run.sh
ENTRYPOINT ["/bin/sh","/run.sh"]