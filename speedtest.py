"""
Internet speedtest at scheduled intervals

This script performs an internet speedtest using pyspeedtest [1]
at regular intervals scheduled using schedule [2]. For each test
the time, downoad- and upload speed are saved in a csv file.

For configuration see config.py

To execute, run this script

[1] https://pypi.python.org/pypi/pyspeedtest
[2] https://github.com/dbader/schedule
"""
import schedule
import time
import pyspeedtest
import csv
import os.path
from datetime import datetime

from config import config

def run_speedtest():
    """ Runs the speedtest """
    time_now = str(datetime.now())
    st = pyspeedtest.SpeedTest()
    down = st.download()
    up = st.upload()
    print("Time: {}\t Download: {}\t Upload: {}".format(time_now, down, up))
    save_results(time_now, down, up)


def save_results(time_now, download_speed, upload_speed):
    """ Save results to file """
    filename = config['SAVE_FILE']
    # Writer header row if file does not exist
    if not os.path.isfile(filename):
        with open(filename, 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['Time', 'Download', 'Upload'])
    # Write results to file
    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([time_now, download_speed, upload_speed])


if __name__ == '__main__':

    job = schedule.every(config['INTERVAL'])
    job.unit = config['INTERVAL_UNIT']
    job.do(run_speedtest)

    print("Starting speedtest ...")

    while True:
        run_speedtest() # Run first job manually
        schedule.run_pending()
        # time.sleep(1)
