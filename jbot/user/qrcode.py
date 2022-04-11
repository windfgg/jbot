import asyncio,qrcode
from telethon import events

# def creat_qr(text):
#     '''实例化QRCode生成qr对象'''
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_H,
#         box_size=10,
#         border=4
#     )
#     qr.clear()
#     # 传入数据
#     qr.add_data(text)
#     qr.make(fit=True)
#     # 生成二维码
#     img = qr.make_image()
#     # 保存二维码
#     img.save(QR_IMG_FILE)

# @jdbot.on(events.NewMessage(from_users=chat_id,pattern=r'^qrcode []$'))
# async def user_login(event):
#     try:
#         user.connect()
#         qr_login = await user.qr_login()
#         creat_qr(qr_login.url)
#         await jdbot.send_message(chat_id,'请使用TG扫描二维码以开启USER',file=QR_IMG_FILE)
#         await jdbot.send_message(chat_id,qr_login.url)
#         await qr_login.wait(timeout=100)
#         await jdbot.send_message(chat_id,'恭喜您已登录成功,请修改 /set 将开启user 改为True 并重启机器人 /reboot')
#     except Exception as e:
#         await jdbot.send_message(chat_id,'登录失败\n'+str(e))