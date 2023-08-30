# Base image
FROM python:3.10-slim
# FROM gcr.io/google.com/cloudsdktool/cloud-sdk:slim@sha256:4bca8e5ea927bf040bdb31683b45f4daa9b5106fa749c46095072567a437389f
# FROM gcr.io/dna-retailermedia-dev-afab/aam@sha256:de15a645fe8a698d51f237b3be889fc2f9f05c71505f57c9e08217ffa71a4ce5




ENV PORT 8080


WORKDIR /app


# LINUX:
RUN apt-get update && apt-get install -y git
RUN apt-get install -y python3.10
RUN apt-get install postgresql:14

# GIT:
# RUN git clone -b ${app_tag} https://${github_token}@github.com/procter-gamble/ds-cf-aam-app.git
RUN git clone https://github.com/dmerz75/vb2x.git

WORKDIR /app/vb2x

RUN pwd
RUN ls
RUN echo "-listsubdirs-"
RUN ls *
RUN pip install --upgrade pip
RUN pip install .

RUN cd vbsite && pip install -r requirements.txt
RUN cd vbsite && ./run_db_migrations.sh
RUN cd vbsite && ./run.sh

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

ENTRYPOINT ["python3", "hello.py"]


