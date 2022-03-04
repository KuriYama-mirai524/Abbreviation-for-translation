import time
import requests
import demjson
import simuse
import spider

with open('data.json', 'r') as f:
    data = demjson.decode(f.read())
    print(data)

# 连接bot
daisy = simuse.Get_Session(data, getsession=1)
if daisy == 1 or 0:
    print('获取会话失败，请检查config填写是否正确')
else:
    print('bot连接成功', daisy)
    print('开始监听')
while True:
    msg = simuse.Fetch_Message(data, session=daisy, deal=1)
    if msg == 0:
        pass
    else:
        group = msg[0]['group']
        msg = msg[0]['messagechain'][1]['text']
        if str(group) in str(data['group']):
            if '.' in msg:
                try:
                    key = str(msg).replace('.', '')
                    resp = spider.trans(msg=key)
                    word = resp[0]['trans']
                    post = {
                        "sessionKey": daisy,
                        "target": group,
                        "messageChain": [
                            {"type": "Plain", "text": '查询到这些意思:'+'\n'+str(word).replace("'", '').replace(',', '\n')}
                        ]
                    }
                    url = 'http://'+data['host']+'/sendGroupMessage'
                    requests.request('post', url=url, json=post)



                except Exception as e:
                    print('发生了一个错误')
                    print('错误类型', e.__class__.__name__)
                    print('错误详情', e)
                    print('如果自己无法解决，请去帖子联系懒逼作者')
            else:
                pass
        else:
            pass

    time.sleep(1)

