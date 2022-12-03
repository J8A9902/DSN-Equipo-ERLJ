import os

DATABASE_URL = os.environ.get('DATABASE_URL')
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
GCP_PROJECT_ID = os.environ.get('GCP_PROJECT_ID')
GCP_SUBSCRIPTION_ID = os.environ.get('GCP_SUBSCRIPTION_ID')
GCP_SUBSCRIBE_TIMEOUT = os.environ.get('GCP_SUBSCRIBE_TIMEOUT')