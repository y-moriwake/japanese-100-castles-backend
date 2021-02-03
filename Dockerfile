FROM python:3.9.0
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /code/