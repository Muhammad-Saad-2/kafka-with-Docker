
from starlette.config import Config
from starlette.datastructures import Secret

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()

DATABASE_URL = config("DATABASE_URL", cast=Secret)
BOOTSTRAP_SEVER = config("BOOTSTRAP_SERVER", cast=str)
KAKFKA_ORDER_TOPIC=config("KAFKA_ORDER_TOPIC",cast=str)
KAFKA_CONSUMER_GROUP_ID_FOR_PRODUCT=config("KAFKA_CONSUMER_GROUP_ID_FOR_PRODUCT", cast=str)
