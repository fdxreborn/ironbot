from asyncio.exceptions import TimeoutError
import datetime
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
    reply_message = await event.get_reply_message() 
    chat = "@AsalAja777_bot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("``````")
       return
    await event.edit("```Making```")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1178524273))
              await bot.forward_messages(chat, reply_message)
              response = await response 
              res = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=752979930)
              )
              r = await res
          except YouBlockedUserError: 
              await event.reply("``````")
              return
          else: 
             await event.edit(f"{response.message.message}")
             await bot.forward_messages(event.chat_id, response.message)
             await bot.forward_messages(event.chat_id, response.message)
             await event.client.delete_messages(conv.chat_id, [msg.id, r.id, respond.id])
             await event.delete()
