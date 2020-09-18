# -*- coding: utf-8 -*-
from __future__ import print_function
import os
from datetime import date, time, datetime, timedelta
import time
import multiprocessing

from capture.capture_api import CaptureAPI, file_hash


# from capture_api_client import CaptureServiceAPI
# from capture.capture import CaptureAPI, file_hash


class PerformanceTestAPI():
    def setUp(self):
        self.api_client = CaptureAPI(
            "10.7.100.29", "CC41E2C76CF3", "E7C76F3C1383F5C25388E6863C195B44")

    def test_file_scan_sec(self, file_path, finish_time):
        s_time = time.time()
        start_time = datetime.now()
        file_count = 0
        for one in os.listdir(file_path):
            duration = time.time() - s_time
            filename = os.path.join(file_path, one)
            if os.path.isfile(filename) & (duration <= finish_time):
                print("child id %s" % os.getpid())
                print("duration [%.6f] sec" % duration)
            self.api_client.file_scan(filename)
            file_count += 1
        print(f"end duration {duration}")
        return duration


if __name__ == "__main__":
    test = PerformanceTestAPI()
    test.setUp()
    # print(test)

    path = "D://temp//001.jpg"
    finish = float(1)
    p = [None] * 100
    process_num = 1
    loop_num = 1

    test.test_file_scan_sec(path, finish)

    pool = multiprocessing.Pool(processes=1)
    result = []
    for i in range(loop_num):
        result.append(pool.apply_async(test.test_file_scan_sec, (file_path, finish_time,)))
        time.sleep(1)
    pool.close()
    pool.join()
