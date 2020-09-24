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

#@register(outgoing=True, pattern="^.q(?: |$)(.*)")
@borg.on(admin_cmd(pattern=r"hc(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("``````")
       return
    link = event.pattern_match.group(1)
    chat = "@AsalAja777_bot"
    await event.edit("```Making```")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1178524273))
              await bot.forward_messages(chat, link)
              response = await response 
              res = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=1178524273)
              )
              r = await res
          except YouBlockedUserError: 
              await event.reply("``````")
              return
          else: 
             await bot.forward_messages(event.chat_id, respond.message)
             await event.client.delete_messages(conv.chat_id,
                                                [msg.id, r.id, respond.id])
             await event.delete()

#@register(outgoing=True, pattern="^.q(?: |$)(.*)")
@borg.on(admin_cmd(pattern=r"sniff(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    chat = "@AsalAja777_bot"
    await event.edit("```Sedang mengambil musik yang anda inginkan```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await event.edit("`Sedang Di Download, Stay disini aja`")
          try:
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=752979930))
              msg = await bot.send_message(chat, link)
              respond = await response
              res = conv.wait_event(events.NewMessage(incoming=True,from_users=752979930))
              r = await res
              """ - don't spam notif - """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await event.reply("```Tolong DiUnblock @SpotifyMusicDownloaderBot dan coba lagi```")
              return
          await bot.forward_messages(event.chat_id, respond.message)
    await event.client.delete_messages(conv.chat_id,
                                       [msg.id, r.id, respond.id])
    await event.delete()
