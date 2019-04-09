# Author: Victor Ding

# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import robot
from ruamel.yaml import YAML
import os


class ROBOT_YAML(YAML):
    def __init__(self):
        YAML.__init__(self)
        self.default_flow_style = False
        self.block_seq_indent = 2
        self.indent = 4
        self.allow_unicode = True
        self.encoding = 'utf-8'

class RobotHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("Robot.html")

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("Robot parameters received.....")
        # fw_models = self.get_argument("fw_model")
        fw_models = self.get_arguments("fw_model")
        print(fw_models)
        para_dict = {}
        para_dict['equipment_type'] = fw_models
        print(para_dict)
        yml = ROBOT_YAML()
        with open("parameters.yaml", "w") as fh_para:
            yml.dump(para_dict, fh_para)
            # self.robot_run()

    def robot_run(self):
        current_dir = os.getcwd()
        robot_path = os.path.dirname(current_dir) + '\\UTMperformance scripts\\RF_IXload_test.txt'
        print(robot_path)
        robot.run(robot_path, variablefile='parameters.yaml')


application = tornado.web.Application([(r"/index", MainHandler),(r"/robot", RobotHandler), ])
# application = tornado.web.Application([(r"/index", MainHandler), ])

if __name__ == '__main__':
    application.listen(9999)
    tornado.ioloop.IOLoop.instance().start()