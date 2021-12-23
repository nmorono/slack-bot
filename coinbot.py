# import the random library to help us generate the random numbers
import random

# Create the CoinBot Class
class CoinBot:

    # Create a constant that contains the default text for the message
    COIN_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Sure! Flipping a coin....\n\n"
            ),
        },
    }

    # The constructor for the class. It takes the channel name as the a
    # parameter and then sets it as an instance variable
    def __init__(self, channel):
        self.channel = channel
        self.username = "PaaS-bot"
        self.icon_emoji = ":bender_angry:"
        self.timestamp = ""
        self.reaction_task_completed = False
        self.pin_task_completed = False

    # Generate a random number to simulate flipping a coin. Then return the
    # crafted slack payload with the coin flip message.
    def _flip_coin(self):
        rand_int =  random.randint(0,1)
        if rand_int == 0:
            results = "Heads"
        else:
            results = "Tails"

        text = f"The result is {results}"

        return {"type": "section", "text": {"type": "mrkdwn", "text": text}},

    # Craft and return the entire message payload as a dictionary.
    def get_message_payload(self):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.COIN_BLOCK,
                *self._flip_coin(),
            ],
        }