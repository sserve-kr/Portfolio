FROM python:3.11.0

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=portfolio.settings.prod

WORKDIR /app

COPY Pipfile Pipfile.lock /app/
RUN pip install setuptools wheel pipenv
RUN pipenv install --system --deploy

COPY docker-entrypoint.sh /app
COPY ./portfolio/ /app/

RUN ["chmod", "+x", "./docker-entrypoint.sh"]

CMD ["./docker-entrypoint.sh"]
