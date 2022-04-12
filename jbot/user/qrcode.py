import qrcode
from telethon import events
from .login import user
from .. import QR_IMG_FILE

def creat_qr(text):
    '''实例化QRCode生成qr对象'''
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.clear()
    # 传入数据
    qr.add_data(text)
    qr.make(fit=True)
    # 生成二维码
    img = qr.make_image()
    # 保存二维码
    img.save(QR_IMG_FILE)

@user.on(events.NewMessage(pattern=r'^qrcode [\s\S]*$', outgoing=True))
async def user_login(event):
    try:
        num = event.raw_text.split(' ')
        if isinstance(num, list) and len(num) == 2:
            data = int(num[-1])
            creat_qr(data)
            await user.send_message(event.chat_id, '',file=QR_IMG_FILE)
    except Exception as e:
        await user.send_message(event.chat_id,'二维码生成失败\n'+str(e))