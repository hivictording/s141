# Author: Victor Ding

# -*- coding: utf-8 -*-

import logging
import time

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='debug.log',filemode='w',level=logging.DEBUG,\
                    format='%(asctime)s %(levelname)s: %(message)s',datefmt='%d %b %Y %a')

# logging.basicConfig(filename='info.log',level=20)
# logging.basicConfig(filename='warning.log',level=logging.WARNING)
# logging.basicConfig(filename='error.log',level=40)
# logging.basicConfig(filename='critical.log',level=logging.CRITICAL)

logging.warning("This is a %s %s!","555555555555","66666")
logging.critical("{} and {}".format("777","888"))
# logging.info("This is an info message!")
# logging.debug("This is a debug message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

logging.info("Task Started")
time.sleep(3)
logging.info("Task Done")
