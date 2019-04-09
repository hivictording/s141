# Author: Victor Ding

import tornado.ioloop
import tornado.web
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("You are getting...")
        comments = self.get_argument("comments")
        vendors = self.get_arguments("vendors")
        print(type(comments))
        print(comments)
        print(vendors)

    def post(self,*args,**kwargs):
        # print("You're posting a file.....")
        ret = {'result': 'OK'}
        # file_metas = self.request.files.get('sonicwall',None)
        file_metas = self.request.files['sonicwall']
        # print(file_metas)

        if not file_metas:
            ret['result'] = 'Invalid Args'
            return ret

        for meta in file_metas:
            print(meta)
            file_name = meta['filename']
            print("You're posting a file %s" %file_name)
            with open(file_name,'wb') as fh_file:
                fh_file.write(meta['body'])

        self.write(json.dumps(ret))
application = tornado.web.Application([
    (r"/index",MainHandler),
])

if __name__ == '__main__':
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
