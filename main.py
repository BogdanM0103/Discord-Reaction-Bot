from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message

from emojiconverter import emojiConverter
from responses import get_response

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    # Check if the message starts with '#'
    if user_message.startswith('#'):
        user_message = user_message[1:]  # Remove '#' from the message
        emoji_message = emojiConverter(user_message)  # Convert message to emojis

        # Check if emoji_message is a valid list and not empty
        if emoji_message:
            # Join the list into a single string and send it
            await message.channel.send(emoji_message)
        else:
            await message.channel.send('Could not convert message to emojis.')


# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


# STEP 4: HANDLING INCOMING MESSAGES
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# STEP 5: MAIN ENTRY POINT
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
