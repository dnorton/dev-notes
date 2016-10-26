## Keyboard Shortcuts
_[Apple's Keyboard Shortcut page](https://support.apple.com/en-us/HT201236)_

+ `Cmd + e` -- eject selected disk or volume
+ `F4` -- open Launchpad
+ `Ctrl + Left/Right` -- move between desktops
+ `Ctrl + Down` -- view all windows for current app
+ `Cmd + Shift +4` -- screen shot a part of the screen (3 for the whole desktop)
+ `Fn + i` - turn on/off insert
 
### Trackpad Gestures

+ `two finger swipe left` -- opens Notification Center
+ `tap a word with 3 fingers` -- look up word in dictionary
+ `swipe up 3 fingers` -- open Mission Control
+ `3 finger drag` -- move a selected item from one place to another on desktop

## Terminal Commands

### rsync

* `sudo rsync -vaE --progress /Volumes/SourceName /Volumes/DestinationName` -- copy and include extended attributes. See [here](http://apple.stackexchange.com/questions/117465/fastest-and-safest-way-to-copy-massive-data-from-one-external-drive-to-another) for more details

### homebrew
_[homebrew](http://brew.sh/) is the missing package manager for OS X_

* install homebrew:
```bash
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
