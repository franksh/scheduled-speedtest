# Scheduled speedtest

Internet speedtest at scheduled intervals, written in Python3. For each test, the time, download- and upload-speed are saved in a csv-file.

## Install

Clone this repository using

```bash
git clone https://github.com/franksh/scheduled-speedtest.git
```

Then install the Python 3 requirements with

```bash
pip3 install -r requirements.txt
```

## Usage

You can configure the intervals between speedtests and other things in config.py.
Then, start the speedtest with

```bash
python3 speedtest.py
```

and interrupt at any time with CTRL+C to stop saving.
