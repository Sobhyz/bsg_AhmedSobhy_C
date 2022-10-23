from multiprocessing.connection import Client as cli

address = ('0.0.0.0', 12345)
conn = cli(address, authkey=b'EZ')
conn.send(bytes([100]))
conn.close()