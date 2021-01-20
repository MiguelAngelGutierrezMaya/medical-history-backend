FROM python:3.9.1-slim-buster

ENV PYTHONUNBUFFERED 1

RUN set -ex \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
  wget \
  gnupg \
  tar \
  libpq-dev

RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" >> /etc/apt/sources.list.d/pgdg.list

RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt-get update \
  # psycopg2 dependencies
  && apt-get install -y postgresql-12 musl-dev \
  # Pillow dependencies
  && apt-get install -y libjpeg-dev libghc-zlib-dev tk-dev tcl-dev \
  # CFFI dependencies
  && apt-get install -y libffi-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # Otros
  && apt-get install -y gcc libc-dev python3-dev g++

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt

COPY ./compose/local/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./compose/local/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
