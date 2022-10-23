from multiprocessing.connection import Listener as l
import numpy as np

adrress = ('0.0.0.0',12345)
lis = l(adrress, authkey=b'EZ')
conn = lis.accept()
msg = conn.recv()
print(msg)
print(int.from_bytes(msg,"big"))
conn.close()
lis.close()