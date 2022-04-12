from .. import BOT_SET
from .login import user


if BOT_SET['开启user'].lower() == 'true':
    user.start()
    user.send_message('1478107852', 'user启动成功')
    