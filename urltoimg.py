#using API example code from class
import requests, json
from PIL import Image
# Use the below import line: no package installation is necessary, io is included in python by default
from io import BytesIO

my_key = 'API Key goes here'

#Just search terms, probably changes by API
payload = {
  'client_id': my_key,
  'query': 'island',
  'pages': 1,
  'per_page': 4,
}
# I'm using unsplash for this example, since I have a key for it
endpoint = 'https://api.unsplash.com/photos/random/?client_id=key would be here'
try:
  r = requests.get(endpoint)
  # These lines wil differ per API, but you essentially want to isolate the image URL you want, and store it in an object
  data = r.json()['urls']['raw']
  url = requests.get(data)
  # Once you have the url by itself, use the below line to read it in as an image
  img = Image.open(BytesIO(url.content)) # url can be renamed to anything, whats important is that it stores the image URL we want
  # After you have the image, show or save it
  img.show()
  img.save("test.png")
except:
  print('please try again')