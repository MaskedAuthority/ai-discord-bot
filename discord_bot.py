import discord
from openai import OpenAI
from pathlib import Path
import psycopg2
import time
from pydub import AudioSegment
from pydub.playback import play

selectSql = """
select sender, content from chats order by id desc limit 2
"""

ai = OpenAI(api_key="your open ai key")
ai = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

def say(msg):
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = ai.audio.speech.create(model="tts-1", voice="echo", input=msg)
    response.stream_to_file(speech_file_path)
    sound = AudioSegment.from_file(speech_file_path)
    play(sound)

def me():
    audio_file = open("/path/to/file/audio.mp3", "rb")
    transcript = ai.audio.transcriptions.create(model="whisper-1", file=audio_file)

aethyPrompt = f"""
describe your ai
"""

systemMsg = {"role": "system", "content": aethyPrompt}

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged on as {client.user}!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    completion = ai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=([systemMsg]),
        temperature=0.8,
        frequency_penalty=0.2,
        stop=["<br>"],
    )

    response = completion.choices[0].message.content.strip()

    if response:  # Check if response is not empty
        try:
            await message.channel.send(response)
        except KeyError as e:
            print(f"Error sending message: {e}")
    else:
        print("Received an empty response, not sending a message.")

    print(f"Message from {message.author}: {message.mentions} {message.content}")

@client.event
async def on_guild_available(guild):
    try:
        for sticker in guild.stickers:
            print(f"Sticker available: {sticker.name}")
    except KeyError as e:
        print(f"Encountered an unknown sticker format: {e}")

client.run("your discord token")
