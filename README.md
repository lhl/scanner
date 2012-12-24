scanner
=======

Simple Scanning App (OS X, python, tornado, Chrome, ExactScan, Evernote)

This app is a thin wrapper meant to be run via something like Quicksilver.
It's completely keyboard driven and tries to be minimally invasive, allowing
quick scanning via ExactScan into Evernote on OS X (tested on 10.8).

This is built for my Xerox Documate 262, but can probably work w/ other scanners.
If you haven't bought a scanner yet and are thinking about scanning into Evernote
there are scanners (like the [Fujitsu ScanSnap](http://www.amazon.com/gp/product/B001XWCQO2/ref=as_li_ss_tl?ie=UTF8&tag=randomfoo-20&linkCode=as2&camp=1789&creative=390957&creativeASIN=B001XWCQO2)) that will save you time and effort
w/ 1-click scanning into Evernote built-in.

Code is rough around the edges but putting this out there in case anyway finds it
useful as it includes a few interesting snippets I haven't seen around anywhere:
- opening/URL loading Google Chrome via py-appscript
- subprocess multiline calls via osascript (ExactScan)
- py-appscript posting to Evernote

Also, new to me:
- Automator self-path finding


How it Works
------------
![screenshot](https://www.evernote.com/shard/s1/sh/b063ac72-6056-4702-95f0-18b7fe6f7afc/63af8e838970dcc40a42a4adef42097a/res/afe260b3-f54d-446b-b2c5-86b1d9f8bead/skitch.png)
The 'scan' app is meant to be launched via keyboard which starts the scan.py server
(if necessary) and opens a simple UI. Your last-used settings are remembered and
everything is keyboard-accelerated (ctrl-letter or letter when text fields are unfocused).

ctrl-s, ctrl-enter, cmd-enter and escape work globally and do what you'd expect.

window is automatically closed when scanning is finished.


Requirements
------------
- runs on port 1223
- Python
  - appscript
  - tornado
- ExactScan (Pro) -- this is $75/$100; http://www.exactscan.com/
- Google Chrome
- Evernote


Setup
-----
- change PORT in scan.py if necessary
- Add Profiles to ExactScan w/ the following settings: 
  - Folder name: /private/tmp
  - File name: scan
  - On existing files: Silently overwrite
- Actual Profiles (IDs are hardcoded)
  - 10: Duplex
  - 11: Front
  - 12: Back
- Evernote notebook 'scan._inbox' (recommend putting scans in a stack), hardcoded

Notes
-----
This app uses py-appscript, which, sadly is no longer developed or
supported (but is a lot more pleasant than passing via osascript when it works): 
http://appscript.sourceforge.net/status.html

For more (sad panda) discussion, see:
http://www.leancrew.com/all-this/2012/06/the-first-nail-in-the-coffin-of-python-appscript/

For some other notes/code on Evernote scanning:
- http://norman.walsh.name/2009/11/01/evernote
- http://blog.evernote.com/blog/2008/11/12/scan-to-evernote-on-mac/
- http://katiefloyd.me/revisiting-evernote-and-paperless-updated-hazel-rule/
- http://discussion.evernote.com/topic/27005-help-image-capture-wont-allow-scan-to-evernote/page__st__20

License
-------
This code is licensed under CC-BY-SA 3.0. Basically, copyleft.
http://creativecommons.org/licenses/by-sa/3.0/

Shiny radio buttons adapted from Matt Gentile's CSS3 UI Kit: http://www.icondeposit.com/design:58
CC-BY 3.0
