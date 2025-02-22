import os
from telethon import TelegramClient, events

# Fetch credentials from environment variables
API_ID = int(os.getenv("25602542"))
API_HASH = os.getenv("03475254c2443fc220b24ce0e0bd4a7d")
BOT_TOKEN = os.getenv("7055619133:AAGTOPJDyaysfQXOcJPRq4c9-dWXHDbf4Pw")

# List of all Telegram Channel IDs (add all 4 channel IDs here)
CHANNEL_IDS = [
    int(os.getenv("-1002432269701")),
    int(os.getenv("-1002231999485")),
    int(os.getenv("-1002419147831")),
    int(os.getenv("-1002303607547"))
]

# Initialize the bot
bot = TelegramClient("bot_session", API_ID, API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.respond("Hello! This bot will automatically accept join requests for all linked channels.")

@bot.on(events.ChatAction)
async def approve_join(event):
    """Automatically approves join requests instantly."""
    if event.user_joined or event.user_added:
        try:
            # Check if the event is for one of the specified channels
            if event.chat_id in CHANNEL_IDS:
                await bot.edit_admin(event.chat_id, event.user_id, invite=True)
                await bot.send_message(event.user_id, "✅ Your join request has been accepted!")
                print(f"Approved request for user {event.user_id} in channel {event.chat_id}")
        except Exception as e:
            print(f"Error approving user {event.user_id} in channel {event.chat_id}: {e}")

print("Bot is running...")
bot.run_until_disconnected()
