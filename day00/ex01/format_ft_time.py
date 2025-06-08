import datetime

dt = datetime.datetime.today()
seconds = dt.timestamp()

x = datetime.datetime.now().date()
print('Seconds since January 1, 1970: {:,} or {:.2e} in scientific notation'.format(seconds, seconds))
print(x.strftime("%b %d %Y"))
