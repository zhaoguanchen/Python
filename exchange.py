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

# 字段、语句定义
id_01 = -1
id_02 = -1
name_01 = "qq"
name_02 = "ww"
id_temp = -1 


def set_variable():
	global name_01
	global name_02
	name_01 = raw_input("Please intput name_01:")
	print name_01
	name_02 = raw_input("Please intput name_02:")
	print name_02


# sql_check_1 = 'select id from auth_user where username = "%s";'%(name_01)
# sql_check_2 = 'select id from auth_user where username = "%s";'%(name_02)


# 连接数据库
def get_connection():

	db = MySQLdb.connect(HOST,USER,PASSWD,DB)
	cursor = db.cursor()
	return cursor



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
def executeQuery(self, sqlcode):
        try:
            self.cur.execute(sqlcode)
            resultSet = self.cur.fetchall()
            self.conn.commit()
            return resultSet
        except Exception as e:
            self.conn.rollback()
            raise e

# 查找原账户ID
def find_id(name):


		cursor = get_connection()
	
	# try:
	#    # 执行SQL语句	
		
		sql_check = 'select id from auth_user where username = "%s";'%(name)
		print sql_check
		res = cursor.execute(sql_check)
		print res
		while res == 0:
			print "账户未找到，请重新输入0"
			name_01 = raw_input("Please intput name_01:")
			print name_01
			
			res = cursor.execute(sql_check)
			# print sql_check_1
		
	#获取所有记录列表
		results = cursor.fetchall()

		
		for row in results:
			fname = row[0]   
			global id_temp
			global name_01
			global name_02
			print "%s : %s" % (name_01, fname)
			id_temp= fname
			
	   
	# except:
	#     print "Error: unable to fecth data with name_01"


		return id_temp







# # 查找目标账户ID

# try:
# #    # 执行SQL语句	
# 	res = cursor.execute(sql_check_2)
# 	while res == 0:
# 		print "目标账户未找到，请重新输入0"
# 		name_02 = raw_input("Please intput name_02:")
# 		print name_02
# 		sql_check_2 = 'select id from auth_user where username = "%s";'%(name_02)
# 		res = cursor.execute(sql_check_2)
# 	# db.commit()

# #获取所有记录列表
# 	results = cursor.fetchall()
# 	for row in results:
# 		fname = row[0]   
# 		print "%s : %s" % (name_02, fname)
# 		id_02 = fname
   
# except:
#     print "Error: unable to fecth data with name_02"





# sql_wf = 'update desktop_document2 set owner_id=74 where owner_id=57 and type="oozie-workflow2";'
# sql_coo = 'update desktop_document2 set owner_id=74 where owner_id=57 and type="oozie-coordinator2";'
# sql_extra = 'UPDATE desktop_document as a INNER JOIN desktop_document2 as b set a.owner_id=74 where a.object_id =b.id and b.owner_id=74;'




# def generate_html(from_someone, to_someone, words, title="love"):
#     """
#     :param from_someone: your name as type string
#     :param to_someone:  your girlfriend's/boyfriend's name
#     :param words: what you want to say
#     :param title: the html page title
#     :return: None. But a html file will be generate
#     """
#     html = open('html/template.html', encoding='UTF-8').read()
#     pixel_matrix = text2pixel(words, width=140, height=30)
#     six_nine = matrix2six_nine(pixel_matrix)

#     html = html.replace('Your_name', from_someone)
#     html = html.replace('Somebody', to_someone)
#     html = html.replace('Generate text and fill in here!', six_nine)
#     html = html.replace('Replace title here', title)

#     with open('html/main.html', 'w', encoding='utf-8') as f:
#         f.write(html)
#         f.close()


# if __name__ == '__main__':

#     # generate_html(from_someone, to_someone, words)
#     generate_html("Peichun", "You", "Nice to meet you!", title="hello")



if __name__ == '__main__':
	print 'aaaaaaa'
	set_variable()
	print name_01
	print name_02
	
	id_01 = find_id(name_01)
	id_02 = find_id(name_02)
	print id_01
	print id_02


