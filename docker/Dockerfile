# Base image
FROM python:3.10-slim

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

ENTRYPOINT ["python"]