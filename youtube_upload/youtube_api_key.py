api_key = "AIzaSyAPllsbvvJAePVRqZ7QbE7XITZRyoyvzLc"

from googleapiclient.discovery import build

youtube = build('youtube','v3',developerKey = api_key)

request = youtube.channels().list(
        part = 'statistics' ,
        forUsername = 'schafer5'  
)

response = request.execute()

print(response)