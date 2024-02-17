from os import getenv

from dotenv import load_dotenv

load_dotenv(".env")

api_id = int(getenv("api_id", None))
api_hash = getenv("api_hash", None)
session = getenv("session", None)
bot_token = getenv("bot_token", None)
db_name = getenv("db_name", None)
mongo_uri = getenv("mongo_uri", None)
owner_id = int(getenv("owner_id", None))
log_pic = getenv("log_pic", "https://telegra.ph//file/43cec0ae0ded594b55247.jpg")
