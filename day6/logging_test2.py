# Author: Victor Ding

# -*- coding: utf-8 -*-

import logging

class Ford(logging.Filter):
    def filter(self, record):
        print(dir(record))
        if record.msg.startswith('ford'):
            return True
        else:
            return False


llog = logging.getLogger("log")

llog.setLevel(20)
llog.addFilter(Ford())

llog.critical("ford 2019")
llog.critical("honda 2019")


# mylogger = logging.getLogger(__name__)
#
# print(mylogger)
#
