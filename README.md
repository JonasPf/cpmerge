# Description

cpmerge is a simple clipboard manager to synchronize CLIPBOARD and PRIMARY.

Linux has two types of clipboards:
- PRIMARY: Copy by selecting text, paste by middle mouse click
- CLIPBOARD: Copy by using the copy command (usually: CTRL+c), paste by using the paste command (usually: CTRL+v)

cpmerge merges these two clipboards into one. Whenever you copy something into the CLIPBOARD it will automatically be copied into PRIMARY. However when you select something into PRIMARY it waits until you've moved the mouse a little bit before copying it into CLIPBOARD. The reason for this that a lot of people select some text and press CTRL+v to overwrite the selected text. If PRIMARY got copied into CLIPBOARD straight away this would just replace the selected text with itself.

If run with GUI it also keeps track of the last 10 clipboard entries. A taskbar icon allows to copy those old values into the clipboard again.

# Installation

Python 2.7 should already be installed on most systems.
wxPython and pip need to be installed as well. On my Ubuntu machine (with Universe activated) this can be done with:

```
sudo apt-get install python-pip -y
sudo apt-get install python-wxgtk2.8 -y
```

After those requirements are installed, just run:

```
sudo pip install cpmerge
```

cpmerge can be started by simply running: 

```
cpmerge
```

# Configuration

To run it without tray icon and history: 

```
cpmerge --nogui
```

Depending on your screen resolution (and how nervous your mouse hand is) you may need to tweak the distance the mouse needs to be moved before copying from PRIMARY to CLIPBOARD. You can do this with:

```
cpmerge --distance=20
```

For debugging information regarding the mouse distance, run:

```
cpmerge -vv
```

# Other stuff

Py_mem.py tells me that cpmerge uses 35.8 MB of memory. While this is not a huge amount by todays standard I still consider it a lot for the simple task. If you know a tool with similar features which uses less resources, please let me know.

Similar tools (none of them supports the mouse movement before PRIMARY -> CLIPBOARD as far as I'm aware) are listed on: https://wiki.archlinux.org/index.php/clipboard

Homepage: http://jonaspfannschmidt.com/cpmerge
Code: http://github.com/jonaspf/cpmerge
Icon from: http://led24.de/iconset/
