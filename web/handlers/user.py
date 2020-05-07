#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: Binux<i@binux.me>
#         http://binux.me
# Created on 2014-08-09 11:39:25

import json
import time
import datetime
from tornado import gen

from base import *

import send2phone 

class UserRegBark(BaseHandler):
    @tornado.web.authenticated
    def get(self, taskid):
        user = self.current_user
        task = self.check_permission(self.db.task.get(taskid, fields=('id', 'userid',
            'tplid', 'disabled', 'note')), 'w')

        tpl = self.check_permission(self.db.tpl.get(task['tplid'], fields=('id', 'userid', 'note',
            'sitename', 'siteurl', 'variables')))

        self.render('user_register_barkurl.html', userid=user['id'] ,tpls=[tpl, ], tplid=tpl['id'], tpl=tpl, task=task)
    
    @tornado.web.authenticated
    def post(self, userid):
        self.evil(+5)
        if  ("testbark" in self.request.body_arguments):
            try:
                if  (self.request.body_arguments["barkurl"][0] != ""):
                    barkurl = self.request.body_arguments["barkurl"][0]
                    push = send2phone.send2phone(barkurl=barkurl)
                    t = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
                    push.send2bark(u"正在测试Bark", u"{t} 发送测试".format(t=t))
                else:
                    raise Exception(u"请输入barkurl")
            except Exception as e:
                self.render('tpl_run_failed.html', log=e)
                return
            
            self.render('tpl_run_success.html', log=u"测试成功，请检查是否受到推送")
            return
        
        if  ("send" in self.request.body_arguments):
            try:
                if  (self.request.body_arguments["barkurl"][0] != ""):
                    self.db.user.mod(userid, barkurl = self.request.body_arguments["barkurl"][0])
                else:
                    raise Exception(u"注册失败")
            except Exception as e:
                self.render('tpl_run_failed.html', log=e)
                return
            self.render('tpl_run_success.html', log=u"注册成功")
            return
        
        self.redirect('/my/')
        
class UserRegschan(BaseHandler):
    @tornado.web.authenticated
    def get(self, taskid):
        user = self.current_user
        task = self.check_permission(self.db.task.get(taskid, fields=('id', 'userid',
            'tplid', 'disabled', 'note')), 'w')

        tpl = self.check_permission(self.db.tpl.get(task['tplid'], fields=('id', 'userid', 'note',
            'sitename', 'siteurl', 'variables')))

        self.render('user_register_schan.html', userid=user['id'] ,tpls=[tpl, ], tplid=tpl['id'], tpl=tpl, task=task)
    
    @tornado.web.authenticated
    def post(self, userid):
        self.evil(+5)
        if  ("testschan" in self.request.body_arguments):
            try:
                if  (self.request.body_arguments["skey"][0] != ""):
                    skey = self.request.body_arguments["skey"][0]
                    push = send2phone.send2phone(skey=skey)
                    t = datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')
                    push.send2s(u"正在测试S酱", u"{t} 发送测试".format(t=t))
                else:
                    raise Exception(u"skey")
            except Exception as e:
                self.render('tpl_run_failed.html', log=e)
                return
            
            self.render('tpl_run_success.html', log=u"测试成功，请检查是否受到推送")
            return
        
        if  ("send" in self.request.body_arguments):
            try:
                if  (self.request.body_arguments["skey"][0] != ""):
                    self.db.user.mod(userid, skey = self.request.body_arguments["skey"][0])
                else:
                    raise Exception(u"注册失败")
            except Exception as e:
                self.render('tpl_run_failed.html', log=e)
                return
            self.render('tpl_run_success.html', log=u"注册成功")
            return
        
        self.redirect('/my/')
        
class UserRegPushSw(BaseHandler):
    @tornado.web.authenticated
    def get(self, taskid):
        user = self.current_user
        task = self.check_permission(self.db.task.get(taskid, fields=('id', 'userid',
            'tplid', 'disabled', 'note')), 'w')

        tpl = self.check_permission(self.db.tpl.get(task['tplid'], fields=('id', 'userid', 'note',
            'sitename', 'siteurl', 'variables')))

        self.render('user_register_pushsw.html', userid=user['id'] ,tpls=[tpl, ], tplid=tpl['id'], tpl=tpl, task=task)
    
    @tornado.web.authenticated
    def post(self, userid):
        self.evil(+5)
        handpush_succ_flg = 0
        handpush_fail_flg = 0
        autopush_succ_flg = 0
        autopush_fail_flg = 0
        if  ("handpush_succ" in self.request.body_arguments):
            handpush_succ_flg = 1
        if  ("handpush_fail" in self.request.body_arguments):
            handpush_fail_flg = 1
        if  ("autopush_succ" in self.request.body_arguments):
            autopush_succ_flg = 1
        if  ("autopush_fail" in self.request.body_arguments): 
            autopush_fail_flg = 1
        flg = (handpush_succ_flg << 3) | (handpush_fail_flg << 2) | (autopush_succ_flg << 1)  | (autopush_fail_flg)
        self.db.user.mod(userid, noticeflg=flg)
        
        self.redirect('/my/')
     
handlers = [
        ('/user/(\d+)/barkurl', UserRegBark),
        ('/user/(\d+)/schan', UserRegschan),
        ('/user/(\d+)/pushsw', UserRegPushSw),
        ]
