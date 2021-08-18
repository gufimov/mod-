# Ultroid - UserBot
# Copyright (C) 2021 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

"""
✘ Commands Available -

• `{i}instadl <Instagram Url>`
  `Download Instagram Media...`

"""

import os

import instagrapi

from . import *

CLIENT = []


def create_client(username, password):
    settings = None
    if udB.get("INSTA_SET"):
        settings = eval(udB.get("INSTA_SET"))
    try:
        return CLIENT[0]
    except IndexError:
        cl = instagrapi.Client(settings)
        cl.login(username, password)
        CLIENT.append(cl)
        udB.set("INSTA_SET", str(cl.get_settings()))
        return cl


@ultroid_cmd(pattern="instadl ?(.*)")
async def insta_dl(e):
    match = e.pattern_match.group(1)
    replied = await e.get_reply_message()
    tt = await eor(e, "`Processing...`")
    if match:
        text = match
    elif e.is_reply and "insta" in replied.message:
        text = replied.message
    else:
        return await eor(tt, "Provide a Link to Download...")
    un = udB.get("INSTA_USERNAME")
    up = udB.get("INSTA_PASSWORD")
    if un and up:
        try:
            CL = create_client(un, up)
            media = CL.video_download(CL.media_pk_from_url(text))
            await e.reply(f"**Uploaded Successfully\nLink :** {text}", file=media)
            await tt.delete()
            os.remove(media)
            return
        except Exception as B:
            return await eor(tt, str(B))
    if isinstance(e.media, types.MessageMediaWebPage) and isinstance(
        e.media.webpage, types.WebPage
    ):
        photo = e.media.webpage.photo or e.media.webpage.document
        if not photo:
            return await eor(
                tt,
                "Please Fill `INSTA_USERNAME` and `INSTA_PASSWORD` to Use This Comamand!",
            )
        await tt.delete()
        return await e.reply(
            f"**Link:{text}\n\nIf This Wasnt Excepted Result, Please Fill `INSTA_USERNAME` and `INSTA_PASSWORD`...",
            file=photo,
        )
    await eor(tt, "Please Fill Instagram Credential to Use this Command...")


@ultroid_cmd(pattern="instadata")
async def soon_(e):
    un = udB.get("INSTA_USERNAME")
    up = udB.get("INSTA_PASSWORD")

    e.pattern_match.group(1)
    try:
        create_client(un, up)
    except Exception as g:
        return await eor(e, g)
    return
