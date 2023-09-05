# Base image
FROM python:3.10-slim
# FROM gcr.io/google.com/cloudsdktool/cloud-sdk:slim@sha256:4bca8e5ea927bf040bdb31683b45f4daa9b5106fa749c46095072567a437389f
# FROM gcr.io/dna-retailermedia-dev-afab/aam@sha256:de15a645fe8a698d51f237b3be889fc2f9f05c71505f57c9e08217ffa71a4ce5


ENV PORT 8080

WORKDIR /app

# LINUX:
RUN apt-get update && apt-get upgrade
RUN apt-get -y install git gnupg2 wget vim python3.10 gcc python3-dev gunicorn
# RUN sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
# RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
# RUN apt-get -y update
# RUN apt-get -y install postgresql-14
# RUN postgres psql -c "SELECT version();"

# GIT:
# RUN git clone -b ${app_tag} https://${github_token}@github.com/procter-gamble/ds-cf-aam-app.git
# RUN git clone https://github.com/dmerz75/vb2x.git

COPY ./requirements.txt .
COPY ./vbsite /app
WORKDIR /app/vbsite

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r ../requirements.txt && \
    adduser --disabled-password --no-create-home django-user

ENV PATH="/py/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

USER django-user


RUN pwd
RUN ls
RUN echo "-listsubdirs-"
RUN ls *
# RUN pip install --upgrade pip
# RUN pip install .

# RUN cd vbsite && pip install -r requirements.txt
# RUN cd vbsite && ./run_db_migrations.sh


# Gunicorn as app server
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 4 --timeout 0 app.wsgi:lets_play


# RUN cd vbsite && ./run.sh

# COPY hello.py .

# ARG github_token
# ARG model_type
# ARG model_repo_tag
# ARG aam_io_tag

# WORKDIR /data
# COPY feature_metadata /data/feature_metadata
# COPY test/fake_data.csv /data/tests/test_objects/fake_data.csv
# COPY test/fake_lgbm.bst /data/tests/test_objects/fake_lgbm.bst
# COPY docker/pipeline.py /data/pipeline.py
# COPY docker/pipeline_steps.py /data/pipeline_steps.py
# COPY docker/requirements-deploy.txt /data/requirements-deploy.txt

# RUN git config --global url."https://${github_token}@github.com".insteadOf "https://github.com"

# RUN pip install "git+https://github.com/procter-gamble/ds-cf-aam-model-repo.git@${model_repo_tag}#subdirectory=src/${model_type}"
# RUN pip install -r /data/requirements-deploy.txt
# RUN pip install git+https://github.com/procter-gamble/ds-cf-aam-io@${aam_io_tag}#egg=broadcasting

#, "hello.py"]
# CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 main:app
# ENTRYPOINT ["python", "manage.py", "runserver", "8080"]

# ENTRYPOINT ["python3", "hello.py"]
