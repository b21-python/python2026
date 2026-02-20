# Day 3

## Goals for today

- Write some python
- Setup git and log into GitHub locally
- Create your first git repo on github
- Add your code to your github repository

## Turning on the Pi

> IMPORTANT: Connect power LAST

Connection checklist
- Connect display via HDMI port closest to USB C Power port
- Connect keyboard and mouse via one of 4 USB ports
- Turn monitor on
- Connect USB power via port next to HDMI
- Pi should turn on automatically, if it does not after a few seconds press the power button

## Write some python

We will review [python101](../day1/python101.md) from last week and then go over [python102](./python102.md)

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
