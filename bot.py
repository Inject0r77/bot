import discord
from discord.ext import commands
from config import DISCORD_TOKEN

COMMAND_PREFIX = "!"

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.voice_states = True
intents.message_content = True

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents)

from commands.music import setup_music_commands
from commands.system import setup_system_commands

setup_music_commands(bot)
setup_system_commands(bot)

if __name__ == "__main__":
    print("Бот запускается...")
    bot.run(DISCORD_TOKEN)
