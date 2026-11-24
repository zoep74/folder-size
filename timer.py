import time, sys

secs = int(sys.argv[1]) if len(sys.argv) > 1 else 16
print('sleep', secs)
time.sleep(secs)
print('ok')
