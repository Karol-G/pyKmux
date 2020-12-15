# pyKmux
[![License](https://img.shields.io/badge/License-MIT-brightgreen.svg)](LICENSE)

A small and simple python script to automatically renew a kerberos ticket in a tmux session

## Installation
* Install pexpect with: `pip install pexpect`
* Clone the pyKmux repo
* Execute `kinit` in your terminal and copy the entire password prompt (including the colon) into `password_prompt` in `pykmux.py`
* Type in your password in `password` in `pykmux.py`

## How to use
* Create or attach to a tmux session: `tmux new` or `tmux a -t X`
* Open a new tmux pane: `Ctrl+B "`
* Activate the new pane: `Ctrl+B DOWN`
* Execute `pykmux.py` every 5 hours: `watch -n 18000 "python pykmux.py"`
* (Optional) Hide the pane
