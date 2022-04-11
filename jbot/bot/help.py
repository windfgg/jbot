from telethon import events
from .. import jdbot, chat_id
from .help_info import help_info

@jdbot.on(events.NewMessage(from_users=chat_id, pattern='^/help'))
async def bot_help(event):
    '''接收/help命令后执行程序'''
    await jdbot.send_message(chat_id, help_info)
