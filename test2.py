import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Set up Slack client
client = WebClient(token=SLACK_BOT_TOKEN)

# Get all channels the bot is a member of
response = client.conversations_list()
channels = response["channels"]

while True:
  # For each channel, send a cat image every 5 minutes
  for channel in channels:
    try:
      response = client.files_upload(
        channels=channel["id"],
        file=open("cat.jpg", "rb")
      )
      print(f"Sent cat image to channel {channel['name']}")
    except SlackApiError as e:
      print(f"Error sending cat image to channel {channel['name']}: {e}")

  # Wait 5 minutes before sending the next cat image
  time.sleep(5 * 60)

  def search_cat_images(query):
  # Use the Slack API to search for cat images matching the given query
   try:
    response = client.search_files(query=query, types=["images"])
    return response["files"]
   except SlackApiError as e:
    print(f"Error searching for cat images: {e}")
    return []
