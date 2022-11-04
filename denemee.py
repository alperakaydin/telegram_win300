
from telethon import TelegramClient, events
import datetime
api_id = 7145550
api_hash = "659da193100cfd421ce6aedf1ef6ea79"

client = TelegramClient('anon', api_id, api_hash)
# channel_id=1194185327
# user_id=1704449472 Efe gencelli
# selma 1194185327
# eren 987004745
# emre 1572434674
users = [1704449472, 817741597, 1321541491, 1194185327, 987004745, 1274728384, 1567439376, 878428601 ]
id_name = {
    1704449472: "Efe Gencelli",
    1194185327: "Selma",
    987004745: "Eren",
    1567439376: "Elif",
    1321541491: "Emre"
}
def varmi(id_list,id):
    for user in id_list:
        if user == id:
            return True
    return False

def isimbul(id):
    try:
        return id_name[id]
    except:
        return "NoName"


@client.on(events.NewMessage(chats=1194185327))  # (from_users=users)  chats=1194185327
async def main(event):
    await client.start()
    print("--------")
    f = open("datalog.txt", "a")
    sender_name = ""
    if hasattr(event.message.from_id, "user_id"):
        sender_name = isimbul(event.message.from_id.user_id)
        print(f"{event.message.from_id.user_id} ___ {event.message.date}")
        f.write(f"{event.message.from_id.user_id} ___ {event.message.date}\n")
        f.close()

    if (hasattr(event.message.from_id, "user_id") and varmi(users,event.message.from_id.user_id)) \
            or not hasattr(event.message.from_id, "user_id"):
        message_from_user_text = event.message.raw_text

        if event.message.photo: # PHOTO
            path = await event.message.download_media()
            path = f"./{path}"
            print('File saved to', path)
            print(path)

            if event.message.is_reply: # ALINTI
                reply_message = await event.message.get_reply_message()

                if reply_message.message and message_from_user_text:
                    await client.send_message('Sub-Win300', f'__{reply_message.message}__\n#{sender_name} {message_from_user_text}'
                                              , file=path)
                    # await client.send_file('Sub-Win300', path)
                    print(f"ALINTI         :{reply_message.message}")
                    print(f"ALINTI USER ID :{reply_message.from_id}")
                    print(f"USER ID        :{event.from_id}")
                    print(f"MESSAGE        :{message_from_user_text}")
                elif reply_message.message:
                    await client.send_message('Sub-Win300', f'__{reply_message.message}__', file=path)
                elif message_from_user_text:
                    await client.send_message('Sub-Win300', f'#{sender_name} {message_from_user_text}', file=path)
                else:
                    await client.send_message('Sub-Win300', f'#{sender_name} ', file=path)

            else: # ALINTI YOK
                if message_from_user_text:
                    await client.send_message('Sub-Win300', f'#{sender_name} {message_from_user_text}', file=path)
                    print(f"USER ID :{event.from_id}")
                    print(f"MESSAGE :{message_from_user_text}")
                else:
                    await client.send_message('Sub-Win300', f'#{sender_name} ', file=path)
        else:
            if event.message.is_reply:  # ALINTI
                reply_message = await event.message.get_reply_message()

                if reply_message.message and message_from_user_text:
                    await client.send_message('Sub-Win300', f'__{reply_message.message}__\n#{sender_name} {message_from_user_text}')
                    # await client.send_file('Sub-Win300', path)
                    print(f"ALINTI         :{reply_message.message}")
                    print(f"ALINTI USER ID :{reply_message.from_id}")
                    print(f"USER ID        :{event.from_id}")
                    print(f"MESSAGE        :{message_from_user_text}")
                elif reply_message.message:
                    await client.send_message('Sub-Win300', f'__{reply_message.message}__')
                elif message_from_user_text:
                    await client.send_message('Sub-Win300', f'#{sender_name} {message_from_user_text}')

            else:  # ALINTI YOK
                if message_from_user_text:
                    chat = await event.get_chat()
                    #print(chat.stringify())
                    await client.send_message('Sub-Win300', f'#{sender_name} {message_from_user_text}')
                    print(f"USER ID :{event.from_id}")
                    print(f"MESSAGE :{message_from_user_text}")

with client:
    client.run_until_disconnected()


if __name__ == "__main__":
    main()