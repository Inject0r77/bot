from discord.ext import commands
from discord import FFmpegPCMAudio
from utils.queue import MusicQueue
from utils.youtube import download_audio

queue = MusicQueue()

def setup_music_commands(bot: commands.Bot):
    @bot.command(name="play")
    async def play(ctx, url: str):
        if not ctx.voice_client:
            if ctx.author.voice:
                channel = ctx.author.voice.channel
                await channel.connect()
            else:
                await ctx.send("Вы должны быть в голосовом канале!")
                return

        await ctx.send("Загружаю трек, подождите...")
        try:
            audio_file = download_audio(url)
            queue.add_track(audio_file)
            await ctx.send(f"Трек добавлен в очередь: {audio_file}")
        except Exception as e:
            await ctx.send(f"Ошибка загрузки: {e}")
            return

        if not ctx.voice_client.is_playing():
            await play_next(ctx)

    async def play_next(ctx):
        next_track = queue.get_next_track()
        if next_track:
            ctx.voice_client.play(
                FFmpegPCMAudio(next_track),
                after=lambda e: bot.loop.create_task(play_next(ctx)),
            )
            await ctx.send(f"Играет: {next_track}")
        else:
            await ctx.send("Очередь пуста.")

    @bot.command(name="pause")
    async def pause(ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            await ctx.send("Воспроизведение приостановлено.")
        else:
            await ctx.send("В данный момент ничего не воспроизводится.")

    @bot.command(name="stop")
    async def stop(ctx):
        if ctx.voice_client:
            ctx.voice_client.stop()
            queue.clear()
            await ctx.send("Воспроизведение остановлено и очередь очищена.")
        else:
            await ctx.send("Бот не воспроизводит музыку.")

    @bot.command(name="plist")
    async def plist(ctx):
        tracks = queue.list_tracks()
        if tracks:
            await ctx.send("Очередь треков:
" + "\n".join(tracks))
        else:
            await ctx.send("Очередь пуста.")
