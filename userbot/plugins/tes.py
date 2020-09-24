from asyncio.exceptions import TimeoutError
import datetime
import os
import shutil
import time
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.utils import admin_cmd

@borg.on(admin_cmd(pattern=("hc ?(.*)")))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    chat = "@AsalAja777_bot"
    message_id_to_reply = event.message.reply_to_msg_id
    await event.edit("```Hemmm.....```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @sangmatainfo_bot and try again```")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "The user have enabled privacy settings you cant get name history"
            )
        else:
            await event.edit(f"`{response.message.message}`")

@borg.on(admin_cmd(pattern="snif ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    reply_message = await event.get_reply_message()
    reply_to_id = event.message
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    chat = "@AsalAja777_bot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=461843263))
              await event.client.send_message(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("Unblock @vixtbot")
              return
          if response.text.startswith("I can't find that"):
             await event.edit("sorry i can't find it")
          else: 
             await event.delete()
             await borg.send_file(event.chat_id, response.message, reply_to=reply_to_id)


