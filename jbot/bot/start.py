from telethon import events
from .. import jdbot, chat_id,ch_name
from .start_info import start_info

@jdbot.on(events.NewMessage(from_users=chat_id, pattern='/start'))
async def bot_start(event):
    '''接收/start命令后执行程序'''
    await jdbot.send_message(chat_id, start_info)

if ch_name:
    jdbot.add_event_handler(bot_start,events.NewMessage(from_users=chat_id, pattern='开始'))
