FROM python:3.10

EXPOSE 8000
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
RUN pip install gunicorn
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN mkdir server
COPY ./ /server
WORKDIR server
RUN poetry install --no-interaction
RUN ./manage.py check --deploy
CMD gunicorn config.wsgi:application -b 0.0.0.0:8000
