# DVMN notify bot
This project's purpose is to check status of works using site API and alert user, if work is reviewed.

## How to install

1. Download repository

2. Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```python
pip install -r requirements.txt
```

## Setting up

For use this scripts, you will need:
- Telegram bot token (use existing one or create new on [@BotFather](http://t.me/BotFather))
- DVMN API token, get it on [dvmn.org](https://dvmn.org/api/docs/) after registering on site
- Your Telegram chat ID

Create .env file in script directory, then put in your tokens and parameters, like:
```python
DVMN_TOKEN="your_devman_token"
TG_BOT_TOKEN="your_bot_token"
TG_CHAT_ID="your_chat_id"
```

## Using script

Before using, you should start conversation with your bot in telegram. Without that bot can`t send you messages.

To start using bot, type

```python
python3 main.py
```

Script will be up and running. Bot alerts you on work status changes.
