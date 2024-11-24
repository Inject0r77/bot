from discord.ext import commands
from discord import VoiceChannel

def setup_system_commands(bot: commands.Bot):
    @bot.command(name="join")
    async def join(ctx):
        if ctx.author.voice:
            channel: VoiceChannel = ctx.author.voice.channel
            await channel.connect()
            await ctx.send(f"Подключился к каналу {channel.name}")
        else:
            await ctx.send("Вы должны быть в голосовом канале!")

    @bot.command(name="leave")
    async def leave(ctx):
        if ctx.voice_client:
            await ctx.voice_client.disconnect()
            await ctx.send("Отключился от канала.")
        else:
            await ctx.send("Бот не подключен к голосовому каналу.")
