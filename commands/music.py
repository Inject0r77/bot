from discord.ext import commands
from discord import FFmpegPCMAudio
from utils.queue import MusicQueue
from utils.youtube import download_audio
from utils.database import get_language
import json

queue = MusicQueue()

def load_localization(language: str) -> dict:
    with open(f'locales/{language}.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def setup_music_commands(bot: commands.Bot):
    @bot.command(name="play")
    async def play(ctx, url: str):
        language = get_language(ctx.guild.id)
        localization = load_localization(language)
        if not ctx.voice_client:
            if ctx.author.voice:
                channel = ctx.author.voice.channel
                await channel.connect()
            else:
                await ctx.send("You need to be in a voice channel!")
                return
        await ctx.send(localization["play"])
        try:
            audio_file = download_audio(url)
            queue.add_track(audio_file)
            await ctx.send(f"Track added to the queue: {audio_file}")
        except Exception as e:
            await ctx.send(f"Error downloading: {e}")
            return

    @bot.command(name="pause")
    async def pause(ctx):
        language = get_language(ctx.guild.id)
        localization = load_localization(language)
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            await ctx.send(localization["pause"])
        else:
            await ctx.send("Nothing is playing currently.")
