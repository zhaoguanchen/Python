# -*- coding: UTF-8 -*-

import MySQLdb
import datetime
#git test:
#主机名
LOCALHOST = '192.168.0.1'
HOST = '192.168.15.55'
#用户名
USER = "root"
#密码
PASSWD = "123456"
#数据库名
DB = "hue"

# 字段、语句定义
id_01 = -1
id_02 = -1
name_01 = "qq"
name_02 = "ww"
id_temp = -1 

# 设置name1
def set_variable_name_01():

	name_01 = raw_input("Please intput name_01:")
	return name_01

# 设置name2	
def set_variable_name_02():

	name_02 = raw_input("Please intput name_02:")
	return name_02




# 连接数据库
def get_connection():

	db = MySQLdb.connect(HOST,USER,PASSWD,DB)	
	return db

# 关闭数据库连接
def close_connection(db):

	db.close()

# 查找账户ID
def find_id(db, name):

	cursor = db.cursor()
	
	try:
	   # 执行SQL语句
		id_temp = -1
			
		sql_check = 'select id from auth_user where username = "%s";'%(name)
		print sql_check

		res = cursor.execute(sql_check)
		
		if res == 0:
			print "账户未找到，请重新输入"
			
			return -1
		
		#获取所有记录列表
		results = cursor.fetchall()		
		for row in results:
			fname = row[0]   
			id_temp = fname
				   
	except:
	    print "Error: unable to fecth data"

	return id_temp


# 更新workflow表
def set_wf(db, id_01, id_02):

	sql_set_wf = 'update desktop_document2 set owner_id=%s where owner_id=%s and type="oozie-workflow2";'%(id_02, id_01)
	print "sql_wf",sql_set_wf
	cursor = db.cursor()
	res = cursor.execute(sql_set_wf)
	print "影响行数", res


# 更新coordinator表
def set_coo(db, id_01, id_02):

	sql_set_coo = 'update desktop_document2 set owner_id=%s where owner_id=%s and type="oozie-coordinator2";'%(id_02, id_01)
	print "set_coo", sql_set_coo
	cursor = db.cursor()
	res = cursor.execute(sql_set_coo)
	print "影响行数", res


# 更新外键表
def set_extra(db, id_02):
	
	sql_set_extra = 'UPDATE desktop_document as a INNER JOIN desktop_document2 as b set a.owner_id=%s where a.object_id =b.id and b.owner_id=%s;'%(id_02, id_02)
	print "sql_extra",sql_set_extra
	cursor = db.cursor()
	res = cursor.execute(sql_set_extra)
	print "影响行数", res

# 信息确认
def confirm(name_01,name_02,id_01,id_02):
	print "确认账号信息"
	print "From：",name_01,"id为",id_01
	print "To：",name_02,"id为",id_02
	print "确认请输入yes"
	confirm_info = raw_input("请输入")
	if confirm_info == "yes":
		return True
	
	else :
		return False


# 日志记录
def log(name_01,name_02):

	now_time = datetime.datetime.now()
	f = open("log.txt","a")
	f.write("%s,   原账户：%s----->目标账户：%s \n"%(now_time, name_01, name_02))
	f.close()
	print "日志已记录"

if __name__ == '__main__':

	print '-----------------------------------------'
	print '任务迁移，请仔细核对信息'
	print '-----------------------------------------'
	

	db = get_connection()	

	while id_01 == -1 :
	 	
		name_01 = set_variable_name_01()
		id_01 = find_id(db, name_01)
	

	while id_02 == -1 :
	 	
		name_02 = set_variable_name_02()
		id_02 = find_id(db, name_02)

	confirm = confirm(name_01,name_02,id_01,id_02)
	if confirm is True:
		
		set_wf(db, id_01, id_02)
		set_coo(db, id_01, id_02)
		set_extra(db, id_02)
	 	print "完成了"
	else :
	 	print "错了？ 重来吧"
	close_connection(db)
	log(name_01,name_02)

