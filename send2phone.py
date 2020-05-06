#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import requests
import json
import os
import codecs
import io

class send2phone:
    def __init__(self, *args, **kwargs):
        hfile="./config/config.json"
        if (True == os.path.isfile(hfile)):
            hjson = json.loads(io.open(hfile, 'r', encoding='utf-8').read())
            self.barklink = hjson[u"bark链接"]
            self.skey = hjson[u"s酱key"]
            self.wj = hjson[u"腾讯问卷"]
        else:
            self.barklink = ""
            self.skey = ""
            self.wj = {
		                  "链接":"",
		                  "ID":"",
		                  "问题ID":"",
		                  "填空ID":""
	                  }
            
        self.base_headers={
            "Host": "wj.qq.com",
            "Connection": "keep-alive",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36",
            "Origin": "https://wj.qq.com",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,zh-TW;q=0.8"
            }

            
    def send2bark(self, title, content):
        if (self.barklink) and (self.wj[u"链接"] == ""):
            try:
                msg = "{0}/推送标题/{1}/{2}".format(self.barklink, title, content)
                res = requests.get(msg,verify=False)
            except Exception as e:
                print('Reason:', e)
        return
        
    def send2s(self, title, content):
        if (self.skey != ""):
            try:
                link = "https://sc.ftqq.com/{0}.send".format(self.skey)
                d = {'text': title, 'desp': content}
                res = requests.post(link, data=d , verify=False)
            except Exception as e:
                print('Reason:', e)

        return    
        
    def send2BarkAndWJ(self, title, content):
        if (self.barklink) and (self.wj[u"链接"]):
            try:
                msg = "{0}/推送标题/{1}/{2}?url=https://wj.qq.com".format(self.barklink, title, content)
                requests.get(msg,verify=False)
                s = "{\"id\":\"123456\",\"survey_type\":0,\"jsonLoadTime\":3,\"time\":1587372438,\"ua\":\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36\",\"referrer\":\"https://wj.qq.com/mine.html\",\"openid\":\"\",\"pages\":[{\"id\":\"1\",\"questions\":[{\"id\":\"qID\",\"type\":\"text_multiple\",\"blanks\":[{\"id\":\"fID\",\"value\":\"dasdas\"}]}]}],\"latitude\":\"\",\"longitude\":\"\",\"is_update\":false}"
                s = s.replace("123456", self.wj["ID"])
                s = s.replace("qID", self.wj[u"问题ID"])
                s = s.replace("fID", self.wj[u"填空ID"])
                t = "{0}  {1}".format(title, content).decode("utf-8")
                s = s.replace("dasdas", t)
                self.base_headers["Referer"] = self.wj[u"链接"]          
                rjson={
                    "survey_id": self.wj[u"ID"],
                    "answer_survey":s
                }
                
                requests.post("https://wj.qq.com/sur/collect_answer", 
                              headers=self.base_headers, 
                              json=rjson, 
                              verify=False)
            except Exception as e:
                print('Reason:', e) 

        return
    
if __name__ == "__main__":
    pushno = send2phone()
    pushno.send2bark("签到任务 {0} 失败".format('test'), "任务已禁用")
    pushno.send2s("签到任务 {0} 失败".format('test'), "任务已禁用")
    pushno.send2BarkAndWJ(u"签到任务 {0} 失败".format('test'), u"任务已禁用")
