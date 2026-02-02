from multiprocessing import process
import os, subprocess, glob, time


subprocess.run(f"cp Glitched/*.png ./", shell=True)
subprocess.run(f"cp Loading/*.png ./", shell=True)

# time.sleep(2)

images = glob.glob("*.png")


class Frame:
    def __init__(self, path:str, time:int = 50):
        self.path:str = path
        self.time:int = time
    
    def data(self):
        return self.path, self.time

class Cursor:
    def __init__(self, frame1:Frame, name:str, x:int, y:int):
        self.frames:list[Frame] = [frame1]
        self.name:str = name
        self.x:int = x
        self.y:int = y

    def append(self, frame:Frame):
        self.frames.append(frame)

    def write(self, *args:object):

        txt = ''
        for each in args:
            txt += f"{each} "
        
        txt = txt[:-1]

        print(txt, file=self.cfg)
        print(f"<{self}> Wrote:", txt)

    def process(self):
        self.cfg = open('tmp.cursor', 'w')

        for f in self.frames:
            path, time = f.data()
            
            self.write(64, self.x, self.y, path, time)

        self.cfg.close()

        subprocess.run(f"xcursorgen tmp.cursor TARGET/cursors/{self.name}", shell=True)
            



cursors = {}

for image in images:
    ID = None
    time = None
    try:   
        match image.count('.'):
            case 3:
                cursor, x, y, _ = image.split('.')
                print('Adding:', image, 3)
            
            case 4:
                cursor, ID, x, y, _ = image.split('.')
                print('Adding:', image, 4)

            case 5: 
                cursor, ID, time, x, y, _ = image.split('.')
                print('Adding:', image, 5)
            
            case _:
                raise ValueError("File does not comply: name.[frameID].[frameTime].x.y.png")

    except Exception as e:
        print(e, '\nSkipping', image); continue
    
    
    cursor = cursor.lower()
        

    x, y, = int(x), int(y)
    if time:
        frame = Frame(image, int(time))
    else:
        frame = Frame(image)
        
    
    if cursor in cursors:
        cursors[cursor].append(frame)
    else:
        cursors[cursor] = Cursor(frame, cursor, x, y)

    
print('Processing:')
    
for name, cursor in cursors.items():
    print(name)
        
    cursor.process()

subprocess.run(f"rm wait.*.*.20.20.png", shell=True)
subprocess.run(f"rm progress.*.*.20.20.png", shell=True)

subprocess.run(f"sudo ./copy.sh", shell=True)