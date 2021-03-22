FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /store
COPY requirements.txt /store/
RUN pip install -r requirements.txt
COPY . /store/