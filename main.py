from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message

from emojiconverter import emojiConverter, emojiDictionary

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
client: Client = Client(intents=intents)


# Helper function to flatten the emojiDictionary for easier lookup
def flatten_emoji_dictionary(emoji_dict):
    flat_list = []
    for emoji_group in emoji_dict.values():
        flat_list.extend(emoji_group)
    return flat_list


# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    emoji_list = emojiConverter(user_message)
    flat_emoji_list = flatten_emoji_dictionary(emojiDictionary)

    for emoji in emoji_list:
        if emoji in flat_emoji_list:
            # await message.channel.send(emoji)
            await message.add_reaction(emoji)
            print(f"{emoji} was found!")
        else:
            print(f"{emoji} was not found..")


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
