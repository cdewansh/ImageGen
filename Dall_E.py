import openai
import os
import config

openai.api_key = config.DevelopmentConfig.OPENAI_KEY

user_prompt = input("\nWhat do you want to see?\n")

response = openai.Image.create(prompt = user_prompt, n = 1, size = "1024x1024")

image_url = response['data'][0]['url']

print(image_url)