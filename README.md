qiandao
=======
基于quchaonet的蓝调主题签到增加了
源镜像：https://hub.docker.com/r/quchaonet/qiandao

1、设置任务最低间隔时间及任务request最高100限制 (by 戏如人生)

http://cordimax.f3322.net:5558/381.html

2、增加了server酱、bark推送（by AragonSnow）

https://hexo.aragon.wang/2020/04/11/%E7%AD%BE%E5%88%B0%E5%A4%B1%E8%B4%A5%E6%8E%A8%E9%80%81%E5%88%B0%E6%89%8B%E6%9C%BA/

需要推送的：
挂载时候添加一个参数 -v 实际目录:/usr/src/app/config,再添加一个config.json文件再实际目录下面，示例：

docker 启动命令：
```
docker run -d --name qiandao -p 12345:80 -v /app/toolapi:/usr/src/app/config -v /etc/localtime:/etc/localtime q123458384/qiandao
```

再在 /app/toolapi 目录下新建一个 config.json文件，内容如下：
```
{
	"bark链接" : "bark的链接，不用就留空",
	"s酱key" : "s酱的skey，不用就留空",
	"腾讯问卷":{
		"链接":"腾讯问卷的链接，不用就留空",
		"ID":"腾讯问卷的ID，不用就留空",
		"问题ID":"腾讯问卷的问题ID，不用就留空",
		"填空ID":"腾讯问卷的填空ID，不用就留空"
	}
}
```

=========
以下为原镜像说明：

签到 —— 一个自动签到框架 base on an HAR editor

HAR editor 使用指南：https://github.com/binux/qiandao/blob/master/docs/har-howto.md

Web
===

需要 python2.7, 虚拟主机无法安装

```
apt-get install python-dev autoconf g++ python-pbkdf2
pip install tornado u-msgpack-python jinja2 chardet requests pbkdf2 pycrypto
```

可选 redis, Mysql

```
mysql < qiandao.sql
```

启动

```
./run.py
```

数据不随项目分发，去 [https://qiandao.today/tpls/public](https://qiandao.today/tpls/public) 查看你需要的模板，点击下载。
在你自己的主页中 「我的模板+」 点击 + 上传。模板需要发布才会在「公开模板」中展示，你需要管理员权限在「我的发布请求」中审批通过。


设置管理员

```
./chrole.py your@email.address admin
```

使用Docker部署站点
==========

可参考 Wiki [Docker部署签到站教程](https://github.com/binux/qiandao/wiki/Docker%E9%83%A8%E7%BD%B2%E7%AD%BE%E5%88%B0%E7%AB%99%E6%95%99%E7%A8%8B)

qiandao.py
==========

```
pip install tornado u-msgpack-python jinja2 chardet requests
./qiandao.py tpl.har [--key=value]* [env.json]
```

config.py
=========
优先用`mailgun`方式发送邮件，如果要用smtp方式发送邮件，请填写mail_smtp, mail_user, mail_password
```python
mail_smtp = ""     # 邮件smtp 地址
mail_user = ""    # 邮件账户
mail_passowrd = ""   # 邮件密码
mail_domain = "mail.qiandao.today"
mailgun_key = ""
```

鸣谢
====

+[Mark][https://www.quchao.net/] 

+[戏如人生][https://www.quchao.net/]

+[AragonSnow][https://hexo.aragon.wang/]

许可
====

MIT
