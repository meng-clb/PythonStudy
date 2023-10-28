# mySql基本使用
sql对大小写不敏感

sql可以多行书写,以分号结尾

## 查看

```sql 
查看所有数据库
show databases;

查看当前使用数据库
select database();

查看数据表
show tables;
```

### sql注释

> 单行注释: "-- 注释内容" "# 注释内容" ""
>
> 多行注释: "/* 注释内容 */"
>
> show
>
> -- 我是注释



### 使用数据库
```sql
use 库名;
use sys;
```


## 创建
```sql
创建数据库
create database 库名 [charset utf8];
create database test charset utf8;

创建数据表 * 创建数据表之前需要先使用数据库
列表类型有:
> int               整数
> float             浮点数
> varchar(长度)     文本,长度为数字,做最大长度限制
> date              日期类型
> timestamp         时间戳类型

create table student(
    id int ,
    name varchar(10),
    age int
);
```

## 删除
```sql
删除数据库
drop database 数据库名;
drop database test;

删除数据表
drop table 表名; * 确定有这个表,否则会报错
drop table student; 

drop table if exists 表名; * 如果有就删除,不会报错
drop table if exists student; 
```




