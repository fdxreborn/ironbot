from telethon import events, functions
import asyncio, io, types
from uniborg.util import admin_cmd
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd
from userbot import CMD_HELP, bot
from subprocess import PIPE
from subprocess import run as runapp
from userbot.events import register, errors_handler
from asyncio.exceptions import TimeoutError

@register(outgoing=True, pattern=r"^\.decrypt(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Reply to any user message.`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.media:
        await event.edit("```reply to text message```")
        return
    chat = "@hcdecryptor_bot"
    await event.edit("`Processing`")
    try:
        async with bot.conversation(chat) as conv:
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=461843263)
                )
                await bot.forward_messages(chat, reply_message)
                response = await response
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.reply("`Please unblock try again`")
                return
            if response.text.startswith("Forward"):
                await event.edit(
                    "`Can you kindly disable your forward privacy settings for good?`"
                )
            else:
                await bot.forward_messages(event.chat_id, respond.message)
                await event.client.delete_messages(conv.chat_id, [msg.id, r.id, respond.id])
                await event.delete()
    except TimeoutError:
        return await event.edit("`Error: is not responding!.`")


