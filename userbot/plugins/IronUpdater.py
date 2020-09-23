#by : scr
import asyncio
import sys, time, io
from os import environ, execle, path, remove

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from telethon.tl.functions.users import GetFullUserRequest

from math import ceil
import json
import random
import re
from telethon import events, errors, custom, functions, __version__
from userbot import CMD_LIST
import os
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd
import platform
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from datetime import datetime
from os import remove
from platform import python_version, uname
from shutil import which
from userbot.uniborgConfig import Config
import psutil
from telethon import __version__, version

from userbot import CMD_HELP, StartTime, bot, ironversion
from userbot.events import register


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time



from userbot import (
    CMD_HELP,
    HEROKU_API_KEY,
    HEROKU_APP_NAME,
    UPSTREAM_REPO_URL,
    UPSTREAM_REPO_BRANCH,
)

from userbot.events import register

requirements_path = path.join(
    path.dirname(path.dirname(path.dirname(__file__))), "requirements.txt"
)


async def gen_chlog(repo, diff):
    ch_log = ""
    d_form = "%d/%m/%y **%H:%M**"
    for c in repo.iter_commits(diff):
        ch_log += (
            f"•[{c.committed_datetime.strftime(d_form)}]:\n"
            f"{c.summary} <{c.author}>\n"
        )
    return ch_log

async def print_changelogs(event, ac_br, changelog):
    changelog_str = (
        f"**Ada UPDATE Baru [{ac_br}]:\n\nPerubahan info :**\n`{changelog}`"
    )
    if len(changelog_str) > 4096:
        await event.edit("`Changelog is too big, view the file to see it.`")
        file = open("output.txt", "w+")
        file.write(changelog_str)
        file.close()
        await event.client.send_file(
            event.chat_id, "output.txt", reply_to=event.id,
        )
        remove("output.txt")
    else:
        await event.client.send_message(
            event.chat_id, changelog_str, reply_to=event.id,
        )
    return True


async def update_requirements():
    reqs = str(requirements_path)
    try:
        process = await asyncio.create_subprocess_shell(
            " ".join([sys.executable, "-m", "pip", "install", "-r", reqs]),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


async def deploy(event, repo, ups_rem, ac_br, txt):
    if HEROKU_API_KEY is not None:
        import heroku3

        heroku = heroku3.from_key(HEROKU_API_KEY)
        heroku_app = None
        heroku_applications = heroku.apps()
        if HEROKU_APP_NAME is None:
            await event.edit(
                "`[HEROKU]`\n`Pliss benerin settinganya` **HEROKU_APP_NAME** `variable"
                " Agar bisa mendeploy ironbot...`"
            )
            repo.__del__()
            return
        for app in heroku_applications:
            if app.name == HEROKU_APP_NAME:
                heroku_app = app
                break
        if heroku_app is None:
            await event.edit(
                f"{txt}\n" "`Gagal Heroku credentials untuk deploy ironbot dyno.`"
            )
            return repo.__del__()
        await event.edit(
            "`[IRONBOT]`" "\n⏳` Deploy proses, coba check .ping setelah 5 min... `⏳"
        )
        ups_rem.fetch(ac_br)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", "https://api:" + HEROKU_API_KEY + "@"
        )
        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)
        try:
            remote.push(refspec="HEAD:refs/heads/master", force=True)
        except Exception as error:
            await event.edit(f"{txt}\n`Here is the error log:\n{error}`")
            return repo.__del__()
        build = app.builds(order_by="created_at", sort="desc")[0]
        if build.status == "failed":
            await event.edit(
                "`Build gagal!\n" "gagal atau mungkin ada error...`"
            )
            await asyncio.sleep(5)
            return await event.delete()
        else:
            await event.edit("`Deploy berhasil!\n" "Lagi restart bentar, tunggu ya...`")
    else:
        await event.edit(
            "`[HEROKU]`\n" "`Please set up`  **HEROKU_API_KEY**  `variable...`"
        )
    return


async def update(event, repo, ups_rem, ac_br):
    try:
        ups_rem.pull(ac_br)
    except GitCommandError:
        repo.git.reset("--hard", "FETCH_HEAD")
    await update_requirements()
    await event.edit("🚧`-B-`🚧")
    await event.edit("🚧`-B E-`🚧")
    await event.edit("🚧`-B E R-`🚧")
    await event.edit("🚧`-B E R H-`🚧")
    await event.edit("🚧`-B E R H A-`🚧")
    await event.edit("🚧`-B E R H A S-`🚧")
    await event.edit("🚧`-B E R H A S I-`🚧")
    await event.edit("🚧`-B E R H A S I L-`🚧")
    await event.edit("🚧`-B E R H A S I L  U-`🚧")
    await event.edit("🚧`-B E R H A S I L  U P-`🚧")
    await event.edit("🚧`-B E R H A S I L  U P D-`🚧")
    await event.edit("🚧`-B E R H A S I L  U P D A-`🚧")
    await event.edit("🚧`-B E R H A S I L  U P D A T-`🚧")
    await event.edit("🚧`-B E R H A S I L  U P D A T E-`🚧")
    await asyncio.sleep(2)
    await event.edit("`Bot akan restart tunggu beberapa detik`")
    await asyncio.sleep(1)
    await event.delete()
    # Spin a new instance of bot
    args = [sys.executable, "-m", "userbot"]
    execle(sys.executable, *args, environ)
    return


@register(outgoing=True, pattern=r"^\.update( now| deploy|$)")
async def upstream(event):
    "Untuk .update command, mengecek apakah ada update"
    await event.edit("`⚙️Memgambil informasi....`")
    conf = event.pattern_match.group(1).strip()
    off_repo = UPSTREAM_REPO_URL
    force_update = False
    try:
        txt = "`Oops.. Updater tidak bisa berjalan "
        txt += "beberapa masalah ditemukan`\n\n**LOGTRACE:**\n"
        repo = Repo()
    except NoSuchPathError as error:
        await event.edit(f"{txt}\n`directory {error} is not found`")
        return repo.__del__()
    except GitCommandError as error:
        await event.edit(f"{txt}\n`Early failure! {error}`")
        return repo.__del__()
    except InvalidGitRepositoryError as error:
        if conf is None:
            return await event.edit(
                f"`sayangnya, direktori {error} "
                "tampaknya bukan repositori git.\n"
                "Tapi kita bisa memperbaikinya dengan memperbarui paksa menggunakan ironbot "
                ".update now.`"
            )
        repo = Repo.init()
        origin = repo.create_remote("upstream", off_repo)
        origin.fetch()
        force_update = True
        repo.create_head("master", origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)

    ac_br = repo.active_branch.name
    if ac_br != UPSTREAM_REPO_BRANCH:
        await event.edit(
            "**[UPDATER]:**\n"
            f"`Sepertinya Anda menggunakan branch kustom Anda sendiri ({ac_br}). "
            "Dalam hal ini, Updater tidak dapat mengidentifikasi"
            "Branch mana yang akan digabungkan."
            "Silakan periksa ke branch asli`"
        )
        return repo.__del__()
    try:
        repo.create_remote("upstream", off_repo)
    except BaseException:
        pass

    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ac_br)

    changelog = await gen_chlog(repo, f"HEAD..upstream/{ac_br}")
    """ - Special case for deploy - """
    if conf == "deploy":
        await event.edit("`⚡Deploying ironbot, check .alive jika sudah 5-10min...`")
        await deploy(event, repo, ups_rem, ac_br, txt)
        return

    if changelog == "" and not force_update:
        await event.edit(
            "\n`➰ Ironbot Info ➰`\n\n🔺 `Versi   :`  **terbaru** 🔺\n🔺 `Base on :`  "
            f"**{UPSTREAM_REPO_BRANCH}** 🔺\n"
        )
        await asyncio.sleep(3)
        await event.delete()
        return repo.__del__()

    if conf == "" and not force_update:
      #  await print_changelogs(event, ac_br, changelog)
       # await event.delete()
        await event.edit(f"** ADA UPDATE BOSS **\n`Base on :` [{ac_br}]\n\n**PERUBAHAN INFO:**\n{changelog}\n`Ketik : .update now/.update deploy untuk update ironbot.`")
        await asyncio.sleep(3)
        await event.delete()
       # await event.respond("`Ketik : .update now/.update deploy untuk update ironbot.`")

    if force_update:
        await event.edit(
            "`Force sync untuk ironbot,\ntunggu ya...`🛠️"
        )
        await update(event, repo, ups_rem, ac_br)
        await asyncio.sleep(4)
        await event.delete()
    if conf == "now":
        await asyncio.sleep(.1)
        await event.edit("`• Proses update ironbot\n• Sabar ya.🛠️`")
        await asyncio.sleep(.1)
        await event.edit("`• Proses update ironbot\n• Sabar ya..🛠️`")
        await asyncio.sleep(.1)
        await event.edit("`• Proses update ironbot\n• Sabar ya...🛠️`")
        await asyncio.sleep(.1)
        await event.edit("`• Proses update ironbot\n• Sabar ya....🛠️`")
        await asyncio.sleep(.1)
        await event.edit("`• Proses update ironbot\n• Sabar ya.....🛠️`")
        await update(event, repo, ups_rem, ac_br)
    return


@register(outgoing=True, pattern=r"^\.repo$")
async def repo_is_here(wannasee):
    """ For .repo command, just returns the repo URL. """
    await wannasee.edit("`Ironbot repo klik `[Disini!](https://github.com/tesbot07/ironbot).")


@register(outgoing=True, pattern=r"^\.(?:alive|on)\s?(.)?")
async def _(alive):
    chat = await alive.get_chat()
    await alive.delete()
    uptime = await get_readable_time((time.time() - StartTime))
    IMG = Config.ALIVE_IMG
    if IMG is None:
        IMG = "https://drive.google.com/uc?id=1-Mnv3SDxJVc0BWAdasEoIlVBtO9PtbCZ&export=download"
    Alive_caption = (
         "╭━━━━━━| 𝙸𝚁𝙾𝙽𝙱𝙾𝚃 |━━━━━━╮\n"
        f"┣[•👤 `USER     :` {DEFAULTUSER}\n"
        f"┣▰▱▰▱▰▱▰▱▰▱▰▱▰▱\n"
        f"┣[•🤖 `Iron Ver : {ironversion} ➰`\n"
        f"┣[•🐍 `Python.  : v.{python_version()} ➰`\n"
        f"┣[•⚙️ `Telethon : v.{version.__version__} ➰`\n"
        f"┣[•💡 `Base on  : {UPSTREAM_REPO_BRANCH} ➰`\n"
        f"┣[•🕒 `Uptime.  : {uptime} ➰`\n"
        f"╰━━━━━━━━━━━━━━━━━━━━╯\n"
    )
    await borg.send_file(alive.chat_id, IMG,caption=Alive_caption)
    await alive.delete() 



CMD_HELP.update(
    {
        "update": ">`.update`"
        "\nUsage: Checks if the main userbot repository has any updates "
        "and shows a changelog if so."
        "\n\n>`.update now`"
        "\nUsage: Update your userbot, "
        "if there are any updates in your userbot repository."
        "\n\n>`.update deploy`"
        "\nUsage: Deploy your userbot"
        "\nThis will triggered deploy always, even no updates."
    }
)
