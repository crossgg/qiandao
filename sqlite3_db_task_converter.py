#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 Binux <roy@binux.me>

import config
from db.task import TaskDB as _TaskDB
from sqlite3_db.basedb import BaseDB
import db.task as task 
import os

class DBconverter(_TaskDB, BaseDB):
    def __init__(self, path=config.sqlite3.path):
        self.path = path
            
    def ConvertNewType(self, path=config.sqlite3.path):
        self.path = path
        if (os.path.isfile(path)):
            if config.db_type == 'sqlite3':
                import sqlite3_db as db
            else:
                import db
            class DB(object):
                user = db.UserDB()
                tpl = db.TPLDB()
                task = db.TaskDB()
                tasklog = db.TaskLogDB()
            self.db = DB
            try:
                self.db.task.get("1", fields=('ontime', 'ontimeflg'))
            except:                
                self._execute("ALTER TABLE `task` ADD `ontimeflg` INT UNSIGNED NOT NULL DEFAULT 0 ")
                self._execute("ALTER TABLE `task` ADD `ontime` VARCHAR(256) NOT NULL DEFAULT '00:10:00' " )            
        return 