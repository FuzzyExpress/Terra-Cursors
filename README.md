Tarraria inspired cursors for Linux

Installation: run `./copy.sh`
```sh
git clone https://github.com/FuzzyExpress/Terra-Cursors/
sudo rm -rf '/usr/share/icons/TerraCursors' # Only needed if updating
sudo cp -r "./TARGET" "/usr/share/icons/TerraCursors" # Ubuntu system icons, might differ on some systems
```
Read more: https://develop.kde.org/docs/features/cursor/#requirements


You can use `run.py` to turn image files into X11 cursor files.
You'll need `xcursorgen` to do it.
Cursor cration details are stores in the image title.
Format like `Name.[frameID].[frameTime].x.y.png`
- Name: name of the cursor, must match the target cursor. (`.lower()` will be run on it)
- frameID: frame number for the cursor, frames will be grouped by Name (Optinal)
- frameTime: the time in `ms` as in interger the frame will be displayed (Optinal: Default `50ms`)
- x: X location of the cursor center
- y: Y location of the cursor center
