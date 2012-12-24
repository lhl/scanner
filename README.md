scanner
=======

Simple Scanning App (OS X, python, tornado, Chrome, ExactScan, Evernote)

This app is a thin wrapper meant to be run via something like Quicksilver.
It's completely keyboard driven and tries to be minimally invasive.

This is built for my Xerox Documate 262, but can probably work w/ other scanners.

Requirements:

- runs on port 1223
- Python
  - appscript
  - tornado
- ExactScan (Pro) -- this is $75-$100; http://www.exactscan.com/
- Google Chrome
- Evernote

Setup:
- change PORT in scan.py if necessary
- Add Profiles to ExactScan w/ the following settings: 
  - Folder name: /private/tmp
  - File name: scan
  - On existing files: Silently overwrite
- Actual Profiles (IDs are hardcoded)
  - 10: Duplex
  - 11: Front
  - 12: Back


Note: This app uses py-appscript, which, sadly is no longer developed or
supported: http://appscript.sourceforge.net/status.html

For more (sad panda) discussion, see:
http://www.leancrew.com/all-this/2012/06/the-first-nail-in-the-coffin-of-python-appscript/
