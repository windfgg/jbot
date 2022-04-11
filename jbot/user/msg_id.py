from .login import user
from telethon import events
import time

@user.on(events.NewMessage(pattern=r'^id$', outgoing=True))
async def check_id(event):
    message = await event.get_reply_message()
    text = f"此消息ID：`{str(event.message.id)}`\n\n"
    text += f"**群组信息**\nid:`{str(event.chat_id)}\n`"
    msg_from = event.chat if event.chat else (await event.get_chat())
    if event.is_group or event.is_channel:
        text += f"群组名称：`{msg_from.title}`\n"
        try:
            if msg_from.username:
                text += f"群组用户名：`@{msg_from.username}`\n"
        except AttributeError:
            return
    if message:
        text += f"\n**查询的消息**：\n消息id：`{str(message.id)}`\n用户id：`{str(message.sender_id)}`"
        try:
            if message.sender.bot:
                text += f"\n机器人：`是`"
            if message.sender.last_name:
                text += f"\n姓：`{message.sender.last_name}`"
            try:
                text += f"\n名：`{message.sender.first_name}`"
            except TypeError:
                pass
            if message.sender.username:
                text += f"\n用户名：@{message.sender.username}"
        except AttributeError:
            pass
        await event.edit(text)
    else:
        await event.delete()


@user.on(events.NewMessage(pattern=r'^del[ 0-9]*$', outgoing=True))
async def selfprune(event):
    try:
        num = event.raw_text.split(' ')
        if isinstance(num, list) and len(num) == 2:
            count = int(num[-1])
        else:
            count = 1
        await event.delete()
        count_buffer = 0
        async for message in user.iter_messages(event.chat_id, from_user="me"):
            if count_buffer == count:
                break
            await message.delete()
            count_buffer += 1
        notification = await user.send_message(event.chat_id, f'已删除{count_buffer}/{count}')
        time.sleep(.5)
        await notification.delete()
    except Exception as e:
        await user.send_message(event.chat_id, str(e))
