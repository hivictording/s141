# Author: Victor Ding

# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
from robot import run
from ruamel.yaml import YAML
import os,sys
import datetime,time

# import signal
# from robot.running.signalhandler import _StopSignalMonitor as SSM
# from robot.errors import ExecutionFailed
#
# class SONIC_SSM(SSM,object):
#     def __init__(self):
#         SSM.__init__(self)
#
#     def _stop_execution_gracefully(self):
#         raise ExecutionFailed('Execution terminated by signal', exit=True)
#         raise KeyboardInterrupt

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
        fw_models = self.get_arguments("fw_model")
        print(fw_models)
        para_dict = {}
        para_dict['equipment_type'] = fw_models
        yml = ROBOT_YAML()
        with open("parameters.yaml", "w") as fh_para:
            yml.dump(para_dict, fh_para)
        try:
            run(robot_path, variablefile='parameters.yaml')
        except KeyboardInterrupt:
            print("You have pressed CTRL+C!!!!!")
            sys.exit(0)


current_dir = os.getcwd()
robot_path = os.path.dirname(current_dir) + '\\UTMperformance scripts\\RF_IXload_test.txt'
settings = dict(static_path = os.path.dirname(current_dir) + '\\RobotSrv', debug=True,)
application = tornado.web.Application([(r"/index", MainHandler),(r"/robot", RobotHandler), ], **settings)

if __name__ == '__main__':
    try:
        application.listen(9999)
        print("Robot Server Started at %s"% datetime.datetime.now())
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("Bye Bye Bye Bye Bye!!!!!")
        sys.exit(0)
