# Day 2

## Goals for today

- Write some python
- Create a `code` folder to store code you write
- Download the python2026 repo
- Review and Run cubeZero.py from downloaded repo
- Create your own first game in pygame

## Turning on the Pi

> IMPORTANT: Connect power LAST

Connection checklist
- Connect display via HDMI port closest to USB C Power port
- Connect keyboard and mouse via one of 4 USB ports
- Turn monitor on
- Connect USB power via port next to HDMI
- Pi should turn on automatically, if it does not after a few seconds press the power button

## Create `code` folder

- Open the terminal
- Make sure you are in your user directory by entering `cd ~`
- Create the `code` folder by entering `mkdir code` (you can type `ls` to see the folder you created)
- Enter the `code` folder by entering `cd code`

> Case MaTtErS

## Download the code into the `code` directory

- Enter `git clone https://github.com/b21-python/python2026`
- Wait until complete
- See what you just downloaded by entering `ls`.  You should see a folder `python2026`
- cd into the `python2026` folder and see what's inside by typing `ls`

## Open and run cubeZero.py

- Open the Thonny app by clicking Berry->Programming->Thonny
- Run by clicking the 'Run' menu then 'Run Module'

## Create a GitHub account

If you haven't already create a free account at [GitHub](https://github.com)

## Setting Up Git

You must configure git to have your username and email

```bash
git config --global user.name "My Name"

git config --global user.email "myemail@example.com"
```

> NOTE you should not use your real email address.  got to the [github settings](https://github.com/settings/emails) and use your private email

Once you have set your username and email check that they are set correctly using the list command.

```bash
git config --list
```