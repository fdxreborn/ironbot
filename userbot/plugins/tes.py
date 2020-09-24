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

@register(outgoing=True, pattern=r"^\.hc (?:(now)|(.*) - (.*))")
async def _(event):
    if event.fwd_from:
        return
    chat = "@hcdecryptor_bot"
    try:
        await event.edit("`Getting Your Music`")
        async with bot.conversation(chat) as conv:
            await asyncio.sleep(2)
            await event.edit("`Downloading...`")
            try:
                response = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=1025667425)
                )
                msg = await bot.send_message(chat)
                respond = await response
                res = conv.wait_event(
                    events.NewMessage(incoming=True, from_users=1025667425)
                )
                r = await res
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.reply("`Unblock `@SpotifyMusicDownloaderBot` and retry`")
                return
            await bot.forward_messages(event.chat_id, respond.message)
        await event.client.delete_messages(conv.chat_id, [msg.id, r.id, respond.id])
        await event.delete()
    except TimeoutError:
        return await event.edit(
            "`Error: `@SpotifyMusicDownloaderBot` is not responding or Song not found!.`"
        )
