# -*- coding: UTF-8 -*-
# 用于拦截执行语hive句中的DDL操作
# 应用场景为hue


# 删除注释   
def _check_hql_has_ddl(hql_statement):
  sign_new_line = "\n"
  sql_temp = ""
  if hql_statement.find(sign_new_line):
    sql_list = hql_statement.split(sign_new_line)
    for subSql in sql_list:
      if is_comment(subSql):
        continue
      else:
        sql_temp = sql_temp + delete_comment_in_line(subSql) + sign_new_line
  else:
    sql_temp = sql_temp + hql_statement

  sql = remove_end(sql_temp, sign_new_line)

  check_ddl = has_ddl(sql)
  return check_ddl


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

# 判断是否是注释行
def is_comment(line):
  str = line.lstrip()
  if  str.startswith("--"):
    return True
  else:
    return False

# 删除行内注释
def delete_comment_in_line(line):
  index = line.find("--")
  if index > 0 :
    return line[0 : index]
  else:
    return line
  

def has_ddl(sql):

  cmdlist = []
  command = ""
  for cmdpart in sql.split(";"):
    if cmdpart.endswith("\\"):
      command = command + cmdpart[0:len(cmdpart) -1 ] + ";"
      continue
    else:
      command = command + cmdpart
      
    cmdlist.append(command)
    command = ""

  if cmdlist is not None and 0<len(cmdlist):
    for arg in cmdlist:
      if  arg  is not None:
        sql = remove_start(remove_start(remove_start(arg,"\r"),"\n"),"\t").strip()

        if  sql.startswith("alter "):
          return {'status': -1, "message": "The SQL statement has been intercepted because DDL is not supported. invalid character:alter"}
        if  sql.startswith("create "):
          return {'status': -1, "message": "The SQL statement has been intercepted because DDL is not supported. invalid character:create"}
        if sql.startswith("drop "):
          return {'status': -1, "message": "The SQL statement has been intercepted because DDL is not supported. invalid character:drop"}
        if  sql.startswith("truncate "):
          return {'status': -1, "message": "The SQL statement has been intercepted because DDL is not supported. invalid character:truncate"}
         
  return {'status': 0}
  

if __name__ == '__main__':
  sql1="set hive.support.concurrency=false;--create d \nalter mapreduce.job.queuename = root.bdc.dw;\nd --drop overwrite table yiche_mai.aggr_traffic_page_os_day partition (pt='2018-09-04')\ndrop t1.ychpageid as view_page_id           \ncreate\t  ,t1.platformtype as platform_type      \n\t  ,t1.viewipcityid as city_id           \n\t  ,nvl(t1.clientos,-9999) as os           \n\t  ,t1.rfpa_tracker as rfpa_tracker      \n\t  ,t1.ychrfpa_tracker  as ychrfpa_tracker\n\t  ,t1.externalrfpa_tracker  as externalrfpa_tracker\n\t  ,nvl(t1.pv,0) as pv                     -- 浏览量\n\t  ,nvl(t1.uv,0) as uv                     -- 独立访客\n\t  ,nvl(t2.new_uv,0) as new_uv             -- 首次访问*\n\t  ,nvl(t1.viewip,0) as ip                 -- IP\n\t  ,nvl(t1.vv,0) as vv                     -- 访次\n\t  ,nvl(t5.visit_again_cnt,0) as visit_again_cnt   -- 多次访问人数*\n\t  ,nvl(t1.sum_visit_time,0) as sum_visit_time     -- 总流量时长\n\t  ,nvl(t1.sum_visit_time/t1.vv,0) as avg_visit_times   -- 平均浏览时长\n\t  ,nvl(t1.pv/t1.uv,0) as avg_visit_page   -- 平均浏览页数\n\t  ,nvl(t1.pv/t1.vv,0) as avg_visit_depth  -- 平均浏览深度\n\t  ,nvl(t3.bounce_cnt,0) as bounce_cnt     -- 跳出量*\n\t  ,nvl(t4.exit_cnt,0) as exit_cnt         -- 退出量*    \nfrom (\n\tselect ychpageid       -- 易车惠页面标签\n\t\t  ,platformtype    -- 平台类型1：pc/3：wap\n\t\t  ,viewipcityid    -- IP地址所在的地市id\n\t\t  ,clientos        -- 客户端系统\n\t\t  ,rfpa_tracker    -- URL参数-rfpa_tracker\n\t\t  ,ychrfpa_tracker -- URL参数-ychrfpa_tracker\n\t\t  ,externalrfpa_tracker      -- URL参数-externalrfpa_tracker\n\t\t  ,count(cookieid) as pv     -- Cookie中标识值\n\t\t  ,count(distinct cookieid) as uv  -- viewip IP地址按照数字存储\n\t\t  ,count(distinct viewip) as viewip\n\t\t  ,count(distinct viewid) as vv\n\t\t  ,sum(duration) as sum_visit_time -- 访问时长\n\tfrom yiche_mai.attr_traffic_mai_day\n\twhere pt='2018-09-04' and ychpageid is not null\n\tgroup by ychpageid       -- 易车惠页面标签\n\t\t    ,platformtype    -- 平台类型1：pc/3：wap\n\t\t    ,viewipcityid    -- IP地址所在的地市id\n\t\t    ,clientos        -- 客户端系统\n\t\t    ,rfpa_tracker    -- URL参数-rfpa_tracker\n\t\t    ,ychrfpa_tracker -- URL参数-ychrfpa_tracker\n\t\t    ,externalrfpa_tracker      -- URL参数-externalrfpa_tracker\n\t\t    ,clientos        -- 客户端系统\n    union all \n    select if(b.type='m',888,777)    as ychpageid\n\t\t  ,platformtype    -- 平台类型1：pc/3：wap\n\t\t  ,viewipcityid    -- IP地址所在的地市id\n\t\t  ,clientos        -- 客户端系统\n\t\t  ,rfpa_tracker    -- URL参数-rfpa_tracker\n\t\t  ,ychrfpa_tracker -- URL参数-ychrfpa_tracker\n\t\t  ,externalrfpa_tracker      -- URL参数-externalrfpa_tracker\n\t\t  ,count(cookieid) as pv     -- Cookie中标识值\n\t\t  ,count(distinct cookieid) as uv  -- viewip IP地址按照数字存储\n\t\t  ,count(distinct viewip) as viewip\n\t\t  ,count(distinct viewid) as vv\n\t\t  ,sum(duration) as sum_visit_time -- 访问时长\n\tfrom yiche_mai.attr_traffic_mai_day   a\n\tleft join  yiche_mai.dim_ychpage  b\n\ton a.ychpageid=b.ychpageid\n\twhere pt='2018-09-04' and a.ychpageid is not null\n\tgroup by if(b.type='m',888,777) \n\t\t    ,platformtype    -- 平台类型1：pc/3：wap\n\t\t    ,viewipcityid    -- IP地址所在的地市id\n\t\t    ,clientos        -- 客户端系统\n\t\t    ,rfpa_tracker    -- URL参数-rfpa_tracker\n\t\t    ,ychrfpa_tracker -- URL参数-ychrfpa_tracker\n\t\t    ,externalrfpa_tracker      -- URL参数-externalrfpa_tracker\n\t\t    ,clientos        -- 客户端系统\n\n) t1\nleft join\n(\t  \n\tselect ychpageid         -- 易车惠页面标签\n\t      ,platformtype      -- 平台类型1：pc/3：wap\n\t      ,viewipcityid\n\t      ,clientos        -- 客户端系统\n\t      ,rfpa_tracker\n\t      ,ychrfpa_tracker\n\t      ,externalrfpa_tracker\n\t      ,count(distinct cookieid)  as  new_uv\n    from \n        (select ychpageid         -- 易车惠页面标签\n\t           ,platformtype      -- 平台类型1：pc/3：wap\n\t           ,viewipcityid\n\t           ,clientos        -- 客户端系统\n\t           ,rfpa_tracker\n\t           ,ychrfpa_tracker\n\t           ,externalrfpa_tracker\n\t           ,cookieid\n        \t   ,min(viewservertime) min_viewservertime\n         from yiche_mai.attr_traffic_mai_day\n         where pt between date_sub('2018-09-04',180) and '2018-09-04'\n         group by ychpageid\n                 ,platformtype\n                 ,viewipcityid\n                 ,clientos        -- 客户端系统\n                 ,cookieid\n                 ,rfpa_tracker\n                 ,ychrfpa_tracker\n\t             ,externalrfpa_tracker\n\t             ,cookieid\n          union all \n          select  if(b.type='m',888,777)    as ychpageid\n\t           ,platformtype      -- 平台类型1：pc/3：wap\n\t           ,viewipcityid\n\t           ,clientos        -- 客户端系统\n\t           ,rfpa_tracker\n\t           ,ychrfpa_tracker\n\t           ,externalrfpa_tracker\n\t           ,cookieid\n        \t   ,min(viewservertime) min_viewservertime\n         from yiche_mai.attr_traffic_mai_day a\n         left join yiche_mai.dim_ychpage  b\n         on a.ychpageid=b.ychpageid\n         where pt between date_sub('2018-09-04',180) and '2018-09-04'\n         group by if(b.type='m',888,777)    \n                 ,platformtype\n                 ,viewipcityid\n                 ,clientos        -- 客户端系统\n                 ,cookieid\n                 ,rfpa_tracker\n                 ,ychrfpa_tracker\n\t             ,externalrfpa_tracker\n\t             ,cookieid\n        ) tb1\n    where to_date(min_viewservertime)='2018-09-04'\n    group by ychpageid         -- 易车惠页面标签\n\t        ,platformtype      -- 平台类型1：pc/3：wap\n\t        ,viewipcityid\n\t        ,clientos        -- 客户端系统\n\t        ,rfpa_tracker\n\t        ,ychrfpa_tracker\n\t        ,externalrfpa_tracker\n)t2\n on t1.ychpageid=t2.ychpageid \nand t1.viewipcityid=t2.viewipcityid \nand t1.clientos=t2.clientos\nand t1.platformtype=t2.platformtype\nand t1.rfpa_tracker=t2.rfpa_tracker\nand t1.ychrfpa_tracker=t2.ychrfpa_tracker\nand t1.externalrfpa_tracker=t2.externalrfpa_tracker\nleft join\n(\t\n\tselect ychpageid         -- 易车惠页面标签\n\t       ,platformtype     -- 平台类型1：pc/3：wap\n\t       ,viewipcityid\n\t       ,clientos        -- 客户端系统\n\t       ,rfpa_tracker\n\t       ,ychrfpa_tracker\n\t       ,externalrfpa_tracker\n\t       ,count(distinct viewid) as bounce_cnt\n\tfrom (\n\tselect ychpageid         -- 易车惠页面标签\n\t       ,platformtype     -- 平台类型1：pc/3：wap\n\t       ,viewipcityid\n\t       ,clientos        -- 客户端系统\n\t       ,rfpa_tracker\n\t       ,ychrfpa_tracker\n\t       ,externalrfpa_tracker\n\t       ,cookieid\n\t       ,viewid\n\t       ,count(viewid) as bounce_c\n\tfrom\n\t\t(\n\t\tselect ychpageid         -- 易车惠页面标签\n\t           ,platformtype     -- 平台类型1：pc/3：wap\n\t           ,viewipcityid\n\t           ,clientos        -- 客户端系统\n\t           ,rfpa_tracker\n\t           ,ychrfpa_tracker\n\t           ,externalrfpa_tracker\n\t           ,cookieid\n\t\t       ,viewid\n\t\t       ,count(viewurl) as bounce\n\t\tfrom yiche_mai.attr_traffic_mai_day\n\t\twhere pt='2018-09-04'\n\t\tgroup by ychpageid        -- 易车惠页面标签\n\t           ,platformtype      -- 平台类型1：pc/3：wap\n\t           ,viewipcityid\n\t           ,clientos        -- 客户端系统\n\t           ,rfpa_tracker\n\t           ,ychrfpa_tracker\n\t           ,externalrfpa_tracker\n\t           ,cookieid\n\t\t       ,viewid\n        union all \n        select if(b.type='m',888,777)    as ychpageid\n\t           ,platformtype     -- 平台类型1：pc/3：wap\n\t           ,viewipcityid\n\t           ,clientos        -- 客户端系统\n\t           ,rfpa_tracker\n\t           ,ychrfpa_tracker\n\t           ,externalrfpa_tracker\n\t           ,cookieid\n\t\t       ,viewid\n\t\t       ,count(viewurl) as bounce\n\t\tfrom yiche_mai.attr_traffic_mai_day a\n\t\tleft join yiche_mai.dim_ychpage  b\n\t           on a.ychpageid=b.ychpageid\n\t\twhere pt='2018-09-04'\n\t\tgroup by if(b.type='m',888,777)    \n\t           ,platformtype      -- 平台类型1：pc/3：wap\n\t           ,viewipcityid\n\t           ,clientos        -- 客户端系统\n\t           ,rfpa_tracker\n\t           ,ychrfpa_tracker\n\t           ,externalrfpa_tracker\n\t           ,cookieid\n\t\t       ,viewid\n\t\t) o\n\twhere bounce=1\n\tgroup by ychpageid         -- 易车惠页面标签\n\t         ,platformtype     -- 平台类型1：pc/3：wap\n\t         ,viewipcityid\n\t         ,clientos        -- 客户端系统\n\t         ,rfpa_tracker\n\t         ,ychrfpa_tracker\n\t         ,externalrfpa_tracker\n\t         ,cookieid\n\t         ,viewid\n\t\t) q\n\twhere bounce_c=1\n\tgroup by ychpageid         -- 易车惠页面标签\n\t         ,platformtype     -- 平台类型1：pc/3：wap\n\t         ,viewipcityid\n\t         ,clientos        -- 客户端系统\n\t         ,rfpa_tracker\n\t         ,ychrfpa_tracker\n\t         ,externalrfpa_tracker\n\t) t3\n on t1.ychpageid=t3.ychpageid \nand t1.viewipcityid=t3.viewipcityid \nand t1.clientos=t3.clientos\nand t1.platformtype=t3.platformtype\nand t1.rfpa_tracker=t3.rfpa_tracker\nand t1.ychrfpa_tracker=t3.ychrfpa_tracker\nand t1.externalrfpa_tracker=t3.externalrfpa_tracker\nleft join\n(\t\n\tselect ychpageid         -- 易车惠页面标签\n\t       ,platformtype     -- 平台类型1：pc/3：wap\n\t       ,viewipcityid\n\t       ,clientos        -- 客户端系统\n\t       ,rfpa_tracker\n\t       ,ychrfpa_tracker\n\t       ,externalrfpa_tracker\n\t       ,count(1) as exit_cnt\n\tfrom\n\t\t(\n\t\tselect ychpageid        -- 易车惠页面标签\n\t           ,platformtype      -- 平台类型1：pc/3：wap\n\t           ,viewipcityid\n\t           ,clientos        -- 客户端系统\n\t           ,rfpa_tracker\n\t           ,ychrfpa_tracker\n\t           ,externalrfpa_tracker\n\t           ,cookieid\n\t\t       ,viewid\n\t\t       ,row_number() over(partition by cookieid,viewid order by viewservertime desc) rn\n\t\tfrom yiche_mai.attr_traffic_mai_day\n\t\twhere pt='2018-09-04'\n\t\tunion all\n\t\tselect if(b.type='m',888,777)    as ychpageid\n\t           ,platformtype      -- 平台类型1：pc/3：wap\n\t           ,viewipcityid\n\t           ,clientos        -- 客户端系统\n\t           ,rfpa_tracker\n\t           ,ychrfpa_tracker\n\t           ,externalrfpa_tracker\n\t           ,cookieid\n\t\t       ,viewid\n\t\t       ,row_number() over(partition by cookieid,viewid order by viewservertime desc) rn\n\t\tfrom yiche_mai.attr_traffic_mai_day a\n\t\tleft join yiche_mai.dim_ychpage  b\n\t           on a.ychpageid=b.ychpageid\n\t\twhere pt='2018-09-04'\n\t\t) p\n\twhere rn=1\n\tgroup by ychpageid         -- 易车惠页面标签\n\t         ,platformtype     -- 平台类型1：pc/3：wap\n\t         ,viewipcityid\n\t         ,clientos        -- 客户端系统\n\t         ,rfpa_tracker\n\t         ,ychrfpa_tracker\n\t         ,externalrfpa_tracker\n\t) t4\n on t1.ychpageid=t4.ychpageid \nand t1.viewipcityid=t4.viewipcityid \nand t1.clientos=t4.clientos\nand t1.platformtype=t4.platformtype\nand t1.rfpa_tracker=t4.rfpa_tracker\nand t1.ychrfpa_tracker=t4.ychrfpa_tracker\nand t1.externalrfpa_tracker=t4.externalrfpa_tracker\nleft join\n( \nselect ychpageid         -- 易车惠页面标签\n\t   ,platformtype     -- 平台类型1：pc/3：wap\n\t   ,viewipcityid\n\t   ,clientos        -- 客户端系统\n\t   ,rfpa_tracker\n\t   ,ychrfpa_tracker\n\t   ,externalrfpa_tracker\n\t   ,count(distinct cookieid) as visit_again_cnt\nfrom (\n     select ychpageid         -- 易车惠页面标签\n\t       ,platformtype     -- 平台类型1：pc/3：wap\n\t       ,viewipcityid\n\t       ,clientos        \n\t       ,rfpa_tracker\n\t       ,ychrfpa_tracker\n\t       ,externalrfpa_tracker\n\t       ,cookieid\n\t       ,count(distinct viewid) as distinct_viewid\n\t from  yiche_mai.attr_traffic_mai_day\n\t where  pt between date_sub('2018-09-04',180) and '2018-09-04'\n\t group by ychpageid        \n\t         ,platformtype     \n\t         ,viewipcityid\n\t         ,clientos        \n\t         ,rfpa_tracker\n\t         ,ychrfpa_tracker\n\t         ,externalrfpa_tracker\n\t         ,cookieid\n\t union all \n\t select if(b.type='m',888,777)    as ychpageid\n\t       ,platformtype     \n\t       ,viewipcityid\n\t       ,clientos        \n\t       ,rfpa_tracker\n\t       ,ychrfpa_tracker\n\t       ,externalrfpa_tracker\n\t       ,cookieid\n\t       ,count(distinct viewid) as distinct_viewid\n\t from  yiche_mai.attr_traffic_mai_day a\n\t left join yiche_mai.dim_ychpage  b\n\t        on a.ychpageid=b.ychpageid\n\t where  pt between date_sub('2018-09-04',180) and '2018-09-04'\n\t group by if(b.type='m',888,777)    \n\t         ,platformtype    \n\t         ,viewipcityid\n\t         ,clientos       \n\t         ,rfpa_tracker\n\t         ,ychrfpa_tracker\n\t         ,externalrfpa_tracker\n\t         ,cookieid\n) m\nwhere distinct_viewid>=2\ngroup by ychpageid        \n\t     ,platformtype    \n\t     ,viewipcityid\n\t     ,clientos       \n\t     ,rfpa_tracker\n\t     ,ychrfpa_tracker\n\t     ,externalrfpa_tracker\n)t5\n on t1.ychpageid=t5.ychpageid \nand t1.viewipcityid=t5.viewipcityid \nand t1.clientos=t5.clientos\nand t1.platformtype=t5.platformtype\nand t1.rfpa_tracker=t5.rfpa_tracker\nand t1.ychrfpa_tracker=t5.ychrfpa_tracker\nand t1.externalrfpa_tracker=t5.externalrfpa_tracker"
  sql = "create ;table aa;"
  res = _check_hql_has_ddl(sql1);
  print (res)

