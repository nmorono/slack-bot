from slack import WebClient
from coinbot import CoinBot
import os

# Create a slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))

# Get a new CoinBot
coin_bot = CoinBot("#paas-con-bot")

# Get the onboarding message payload
message = coin_bot.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)