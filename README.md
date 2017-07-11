# Scheduled speedtest

Internet speedtest at scheduled intervals. For each test, the time, download- and upload-speed are saved in a csv-file.

## Install

Clone this repository using

  $ sudo git clone https://github.com/franksh/scheduled-speedtest.git

Then install the Python requirements using

  $ sudo pip3 install requirements.txt

## Usage

You can configure the intervals between speedtests and other things in config.py.
Then, start the speedtest with

$ python3 speedtest.py

and interrupt at any time with CTRL+C to stop saving.
