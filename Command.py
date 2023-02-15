from TelegramApi import *

async def startbot(update: Update, bot):
    await Reply(update, "hi, " + GetUserName(update))

async def getSticker(update: Update, bot):
    await Reply(update, "get sticker")