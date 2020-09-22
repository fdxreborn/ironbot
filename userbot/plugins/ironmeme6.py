from telethon import events
import asyncio
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME, bot


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Ironbots"

@borg.on(admin_cmd(pattern="stupid$"))
@borg.on(sudo_cmd(pattern="stupid$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 14)
    event = await edit_or_reply(event, "brain")
    animation_chars = [
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠     <(^_^ <)    🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠   <(^_^ <)      🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠 <(^_^ <)        🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠<(^_^ <)         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           (> ^_^)>🗑",
        "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           <(^_^ <)🗑",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 14])

@borg.on(admin_cmd(pattern=r"call"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 18)
    await event.edit("Calling")
    animation_chars = [        
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "`Telegram: Hello This is Telegram HQ. Who is this?`",
            f"`Me: Yo this is` {DEFAULTUSER} ,`Please Connect me to my idiot bro,Ayush Durov`",
            "`User Authorised.`",
            "`Calling Pavel Durov`  `At +916969696969`",
            "`Private  Call Connected...`",
            "`Me: Hello Sir, Please Ban This Telegram Account.`",    
            "`Pavel: May I Know Who Is This?`",
            "`Me: Yo Brah, I Am`  ",
            "`Pavel: OMG!!! Long time no see, Wassup Brother...\nI'll Make Sure That Guy Account Will Get Blocked Within 24Hrs.`",
            "`Me: Thanks, See You Later Brah.`",
            "`Pavel: Please Don't Thank Brah, Telegram Is Our's. Just Gimme A Call When You Become Free.`",
            "`Me: Is There Any Issue/Emergency???`",
            "`Pavel: Yes Sur, There Is A Bug In Telegram v69.6.9.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.`",
            "`Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.`",
            "`Pavel: Sure Sur \nTC Bye Bye :)`",
            "`Private Call Disconnected.`"
        ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])


@borg.on(admin_cmd(pattern=r"isro"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 24)
    await event.edit("Connecting..")
    animation_chars = [
        
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n🚀⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛🚀⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛🚀⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🚀⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",    
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛🚀⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛🚀\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "🛸⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n🛸⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛🛸⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛🛸⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛🛸⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛",
            "⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛⬛\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸⬛🚶‍♂️\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n👽⬛⬛🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛👽⬛🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
            "⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛⬛⬛⬛⬛\n⬛⬛👽🛸🚶‍♂️⬛\n⬜⬜⬜⬜⬜⬜",
            "__Signal Lost....__"

 ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 24])


@borg.on(admin_cmd(pattern=r"hand"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 13)
  #  input_str = event.pattern_match.group(1)
  #  if input_str == 'hand':
    #    await event.edit(input_str)
    animation_chars = [
         '👈',
         '👉',
         '☝️',
         '👆',
         '🖕',
         '👇',
         '✌️',
         '🤞',
         '🖖',
         '🤘',
         '🤙',
         '🖐️',
         '👌'
     ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[(i % 13)])

@borg.on(admin_cmd(pattern=r"anim"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 9)
  #  input_str = event.pattern_match.group(1)
  #  if input_str == 'anim':
   #     await event.edit(input_str)
    animation_chars = [
         '😁',
         '😧',
         '😡',
         '😢',
         '😁',
         '😧',
         '😡',
         '😢',
         '__**...Eaaa....**__'
     ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[(i % 9)])

@borg.on(admin_cmd(pattern=r"fnl"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 6)
 #   input_str = event.pattern_match.group(1)
 #   if input_str == 'fnl':
 #       await event.edit(input_str)
    animation_chars = [
         '😁🏿',
         '😁🏾',
         '😁🏽',
         '😁🏼',
         '\u200e😁',
         '**End...**']
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[(i % 6)])

import os

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY, bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.kamui(:? |$)([1-8])?")
async def _(fry):
    await fry.edit("`Sending information...`")
    level = fry.pattern_match.group(2)
    if fry.fwd_from:
        return
    if not fry.reply_to_msg_id:
        await fry.edit("`Reply to any user message photo...`")
        return
    reply_message = await fry.get_reply_message()
    if not reply_message.media:
        await fry.edit("`No image found to fry...`")
        return
    if reply_message.sender.bot:
        await fry.edit("`Reply to actual user...`")
        return
    chat = "@image_deepfrybot"
    message_id_to_reply = fry.message.reply_to_msg_id
    async with fry.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(reply_message)
            if level:
                m = f"/deepfry {level}"
                msg_level = await conv.send_message(m, reply_to=msg.id)
                r = await conv.get_response()
            response = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await fry.reply("`Please unblock` @image_deepfrybot`...`")
            return
        if response.text.startswith("Forward"):
            await fry.edit("`Please disable your forward privacy setting...`")
        else:
            downloaded_file_name = await fry.client.download_media(
                response.media, TEMP_DOWNLOAD_DIRECTORY
            )
            await fry.client.send_file(
                fry.chat_id,
                downloaded_file_name,
                force_document=False,
                reply_to=message_id_to_reply,
            )
            """ - cleanup chat after completed - """
            try:
                msg_level
            except NameError:
                await fry.client.delete_messages(conv.chat_id, [msg.id, response.id])
            else:
                await fry.client.delete_messages(
                    conv.chat_id, [msg.id, response.id, r.id, msg_level.id]
                )
    await fry.delete()
    return os.remove(downloaded_file_name)


CMD_HELP.update(
    {
        "deepfry": ">`.kamui` or >`.kamui [level(1-8)]`"
        "\nUsage: deepfry image/sticker from the reply."
        "\n@image_deepfrybot"
    }
)

@borg.on(admin_cmd(pattern=r"anim"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 9)
  #  input_str = event.pattern_match.group(1)
  #  if input_str == 'anim':
   #     await event.edit(input_str)
    animation_chars = [
         '😁',
         '😧',
         '😡',
         '😢',
         '😁',
         '😧',
         '😡',
         '😢',
         '__**...Eaaa....**__'
     ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[(i % 9)])

@borg.on(admin_cmd(pattern=r"anjay"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = .1
    animation_ttl = range(0, 14)
 #   input_str = event.pattern_match.group(1)
 #   if input_str == 'fnl':
 #       await event.edit(input_str)
    animation_chars = [
         'A',
         'En',
         'Je',
         'A',
         'Ye',
         'A',
         'A En',
         'A En Je',
         'A En Je A',
         'A En Je A Ye',
         'Aaaa'
         'Aaaa aaaa',
         'Aaaa aaaanjaayy',
         '**A N J A Y**']
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[(i % 14)])

@borg.on(admin_cmd(pattern=r"theart$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 54)
    animation_chars = [
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])

@borg.on(admin_cmd(pattern=f"monkey$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 6)
    animation_chars = ["🐵", "🙉", "🙈", "🙊", "🖕‎🐵🖕", "**Good to See you friend....**"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])
