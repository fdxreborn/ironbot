from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP
import asyncio
import sys, time, io

#@register(outgoing=True, pattern="^.hc(?: |$)(.*)")
@register(outgoing=True, pattern=r"^\.(?:hc|sniff|bongkar)\s?(.)?")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Reply ke confignya lah.`")
        return
    reply_message = await event.get_reply_message()
    chat = "@Ahsydjwoahdywbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("`Reply to actual users message.`")
        return
    await event.edit("`Proses decrypt boss sabar...`")
    await asyncio.sleep(.2)
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1144339544))
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("`Unblock dulu`")
            return
        if response.text.startswith("Forward"):
            await event.edit("`?`")
        else: 
            await event.client.send_message(event.chat_id, response.message, reply_to=reply_message)
            await event.delete()
