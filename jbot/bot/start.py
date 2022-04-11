from telethon import events
from .. import jdbot, chat_id,ch_name


@jdbot.on(events.NewMessage(from_users=chat_id, pattern='/start'))
async def bot_start(event):
    '''接收/start命令后执行程序'''
    msg = '''
/help 获取命令
/start 获取明显详细说明
/rebot 重启BOT
/ver 获取更新日志以及版本号
/update 更新BOT
/cx 查询现在执行的任务列表
    
/cron 定时任务管理
/addcron 增加定时任务 例: `/addcron 0 0 * * * xxx.js`
/env 环境变量管理
/getfile 获取容器根目录下的文件
/down url 下载文件
/edit 从目录选择文件并编辑 需要将编辑好信息全部发给BOT
/log 查看脚本执行日志
/bean 获取指定账号收支 例：`/bean 1`
/chart 获取指定账号收支变化 例：`/chart 1`
    
/s 获取快捷命令列表
/setshort 添加快捷命令列表
/clearshort 删除快捷输入按钮。

/set 修改设置
/setname 设置命令别名
    
/snode 选择脚本后台执行
/node 执行JS脚本 例: `/node xxxxx.js` (如执行非scripts目录js，需输入绝对路径执行。node命令会等待脚本执行完，期间不能使用BOT，建议使用snode命令)
/cmd 执行命令，例：`/cmd python3 /python/bot.py` 不建议使用BOT使用并发 可能产生不明原因的崩溃。 
    
直接发送文件至BOT 会让您选择保存到目标文件夹，支持保存并运行。'''
    await jdbot.send_message(chat_id, msg)

if ch_name:
    jdbot.add_event_handler(bot_start,events.NewMessage(from_users=chat_id, pattern='开始'))
