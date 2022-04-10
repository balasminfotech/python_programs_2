from dotenv import load_dotenv
load_dotenv()

import os
# Access all environment variables 
# print('*----------------------------------*')
# print(os.environ)
# print('*----------------------------------*')
# # Access a particular environment variable 
# print(os.environ['HOME'])
# print('*----------------------------------*')
# print(os.environ['PATH'])
# print('*----------------------------------*')


# Set environment variables
os.environ['API_USER'] = 'BALA'
os.environ['API_PASSWORD'] = 'KL@$#$$%^%24113SKJjn!@*(!@$$#%$jn13n1jkj'

# Get environment variables
USER = os.getenv('API_USER')
PASSWORD = os.environ.get('API_PASSWORD')

# from decouple import config

# API_USERNAME = config('USER')
# API_KEY = config('KEY')

# # print(USER,PASSWORD)
# if 'API_PASSWORD' in os.environ:
#     print("Environment variable is already Set: ",PASSWORD)


token = os.getenv("NAME")
print(token)