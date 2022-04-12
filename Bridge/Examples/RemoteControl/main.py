from bridge import *
from devices import *
from remoteControls import *

if __name__ == "__main__":
    tv1 = TV('off')
    generic_control = BasicRemoteControl(tv1)