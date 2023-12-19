import requests
import os

api_key = os.getenv("API_KEY")
url = "https://newsapi.org/v2/everything?q=tesla&" \
	   "from=2023-11-19&sortBy=publishedAt&apiKey=" \
	   "a285188888e74daca5d5578b01a3aac2"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the articles titles and descriptions
for article in content["articles"]:
	print(article["title"])
	print(article["description"])
