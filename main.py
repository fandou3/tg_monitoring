from telethon import TelegramClient, events

api_id = ''
api_hash = ''

client = TelegramClient('listener', api_id, api_hash)

@client.on(events.NewMessage)
async def handle_new_message(event):
    if event.is_private:  # 如果这是一条私人消息
        await event.respond('Thanks for your message!423423423')

client.start()
client.run_until_disconnected()