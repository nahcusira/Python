import os
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import slack
import requests

# replace TOKEN with your Slack bot token
client = WebClient(
    token='xoxb-4157154874326-4155550037543-kTQK6kpf6sEtiZbCWrAkIZCH')

# define a function that sends a cat image to a Slack channel


def send_cat_image():
    # replace CHANNEL_ID with the ID of the Slack channel you want to send the message to
    channel_id = 'a'

    # get a random cat image URL
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    cat_image_url = response.json()[0]['url']

    # send the cat image to the Slack channel
    try:
        client.chat_postMessage(channel=channel_id, text=cat_image_url)
    except SlackApiError as e:
        print(f'Error: {e.message}')

# define a function that responds to an inline command with a cat image


@slack.RTMClient.run_on(event='message')
def search_cat_image(**payload):
    data = payload['data']

    # check if the message is an inline command
    if data['text'].startswith('/cat'):
        # get the query from the inline command
        query = data['text'].split('/cat')[1].strip()

        # search for cat images with the given query
        response = requests.get(
            f'https://api.thecatapi.com/v1/images/search?q={query}')
        cat_image_url = response.json()[0]['url']

        # send the cat image to the user who sent the command
        try:
            client.chat_postMessage(channel=data['user'], text=cat_image_url)
        except SlackApiError as e:
            print(f'Error: {e.message}')


# run the Slack bot
if __name__ == '__main__':
    # send a cat image every 5 minutes
    while True:
        send_cat_image()
        time.sleep(300)
