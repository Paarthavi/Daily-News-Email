import requests
import os
from send_email import send_email
from email.mime.text import MIMEText

api_key = os.getenv("API_KEY")
url = f"https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=a285188888e74daca5d5578b01a3aac2"
# &from=2023-11-19

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the articles titles and descriptions
body = ""
for article in content["articles"]:
	#print(article["title"])
	#print(article["description"])
	title = article["title"]
	description = article["description"]

	# Check if description is not None before concatenating
	if description is not None:
		body += title + "\n" + description + 2*"\n"

		format_text = MIMEText(body, 'plain', 'utf-8')

send_email(format_text.as_string())

# Encode the body as UTF-8
#body = body.encode("utf-3")