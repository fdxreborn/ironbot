from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP
import asyncio
import sys, time, io


@register(outgoing=True, pattern="^.hc(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Reply to any user message.`")
        return
    reply_message = await event.get_reply_message()
    chat = "@AsalAja777_bot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("`Reply to actual users message.`")
        return
    await event.edit("`Proses decrypt boss sabar...`")
    await asyncio.sleep(.5)
    await event.edit("`50%...`")
    await asyncio.sleep(.5)
    await event.edit("`70%...`")
    await asyncio.sleep(.5)
    await event.edit("`100%...`")
    await asyncio.sleep(.5)
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=835283956))
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("`Please unblock and try again`")
            return
        if response.text.startswith("Forward"):
            await event.edit("`can you kindly disable your forward privacy settings for good?`")
        else:
            if len(response) > 4096:
                    await event.edit("`Changelog is too big, view the file to see it.`")
                    file = open("output.txt", "w+")
                    file.write(response)
                    file.close()
                    await event.client.send_file(
                         event.chat_id, "output.txt", reply_to=event.id,
                   )
                   await event.delete()
                   await event.edit(f"```{response.message.message}```")
