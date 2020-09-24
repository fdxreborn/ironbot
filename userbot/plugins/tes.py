from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP


@register(outgoing=True, pattern="^.hc(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Reply to any user message.`")
        return
    reply_message = await event.get_reply_message()
    # if not reply_message.text:
    # await event.edit("```reply to text message```")
    # return
    chat = "@AsalAja777_bot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("`Reply to actual users message.`")
        return
    await event.edit("`Hmm...`")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=1178524273))
            await bot.send_message("/start")
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("`Please unblock   and try again`")
            return
        if response.text.startswith("Forward"):
            await event.edit("`can you kindly disable your forward privacy settings for good?`")
        else:
            await event.edit(f"{response.message.message}")


CMD_HELP.update({
    "snif":
        ".snif \
          \nreply to files for view proxy or sni .\n"
})
