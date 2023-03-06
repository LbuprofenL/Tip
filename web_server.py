# -*- coding:utf-8 -*-

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.options import options, define

define("port", default=8000, type=int)


class IndexHandler(RequestHandler):

    def get(self):
        # 获取get方式的参数
        user = self.get_argument("user")
        print("get方式获取参数：" + str(user))

    def post(self):
        # 获取post方式的参数
        # user = self.get_argument("user")
        Ia = self.get_argument("Ia")
        print("post方式获取参数：" + str(Ia))


if __name__ == "__main__":
    app = Application([(r"/", IndexHandler)])
    app.listen(8888)
    IOLoop.current().start()
