from wxauto import WeChat
wx = WeChat()
msgs = wx.GetAllMessage()

for msg in msgs:
    if msg.type =='sys':
        print(f'[????]{msg.content}')
    elif msg.type == 'frined':
        sender = msg.sender
        print(f'{sender.rjust(20)}:{msg.content}')
    elif msg.type == 'self':
        sender = msg.sender
        print(f'{sender.rjust(20)}:{msg.content}')
    elif msg.type == 'time':
        sender = msg.sender
        print(f'{sender.rjust(20)}:{msg.content}')
    elif msg.type == 'recall':
        sender = msg.sender
        print(f'{sender.rjust(20)}:{msg.content}')

