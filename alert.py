import requests
import json
import re
from datetime import date
import config
def retrieve_messages(channelid):
    headers = {
        'authorization': config.auth_key
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages', headers=headers)
    jsonn = json.loads(r.text)

    today = date.today().isoformat()  # Get today's date

    pattern = r"\b([A-Z]{3,4})\b.*?(?=\d+(\.\d+)?\s?[CP])"  # Modified pattern to capture stock ticker and preceding characters

    for value in jsonn:
        timestamp = value['timestamp'].split('T')[0]  # Extract the date from the timestamp
        if timestamp == today:
            content = value['content']
            matches = re.findall(pattern, content, re.IGNORECASE)
            for match in matches:
                stock_ticker = match[0].strip()
                if re.search(r"\b[A-Z]{3,4}\b", stock_ticker):
                    print(f"Stock Ticker: {stock_ticker}")

retrieve_messages(config.channel_id)
