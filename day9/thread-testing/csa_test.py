import requests
import threading
import time


def download(file_type, file_name):
    # download single file
    s_time = time.time()
    url = 'http://10.7.100.33/'
    url += f'{file_type}/{file_name}'
    print(f'Task {threading.current_thread().getName()} started......')
    r = requests.get(url, allow_redirects=True)
    open(file_name, 'wb').write(r.content)
    print(f'Task {threading.current_thread().getName()} completed in {time.time() - s_time} seconds......')


def batch_download(step, start_point):
    # download multiple file with multi-threading
    # step: how many files will be downloaded in the batch
    # start_point: download from which file number
    thread_list = []
    for i in range(step):
        number = str(i + start_point).rjust(3, "0")
        new_thread = threading.Thread(name=f'download-{number}', target=download,
                                      args=('200K', f'200K_{number}.pdf'))
        thread_list.append(new_thread)

    for t in thread_list:
        t.start()
        t.join(1.0)


# start time for downloading
start_time = time.time()


counter = 0

size = 30

# total files
total_files = 100

while 1:
    print(f'Downloading files from file number {counter}')
    if total_files - counter > size:
        batch_download(size, counter)
        counter += size
    else:
        batch_download(total_files - counter, counter)
        break

    time.sleep(20.0 - ((time.time() - start_time) % 20.0))

print(time.time() - start_time)
print('End of Main Thread......')
