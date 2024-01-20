!pip install cryptography

import secrets
from cryptography.fernet import Fernet

# Generate a secret key for the Flask web server
AIRFLOW__WEBSERVER__SECRET_KEY= secrets.token_hex(16)
POSTGRES_PASSWORD= secrets.token_hex(16)
POSTGRES_MB_PASSWORD= secrets.token_hex(16)
_AIRFLOW_WWW_USER_PASSWORD= secrets.token_hex(16)

# Generate a Fernet key for encrypting Airflow connections and variables
AIRFLOW__CORE__FERNET_KEY = Fernet.generate_key().decode()  # Decode to string for readability

print("AIRFLOW__WEBSERVER__SECRET_KEY:", AIRFLOW__WEBSERVER__SECRET_KEY)
print("AIRFLOW__CORE__FERNET_KEY:", AIRFLOW__CORE__FERNET_KEY)
print("POSTGRES_PASSWORD:", POSTGRES_PASSWORD)
print("POSTGRES_MB_PASSWORD:", POSTGRES_MB_PASSWORD)
print("_AIRFLOW_WWW_USER_PASSWORD:", _AIRFLOW_WWW_USER_PASSWORD)
