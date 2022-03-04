import requests


def trans(msg):
    data = {
        'text': msg
    }
    resp = requests.post(url='https://lab.magiconch.com/api/nbnhhsh/guess', json=data)
    return resp.json()


if __name__ == '__main__':
    trans('yysy')
