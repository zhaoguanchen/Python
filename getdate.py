# -*- coding: UTF-8 -*-

import datetime


now_time = datetime.datetime.now()


print "影响行数", now_time
f = open("log.txt","a")
f.write("now_time %s"%(now_time))
f.close()


