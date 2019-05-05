FROM python:3
RUN pip install flask flask_sqlalchemy
ENV FLASK_APP /code/srik_test.py
RUN mkdir code 
COPY . /code
RUN chmod 755 /code/test.py