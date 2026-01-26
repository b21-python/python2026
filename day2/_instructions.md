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

### Configure user name and email

Enter the following commands in the terminal using your name and email.

```bash
git config --global user.name "My Name"

git config --global user.email "myemail@example.com"
```

> NOTE you should not use your real email address.  got to the [github settings](https://github.com/settings/emails) and use your private email

Once you have set your username and email check that they are set correctly using the list command.

```bash
git config --list
```

### Login to github from terminal

Install github command line by entering the following in the terminal

```bash
sudo apt install gh
```

Entery `y` when asked

Use the `gh` command to login enter the following in the terminal

```bash
gh auth login
```

Choose these answers when asked

- ? What account do you want to log into? 
  - Answer: GitHub.com
- ? What is your preferred protocol for Git operations on this host?
  - Answer: HTTPS
- ? Authenticate Git with your GitHub credentials?
  - Answer: Yes
- ? How would you like to authenticate GitHub CLI?
  - Answer: Login with a web browser

Follow the instructions in the terminal and login via the web page opened.