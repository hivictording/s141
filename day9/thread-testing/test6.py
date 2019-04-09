# Author: Victor Ding

# -*- coding: utf-8 -*-

import threading
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s [%(threadName)s] %(message)s')


def worker(message):
    time.sleep(5)
    logging.debug("worker is started, {0}".format(message))


if __name__ == '__main__':
    t = threading.Thread(target=worker, name='worker', kwargs={'message': 'ha,ha'})
    t.daemon = False
    t.start()
    t.join()
    logging.debug("main thread exiting")
