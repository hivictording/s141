# Author: Victor Ding

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("You are getting...")
        user = self.get_argument("user")
        pwd = self.get_argument("password")
        if user == 'victor' and pwd == 'victor':
            self.write("Authentication Success")
        else:
            self.write("Authentication Failed")

    def post(self):
        print("You're posting...")
        user = self.get_argument("user")
        pwd = self.get_argument("password")
        self.write("POST POST POST POST POST")

application = tornado.web.Application([
    (r"/index",MainHandler),
])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
