## slack-bot

Some considerations before run this app.
* [Create the app](#create-the-app)
* [Persmissions](#permissions)
* [Tokens](#tokens)
* [Export Variables in terminal](#export-variables-in-terminal)
* [Run ngrok or another tunneling app. (in the other hand we need a port forwarding in the firewall)](#ngrok)

### STEP BY STEP

we need to create the app in [api.slack](https://api.slack.com/apps)
Create New APP --> From scratch

<img src="./assets/1.png" width="500" height="250">
<img src="./assets/2.png" width="500" height="350">

Set "App Name"
Pick a workspace from the list.

<img src="./assets/3.png" width="500" height="350">

Go to left Menu --> OAuth & Permissions

<img src="./assets/4.png" width="200" height="500">

Go to Bot Token Scopes and add : 
  chat:write.customize (permit to customize bot username and avatar) 
  chat:write (auto added)
  group:history (let connect to the private group)

<img src="./assets/5.png" width="500" height="350">

Next Step install your app --> grant access to the workspace 

<img src="./assets/6.png" width="500" height="350">

Copy the Bot User OAuth Token, this is going to be exported in SLACK_BOT_TOKEN environment variable to get the bot connected.

<img src="./assets/7.png" width="500" height="350">

Go to Basic information, scroll down to App Credentials and Show and Copy Signing Secret, this is going to be exported in SLACK_SIGNING_SECRET to let the bot respond messages.

<img src="./assets/8.png" width="500" height="400">

Go to left menu --> Event Subscriptions --> Enable Events.

Run the aplication 

```
export SLACK_BOT_TOKEN=xoxb-1234567890
export SLACK_SIGNING_SECRET=123456SECRET123456
python app.py
```

Run ngrok 

```
ngrok http 3000
```

Copy the link provided by ngrok and put in request URL adding at the end /slack/events

<img src="./assets/9.png" width="500" height="400">

Scroll down to subscribe to bot events and add message.groups reaction_added and pin_added

<img src="./assets/10.png" width="500" height="400">

Test the bot

