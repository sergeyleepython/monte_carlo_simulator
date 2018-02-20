import threading

from sensors_data import run_sensors, dump_sensors
from dashboard import app

thread1 = threading.Thread(target = run_sensors)
thread2 = threading.Thread(target = app.run_server)
# thread1.daemon = True
# thread2.daemon = True
thread1.start()
thread2.start()