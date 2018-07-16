# -*- coding: UTF-8 -*-

import MySQLdb

#主机名
LOCALHOST = '192.168.0.1'
HOST = '192.168.15.55'
#用户名
USER = "root"
#密码
PASSWD = "123456"
#数据库名
DB = "hue"
id_01 = -1
id_02 = -1
name_01 = raw_input("Please intput name_01:")
print name_01
name_02 = raw_input("Please intput name_02:")
print name_02

sql_check_1 = 'select id from auth_user where username = "%s";'%(name_01)
sql_check_2 = 'select id from auth_user where username = "%s";'%(name_02)





# 打开数据库连接
db=MySQLdb.connect(HOST,USER,PASSWD,DB)
# 获取操作游标
cursor=db.cursor()
# command_a = "select id from auth_user"
# cursor.execute(command_a)
# # 提交到数据库执行
# db.commit()
# # 关闭数据库连接

# name = zhaoguanchen

# sql = "select id from auth_user where username=%s;"


# name = "zhaoguanchen"
# print name
#    # cursor.execute("select id from auth_user where username=%s"%name)
# sql = 'select id from auth_user where username = "%s";'%(name)
# print sql

# res = cursor.execute(sql)
# db.commit()

#    # 获取所有记录列表


# results = cursor.fetchall()
# for row in results:
#   	fname = row[0]
    
# 	print "fname=%s" % (fname)

# 查找原账户ID

try:
#    # 执行SQL语句	
	res = cursor.execute(sql_check_1)
	while res == 0:
		print "原账户未找到，请重新输入0"
		name_01 = raw_input("Please intput name_01:")
		print name_01
		sql_check_1 = 'select id from auth_user where username = "%s";'%(name_01)
		res = cursor.execute(sql_check_1)
		print sql_check_1
	# db.commit()
		
#获取所有记录列表
	results = cursor.fetchall()

	
	for row in results:
		fname = row[0]   
		print "%s : %s" % (name_01, fname)
		id_01 = fname
		
   
except:
    print "Error: unable to fecth data with name_01"

# 查找目标账户ID

try:
#    # 执行SQL语句	
	res = cursor.execute(sql_check_2)
	while res == 0:
		print "目标账户未找到，请重新输入0"
		name_02 = raw_input("Please intput name_02:")
		print name_02
		sql_check_2 = 'select id from auth_user where username = "%s";'%(name_02)
		res = cursor.execute(sql_check_2)
	# db.commit()

#获取所有记录列表
	results = cursor.fetchall()
	for row in results:
		fname = row[0]   
		print "%s : %s" % (name_02, fname)
		id_02 = fname
   
except:
    print "Error: unable to fecth data with name_02"


if id_01 == -1:
	print "原账户未找到，请重新输入"
print id_01
print id_02
# sql_wf = 'update desktop_document2 set owner_id=74 where owner_id=57 and type="oozie-workflow2";'
# sql_coo = 'update desktop_document2 set owner_id=74 where owner_id=57 and type="oozie-coordinator2";'
# sql_extra = 'UPDATE desktop_document as a INNER JOIN desktop_document2 as b set a.owner_id=74 where a.object_id =b.id and b.owner_id=74;'






