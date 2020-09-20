import asyncio, io, os, random, re, textwrap
from random import randint, uniform
from glitch_this import ImageGlitcher
from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps
from telethon import events, functions, types
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeFilename
from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY, bot
from userbot.events import register
THUMB_IMAGE_PATH = './thumb_image.jpg'

@register(outgoing=True, pattern='^\\.mmf(?: |$)(.*)')
async def mim(event):
    if event.fwd_from:
        return
    else:
        if not event.reply_to_msg_id:
            await event.edit("`Syntax: reply to an image with .mmf` 'text on top' ; 'text on bottom' ")
            return
        reply_message = await event.get_reply_message()
        await event.edit('```reply to a image/sticker/gif```')
        return
    reply_message.sender
    await bot.download_file(reply_message.media)
    if reply_message.sender.bot:
        await event.edit('```Reply to actual users message.```')
        return
    await event.edit('```Transfiguration Time! Mwahaha Memifying this image! (」ﾟﾛﾟ)｣ ```')
    await asyncio.sleep(5)
    text = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        file_name = 'meme.jpg'
        reply_message = await event.get_reply_message()
        to_download_directory = TEMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await bot.download_media(reply_message, downloaded_file_name)
        dls_loc = downloaded_file_name
    webp_file = await draw_meme_text(dls_loc, text)
    await event.client.send_file((event.chat_id),
      webp_file, reply_to=(event.reply_to_msg_id))
    await event.delete()
    os.remove(webp_file)


async def draw_meme_text(image_path, text):
    img = Image.open(image_path)
    os.remove(image_path)
    i_width, i_height = img.size
    m_font = ImageFont.truetype('fontx/FontRemix.ttf', int(0.13013698630136986 * i_width))
    if ';' in text:
        upper_text, lower_text = text.split(';')
    else:
        upper_text = text
        lower_text = ''
    draw = ImageDraw.Draw(img)
    current_h, pad = (10, 5)
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=18):
            u_width, u_height = draw.textsize(u_text, font=m_font)
            draw.text(xy=(
             (i_width - u_width) / 2 - 1, int(current_h / 730 * i_width)),
              text=u_text,
              font=m_font,
              fill=(0, 0, 0))
            draw.text(xy=(
             (i_width - u_width) / 2 + 1, int(current_h / 730 * i_width)),
              text=u_text,
              font=m_font,
              fill=(0, 0, 0))
            draw.text(xy=(
             (i_width - u_width) / 2, int(current_h / 730 * i_width) - 1),
              text=u_text,
              font=m_font,
              fill=(0, 0, 0))
            draw.text(xy=(
             (i_width - u_width) / 2, int(current_h / 730 * i_width) + 1),
              text=u_text,
              font=m_font,
              fill=(0, 0, 0))
            draw.text(xy=(
             (i_width - u_width) / 2, int(current_h / 730 * i_width)),
              text=u_text,
              font=m_font,
              fill=(255, 255, 255))
            current_h += u_height + pad

    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=18):
            u_width, u_height = draw.textsize(l_text, font=m_font)
            draw.text(xy=(
             (i_width - u_width) / 2 - 1,
             i_height - u_height - int(0.0410958904109589 * i_width)),
              text=l_text,
              font=m_font,
              fill=(0, 0, 0))
            draw.text(xy=(
             (i_width - u_width) / 2 + 1,
             i_height - u_height - int(0.0410958904109589 * i_width)),
              text=l_text,
              font=m_font,
              fill=(0, 0, 0))
            draw.text(xy=(
             (i_width - u_width) / 2,
             i_height - u_height - int(0.0410958904109589 * i_width) - 1),
              text=l_text,
              font=m_font,
              fill=(0, 0, 0))
            draw.text(xy=(
             (i_width - u_width) / 2,
             i_height - u_height - int(0.0410958904109589 * i_width) + 1),
              text=l_text,
              font=m_font,
              fill=(0, 0, 0))
            draw.text(xy=(
             (i_width - u_width) / 2,
             i_height - u_height - int(0.0410958904109589 * i_width)),
              text=l_text,
              font=m_font,
              fill=(255, 255, 255))
            current_h += u_height + pad

    image_name = 'memify.webp'
    webp_file = os.path.join(TEMP_DOWNLOAD_DIRECTORY, image_name)
    img.save(webp_file, 'WebP')
    return webp_file


@register(outgoing=True, pattern='^\\.mmf2(?: |$)(.*)')
async def mim(event):
    if event.fwd_from:
        return
    else:
        if not event.reply_to_msg_id:
            await event.edit("`Syntax: reply to an image with .mmf` 'text on top' ; 'text on bottom' ")
            return
        reply_message = await event.get_reply_message()
        await (reply_message.media or event.edit('```reply to a image/sticker/gif```'))
        return
    reply_message.sender
    await bot.download_file(reply_message.media)
    if reply_message.sender.bot:
        await event.edit('```Reply to actual users message.```')
        return
    await event.edit('```Transfiguration Time! Mwahaha Memifying this image! (」ﾟﾛﾟ)｣ ```')
    await asyncio.sleep(5)
    text = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        file_name = 'meme.jpg'
        reply_message = await event.get_reply_message()
        to_download_directory = TEMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await bot.download_media(reply_message, downloaded_file_name)
        dls_loc = downloaded_file_name
    webp_file = await draw_meme_text(dls_loc, text)
    await event.client.send_file((event.chat_id),
      webp_file, reply_to=(event.reply_to_msg_id))
    await event.delete()
    os.remove(webp_file)


async def draw_meme_text(image_path, text):
    img = Image.open(image_path)
    os.remove(image_path)
    i_width, i_height = img.size
    m_font = ImageFont.truetype('fontx/FontRemix2.ttf', int(0.13013698630136986 * i_width))
    if ';' in text:
        upper_text, lower_text = text.split(';')
    else:
        upper_text = text
        lower_text = ''
    draw = ImageDraw.Draw(img)
    current_h, pad = (10, 5)
    if upper_text:
        for u_text in textwrap.wrap(upper_text, width=18):
            u_width, u_height = draw.textsize(u_text, font=m_font)
            draw.text(xy=(
             (i_width - u_width) / 2 - 1, int(current_h / 730 * i_width)),
              text=u_text,
              font=m_font,
              fill=(0, 0, 0))
            draw.text(xy=(
             (i_width - u_width) / 2 + 1, int(current_h / 730 * i_width)),
              text=u_text,
              font=m_font,
              fill=(0, 0, 0))
            draw.text(xy=(
             (i_width - u_width) / 2, int(current_h / 730 * i_width) - 1),
              text=u_text,
              font=m_font,
              fill=(0, 0, 0))
            draw.text(xy=(
             (i_width - u_width) / 2, int(current_h / 730 * i_width) + 1),
              text=u_text,
              font=m_font,
              fill=(0, 0, 0))
            draw.text(xy=(
             (i_width - u_width) / 2, int(current_h / 730 * i_width)),
              text=u_text,
              font=m_font,
              fill=(255, 255, 255))
            current_h += u_height + pad

    if lower_text:
        for l_text in textwrap.wrap(lower_text, width=18):
            u_width, u_height = draw.textsize(l_text, font=m_font)
            draw.text(xy=(
             (i_width - u_width) / 2 - 1,
             i_height - u_height - int(0.0410958904109589 * i_width)),
              text=l_text,
              font=m_font,
              fill=(0, 0, 0))
            draw.text(xy=(
             (i_width - u_width) / 2 + 1,
             i_height - u_height - int(0.0410958904109589 * i_width)),
              text=l_text,
              font=m_font,
              fill=(0, 0, 0))
            draw.text(xy=(
             (i_width - u_width) / 2,
             i_height - u_height - int(0.0410958904109589 * i_width) - 1),
              text=l_text,
              font=m_font,
              fill=(0, 0, 0))
            draw.text(xy=(
             (i_width - u_width) / 2,
             i_height - u_height - int(0.0410958904109589 * i_width) + 1),
              text=l_text,
              font=m_font,
              fill=(0, 0, 0))
            draw.text(xy=(
             (i_width - u_width) / 2,
             i_height - u_height - int(0.0410958904109589 * i_width)),
              text=l_text,
              font=m_font,
              fill=(255, 255, 255))
            current_h += u_height + pad

    image_name = 'memify.webp'
    webp_file = os.path.join(TEMP_DOWNLOAD_DIRECTORY, image_name)
    img.save(webp_file, 'WebP')
    return webp_file


CMD_HELP.update({'memify': '`.mmf` texttop ; textbottom        \nUsage: Reply a sticker/image/gif and send with cmd.\n`.mmf2` texttop ; textbottom        \nUsage: Reply a sticker/image/gif and send with cmd.'})

