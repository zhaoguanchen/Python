# -*- coding: UTF-8 -*-


def _check_hql_has_ddl(hql_statement):

  return true
  # list=[]
  # for i in list：

  #   list.append(sql_list[])
  # sql_list = hql_statement.split(";");

  # print(len(sql_list))





def hql_remove_comment(hql):
  S_NEW_LINE = "\n"
  # return true
  res = ""
  if hql.find(S_NEW_LINE):
    sql_list = hql.split(S_NEW_LINE)
    for subSql in sql_list:
      if isComment(subSql):
        continue
      else:
        res = res + delCommentLine(subSql) + S_NEW_LINE
  else:
    res = res + hql

  return res



def remove_end(str,suffix):
  if str.endswith(suffix):
    return str[0:len(str)-len(suffix)]
  else:
    return str
def remove_start(str,suffix):
  if str.startswith(suffix):
    return str[len(suffix):len(str)]
  else:
    return str


def isComment(line):
  str = line.lstrip()
  if  0 == str.startswith("--"):
    return true
  else:
    return false

def delCommentLine(line):

  index = line.find("--")
  # print(index)
  if index > 0 :
    return line[0 : index]
  else:
    return line
  





def ddl_filter(args):
  if args is not None and 0<len(args):
    for arg in args:
      if  arg  is not None:
        sql = remove_start(remove_start(remove_start(arg,"\r"),"\n"),"\t").strip()
        if  arg.startswith("alter ") is True:
          return {'status': -1, "message": "The SQL statement has been intercepted because DDL is not supported. invalid character:alter"}
        if  arg.startswith("create ") is True:
          return {'status': -1, "message": "The SQL statement has been intercepted because DDL is not supported. invalid character:create"}
        if arg.startswith("drop ") is  True :
          return {'status': -1, "message": "The SQL statement has been intercepted because DDL is not supported. invalid character:drop"}
        if  arg.startswith("truncate ") is True:
          return {'status': -1, "message": "The SQL statement has been intercepted because DDL is not supported. invalid character:truncate"}
         
       
  return {'status': 0}






if __name__ == '__main__':
  sql = "create ;table aa;"
  # _check_hql_has_ddl(sql);
  line = delCommentLine(sql)
  line1 =remove_start(line, "cre")
  line2 = remove_end(line, "aa;")
  res = ddl_filter(sql)
  print(line)
  print(line1)
  print(line2)
  print(res)
