FROM python:3.8

WORKDIR /ws

RUN pip install --upgrade pip
RUN pip install scipy matplotlib numpy pandas scikit-learn

COPY ./src .