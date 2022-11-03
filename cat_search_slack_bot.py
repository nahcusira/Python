import slack, urllib.request, time
from flask import *
from slackeventsapi import *
from datetime import *

SLACK_TOKEN = 'xoxb-4157154874326-4155550037543-e6kVyJfN6QtigZ6b52twhJUg'
SIGNING_SECRET="18d9a293cf180a4c3ae1293fa84378ae"
 
app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(SIGNING_SECRET, '/slack/events', app)
 
client = slack.WebClient(token=SLACK_TOKEN)
BOT_ID = client.api_call("auth.test")['user_id']

# def sendImage():
#     urllib.request.urlretrieve('https://cataas.com/cat',"./cat.png")
#     client.files_upload(
#         channels='#a',
#         file="./cat.png",
#     )
# schedule.every(10).seconds.do(sendImage)

@ slack_event_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    if BOT_ID != user_id:
        if text.startswith('!cat'):
            urllib.request.urlretrieve('https://cataas.com/cat/says/'+text[5:],"./cat_search.png")
            client.files_upload(
                channels=channel_id,
                file="./cat_search.png",
            )

    

if __name__ == "__main__":
    app.run(debug=True)




while True:
    urllib.request.urlretrieve('https://cataas.com/cat',"./cat.png")
    upload_text_file = client.files_upload(
        channels='#a',
        file="./cat.png",
)
    time.sleep(30)

