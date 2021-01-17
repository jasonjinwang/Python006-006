# ORM方式连接 MySQL 数据库
# pip3 install sqlalchemy
#!/usr/bin/python3

from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Float, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

# 打开数据库连接
Base = declarative_base()

class Account_table(Base):
    __tablename__ = 'accountorm'
    account_id = Column(Integer(), primary_key=True, autoincrement=True)
    account_name = Column(String(50), nullable=False, unique=True)
    account_age = Column(Integer(), nullable=False)
    account_birth = Column(DateTime(), default=datetime.now)
    account_sex = Column(String(10), nullable=False)
    account_education = Column(String(20), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)

    def __repr__(self):  # 方便对类进行查看及操作
        return "Account_table(account_id='{self.account_id}', " \
            "account_name={self.account_name})".format(self=self)


# 实例一个引擎
dburl = "mysql+pymysql://root:abc!123@127.0.0.1:3306/testdb?charset=utf8mb4"
engine = create_engine(dburl, echo=True, encoding="utf-8")

Base.metadata.create_all(engine)



