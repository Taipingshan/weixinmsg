from wxauto import  WeChat

wx = WeChat()

msgs = wx.GetAllMessage()

for msg in msgs:
    if msg.type == 'sys':
        print(f'[系统消息]{msg.content}')
    elif msg.type ==  'friend':
        sender = msg.sender 
        print(f'{sender.rjust(20)}:{msg.content}')
    elif msg.type ==  'self':
        sender = msg.sender 
        print(f'{sender.rjust(20)}:{msg.content}')
    elif msg.type ==  'time':
        sender = msg.sender 
        print(f'\n[时间消息]{msg.time}')
    elif msg.type ==  'recall':
        sender = msg.sender 
        print(f'\n[撤回消息]:{msg.content}')