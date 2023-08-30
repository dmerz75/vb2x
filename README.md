# vb2x
Perform doubles volleyball court assignments

# Vars:
1. project id - vb2x-395719
2. region - us-central1
3. git clone https://github.com/dmerz75/vb2x.git

# GCP:
1. 1041817817227@cloudbuild.gserviceaccount.com - service account
2. 1041817817227-compute@developer.gserviceaccount.com
3. https://cloud.google.com/python/django/run


# SQL:
./cloud-sql-proxy PROJECT_ID:REGION:INSTANCE_NAME
./cloud-sql-proxy vb2x-395719:us-central1:server-aa69
                  vb2x-395719:us-central1:psql-aa69
p1041817817227-ii4jhe@gcp-sa-cloud-sql.iam.gserviceaccount.com
user: server-aa69


gcloud sql connect INSTANCE_NAME --user merz.d
gcloud sql connect psql-aa69 --user merz.d

gcloud sql connect psql-aa69 --user server-aa69
gcloud sql connect psql-aa69 --user=postgres   ***

<!-- https://cloud.google.com/sql/docs/postgres/connect-instance-cloud-shell#gcloud -->



# settings/production.py

INSTANCE_CONNECTION_NAME = os.environ("INSTANCE_CONNECTION_NAME)
DATABASES = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'serverless_django_prod_db',
        'USER': 'serverless_django_prod_user',
        'PASSWORD': '<your-password>',
        'HOST': f'/cloudsql/{INSTANCE_CONNECTION_NAME}'
    }
}

# https://docs.djangoproject.com/en/4.2/topics/db/multi-db/
./manage.py migrate --database=users
