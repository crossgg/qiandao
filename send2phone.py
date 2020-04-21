#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
# bark 推送
barklink = "https://bark.test.com/bark_key"
# server酱key 
skey = "SCUxxxxxxxxxxxxx"
def send2bark(title, content):
    try:
        msg = "{0}/推送标题/{1}/{2}".format(barklink, title, content)
        link = msg
        res = requests.get(link,verify=False)
    except Exception as e:
        print('Reason:', e)
        return
    return
    
def send2s(title, content):
    try:
        link = "https://sc.ftqq.com/{0}.send".format(skey)
        d = {'text': title, 'desp': content}
        res = requests.post(link, data=d , verify=False)
    except Exception as e:
        print('Reason:', e)
        return
    return
