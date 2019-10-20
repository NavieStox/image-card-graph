FROM python:3.7


RUN pip install --upgrade pip
ADD ./requirement.txt /web/
WORKDIR /web
RUN pip install -r requirement.txt