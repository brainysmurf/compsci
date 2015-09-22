from datetime import datetime
now = datetime.now()

print "%s/%s/%s %s:%s:%s" % (now.year, now.month, now.day, now.hour, now.minute, now.second) 

# Or you can use the format method, which I think is a bit more readable
print "{}/{}/{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
# Reference for that is here: https://docs.python.org/2/library/stdtypes.html#string-formatting
# Interesting reading for it is here: http://stackoverflow.com/questions/5082452/python-string-formatting-vs-format

# Or, even better, use the strftime method
print now.strftime('%Y/%m/%d %H:%M:%S')
# Reference here: https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior
# The only difference is that month is actually zero-padded
