import sqlite3

def get_language(guild_id: int) -> str:
    conn = sqlite3.connect('bot_data.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS guilds (guild_id INTEGER PRIMARY KEY, language TEXT)")
    cursor.execute("SELECT language FROM guilds WHERE guild_id = ?", (guild_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else 'ru'

def set_language(guild_id: int, language: str) -> None:
    conn = sqlite3.connect('bot_data.db')
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO guilds (guild_id, language) VALUES (?, ?)", (guild_id, language))
    conn.commit()
    conn.close()
