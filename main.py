import pprint
from telethon import TelegramClient, events
import asyncio

api_id=7145550
api_hash="659da193100cfd421ce6aedf1ef6ea79"
client = TelegramClient('anon', api_id, api_hash)
#channel_id=1194185327
#user_id=1704449472 Efe gencelli
users = [1704449472,817741597,1274728384]

@client.on(events.NewMessage) #(from_users=users)
async def my_event_handler(event):
    print("--------")
    print(event.from_id.user_id)
    #for i in users:
    #    if(event.from_id.user_id == i):
    
    #print("İSTENEN KULLANICIDAN MESAJ")
    print(event.message.raw_text) 
    if(event.message.is_reply):
        await print( event.message.get_reply_message)
    #print(event.message.reply_to)#get_reply_message().
    #print(event.post_author)
    #print(event.stringify())
        #if 'hello' in event.raw_text:
        #    await event.reply('hi!')



client.start()
client.run_until_disconnected()




"""
async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    username = me.username
    print(username)
    print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    async for dialog in client.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)


with client:
    client.loop.run_until_complete(main())
"""

"""

with TelegramClient('test', api_id, api_hash) as client:
    for message in client.iter_messages("Win300"):
        print(message)
        #client.send_message('me', 'Hello, myself!')
        #print(client.download_profile_photo('me'))

        #@client.on(events.NewMessage(pattern='(?i).*Hello'))
        #async def handler(event):
        #   await event.reply('Hey!')

"""        
