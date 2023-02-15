import os
from typing import List, Union

from telegram import ForceReply
from telegram import Update
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, Application, ExtBot
from dotenv import load_dotenv

load_dotenv()

app: Application = ApplicationBuilder().token(os.getenv("TELEGRAM_TOKEN")).build()
bot: ExtBot = app.bot
text_limit = 4000

# send message
async def Reply(update: Update, msg: Union[list, str], forceReply: bool = False) -> None:
    if type(msg) is list:
        for m in msg:
            await update.message.reply_text(m)
    else:
        if(forceReply):
            return await update.message.reply_text(msg, reply_markup = ForceReply(selective=True))
        else:
            return await update.message.reply_text(msg)
        
async def ReplyPhoto(update: Update, photolink: str) -> None:
    await update.message.reply_photo(photolink)

async def ReplyButton(update: Update, title: str, buttonText = List[List[str]], replyText = List[List[str]]):
    buttonList = buttonText
    for i in range(len(buttonList)):
        for j in range(len(buttonList[i])):
            buttonList[i][j] = InlineKeyboardButton(buttonText[i][j], callback_data = replyText[i][j]) 

    await update.message.reply_text(title, reply_markup = InlineKeyboardMarkup(buttonList))

async def ReplySticker(update: Update, file_id: str) -> None:
    await update.message.reply_sticker(file_id)
    
async def Send(chat_id: int, msg: str):
    return await bot.send_message(chat_id, msg)

# get information about message
def GetUserID(update: Update) -> int:
    return update.message.from_user.id

def GetGroupID(update: Update) -> int:
    return update.message.chat.id

def GetUserName(update: Update) -> str:
    return update.message.from_user.name

def GetText(update: Update) -> str:
    return update.message.text