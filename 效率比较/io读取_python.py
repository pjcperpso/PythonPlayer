import datetime
start = datetime.datetime.now()
with open("radwtmp",'r') as fileread:
    data = fileread.read()
    print(data)
stop = datetime.datetime.now()
print((stop-start).microseconds/1000)
