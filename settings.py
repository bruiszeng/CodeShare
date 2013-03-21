#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import sae.const

# 分页时每页的条目数
NAVNUM = 8

settings = {
    "sitename": "代码分享",  # 设置为你的站点名
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "xsrf_cookies": True,
    # 设置为随机的一串字符，千万不要使用现在这个
    "cookie_secret": "11oETzKXQAGaYdkL4gdgjfkdmuYh78768945$6j5k/Vo=",
    "login_url": "/auth/login",
    "autoescape": None,
    "debug": False,
}

#数据库设置
db = {
    "host": sae.const.MYSQL_HOST,
    "db": sae.const.MYSQL_DB,
    "port": sae.const.MYSQL_PORT,
    "user": sae.const.MYSQL_USER,
    "password": sae.const.MYSQL_PASS,
}
