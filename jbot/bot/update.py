from telethon import events
from .. import jdbot, chat_id, CONFIG_DIR
from .utils import cmd
from .update_log import version, botlog
import requests

@jdbot.on(events.NewMessage(from_users=chat_id, pattern='/update'))
async def bot_up(event):
    try:
        msg = await jdbot.send_message(chat_id, '开始更新程序 请稍候...')
        res = requests.get(
            'https://ghproxy.com/https://raw.githubusercontent.com/WindFgg/jbot/main/config/bot.sh').text
        with open(f'{CONFIG_DIR}/bot.sh', 'w+', encoding='utf-8') as f:
            f.write(res)
        await cmd(f'bash {CONFIG_DIR}/bot.sh')
        await jdbot.delete_messages(chat_id, msg)
    except Exception as e:
        await jdbot.send_message(chat_id, str(e))


@jdbot.on(events.NewMessage(from_users=chat_id, pattern=r'^/ver$', incoming=True))
async def bot_ver(event):
    await jdbot.send_message(chat_id, f'当前版本:`{version}`\n{botlog}')
