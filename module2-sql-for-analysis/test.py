import os
from dotenv import load_dotenv

# def load_settings_from_env(root_path):
#     dotenv.load_dotenv(os.path.join(root_path, '.env')) 

load_dotenv()

password = os.getenv("ELEPHANT_PW")

print(f'pw: {password}')
