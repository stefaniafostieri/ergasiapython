#askhsh6

import calendar

year  = int(raw_input())
month = int(raw_input())

c = calendar.TextCalendar(calendar.SUNDAY)

print "\n",calendar.month_name[month], year, "\n"
print "S\tM\tT\tW\tT\tF\tS\n"

ctr=0
for i in c.itermonthdays(year, month):
    print( format(i, '02d')),"\t",
    ctr +=1
    if(ctr==7):
        print "\n"
        ctr=0