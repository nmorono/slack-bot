import random
class OCP:

    # Create a constant that contains the default text for the message
    OCP_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Comandos de OC esto se empieza a poner divertido!\nResultado de la ejecucion:\n"
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

    # Generate a random number to simulate 
    def _oc_random_response(self,args):
        rand_int =  random.randint(0,1)
        if rand_int == 0:
            results = "Conectado ok"
        else:
            results = "Conexion rechazada"

        text = f"The result is {args}{results}"

        return {"type": "section", "text": {"type": "mrkdwn", "text": text}},

    # Craft and return the entire message payload as a dictionary.
    def oc_exec(self,text):
        return {
            "ts": self.timestamp,
            "channel": self.channel,
            "username": self.username,
            "icon_emoji": self.icon_emoji,
            "blocks": [
                self.OCP_BLOCK,
                *self._oc_random_response(text),
            ],
        }