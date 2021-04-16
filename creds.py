import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class cred():
    API_TOKEN = os.getenv('API_TOKEN')
    owner_id = os.getenv('OWNER_ID')
    my_db = os.getenv('DB_NAME')
    my_user = os.getenv('USER_NAME')
    my_pass = os.getenv('USER_PASS')
    my_host = os.getenv('HOST_NAME')