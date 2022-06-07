import logging
from slack_bolt import App
from slack_sdk.web import WebClient
import ssl as ssl_lib
import certifi

ssl_context = ssl_lib.create_default_context(cafile=certifi.where())

DESTINATION_CHANNEL_ID = 'C03JHCF2205'

app = App()


@app.message("Новая игра")
def inform_integration_team(message, say):
    icon_url = 'https://lastfm.freetls.fastly.net/i/u/770x0/0ac15f795306e7f07ecad777a5c24ad1.jpg'
    username = '♂Dungeon♂Master♂'
    destination_channel = DESTINATION_CHANNEL_ID
    text = '''{
    "blocks": [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "Hey, @integration team! The new game is about to release soon. \n Please do not forget to:"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "• Enable the game for the pre-release partner list \n • Apply and sync the profile settings for Booongo and 3oaks \n • Get yourself a cup off coffee"
            }
        }
    ]
}'''
    say(text=text, channel=destination_channel, username=username, icon_url=icon_url)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())
    app.start(3000)
