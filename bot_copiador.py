#!/usr/bin/env python3
from pyrogram import Client, enums
from pyrogram import filters
import sys
import traceback
from datetime import datetime


# ~~~~~~ CONFIG ~~~~~~~~ #
ACCOUNT = "user"

# Channel IDs...
channels_to_watch = [-1001867528704]
forward_channel = -1002084579318
# ~~~~~~~~~~~~~~~~~~~~~~ #

app = Client(ACCOUNT)
# app.start()

# chats = app.get_dialogs()
# num = 0
# ids = []
# for chat in chats:
#     try:
#         print(chat.chat.title + ' - ' + str(chat.chat.id))
#     except:
#         pass


@app.on_message(filters.chat("me") & filters.forwarded)
def my_handler(client, message):
    print(message)
    app.send_message("me", message.forward_from_chat.id)


@app.on_message(filters.chat(channels_to_watch) & ~filters.via_bot)
def my_handler(client, message):

    if message.media == enums.MessageMediaType.VIDEO:
        message.copy(chat_id=forward_channel, caption='')
    if message.media == enums.MessageMediaType.PHOTO:
        message.copy(chat_id=forward_channel, caption='')


app.run()
