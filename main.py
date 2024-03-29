import requests
import os
from send_email import send_email
from email.mime.text import MIMEText

topic = "tesla"
api_key = os.getenv("API_KEY")
url = f"https://newsapi.org/v2/everything?" \
	  f"q={topic}&" \
	  "sortBy=publishedAt&" \
	f"apiKey={api_key}&" \
	"language=en"
# &from=2023-11-19

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the articles titles and descriptions
body = "Subject: Today's news\n"
for article in content["articles"][:20]:
	#print(article["title"])
	#print(article["description"])
	title = article["title"]
	description = article["description"]
	article_url = article["url"]

	# Check if description is not None before concatenating
	if description is not None:
		body = body + title + "\n" + description + "\n" + article_url + 2*"\n"

		format_text = MIMEText(body, 'plain', 'utf-8')

send_email(format_text.as_string())

# Encode the body as UTF-8
#body = body.encode("utf-3")