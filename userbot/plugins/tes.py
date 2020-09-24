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
            await borg.forward_messages(chat, reply_to=msg.id)
            response = await conv.get_response()
        except YouBlockedUserError:
            await event.reply("```Please unblock @sangmatainfo_bot and try again```")
            return
        if response.text.startswith("Forward"):
            await event.edit(
                "The user have enabled privacy settings you cant get name history"
            )
        else:
            await bot.forward_messages(event.chat_id, reply_to=message_id_to_reply)
            await event.client.delete_messages(conv.chat_id,
                                       [msg.id, r.id, respond.id])
