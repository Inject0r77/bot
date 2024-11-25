from discord.ext import commands
from utils.database import get_language, set_language
import json

def load_localization(language: str) -> dict:
    with open(f'locales/{language}.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def setup_system_commands(bot: commands.Bot):
    @bot.command(name="join")
    async def join(ctx):
        language = get_language(ctx.guild.id)
        localization = load_localization(language)
        if ctx.author.voice:
            channel = ctx.author.voice.channel
            await channel.connect()
            await ctx.send(localization["join"].format(channel=channel.name))
        else:
            await ctx.send("You need to be in a voice channel!")

    @bot.command(name="leave")
    async def leave(ctx):
        language = get_language(ctx.guild.id)
        localization = load_localization(language)
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send(localization["leave"])
        else:
            await ctx.send("The bot is not in a voice channel.")

    @bot.command(name="language")
    async def language(ctx, lang: str):
        if lang not in ['ru', 'en']:
            await ctx.send("Invalid language. Use 'ru' or 'en'.")
            return
        set_language(ctx.guild.id, lang)
        localization = load_localization(lang)
        await ctx.send(localization["language_switched"])
