FROM python

ENV PYTHONUNBUFFERED=1 \
    DOCKERIZE_VERSION=v0.6.1

WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock ./
RUN apt update \
 && apt install -y binutils libproj-dev gdal-bin git \
 && pip install -U --no-cache-dir pipenv \
 && pipenv install --system \
 && wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
 && apt purge -y git \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY . ./

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
