from os import environ
from peewee import PostgresqlDatabase

postgresql_connection = PostgresqlDatabase(
  environ.get('POSTGRES_DB'),
  user=environ.get('POSTGRES_USER'),
  password=environ.get('POSTGRES_PASSWORD'),
  host=environ.get('POSTGRES_HOST'),
  port=environ.get('POSTGRES_PORT')
)