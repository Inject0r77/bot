import discord
from discord.ext import commands
from commands.system import setup_system_commands
from commands.music import setup_music_commands

# Конфигурация
from config import DISCORD_TOKEN

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Регистрация команд
setup_system_commands(bot)
setup_music_commands(bot)

# Запуск бота
if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
