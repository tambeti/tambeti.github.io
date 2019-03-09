#!/usr/bin/env python

from datetime import date
import os
import sys

def usage():
    print "Usage: %s [2019-02-22]" % (sys.argv[0])
    sys.exit(1)

if len(sys.argv) == 1:
    today = date.today()
elif len(sys.argv) == 2:
    import dateutil.parser
    try:
        today = dateutil.parser.parse(sys.argv[1]).date()
    except:
        usage()
else:
    usage()

startDate = date(2017, 1, 2)
startIndex = 460
daysSince = (today-startDate).days

nowIndex = startIndex + daysSince
dateStr = today.strftime("%d%m%Y")

url = 'http://v.postimees.ee/ristsona/Veebiristsonad/Veebiristsona%d-%s/Veebiristsona%d-%s.html' % (nowIndex, dateStr, nowIndex, dateStr)

print url
os.system("open " + url)
