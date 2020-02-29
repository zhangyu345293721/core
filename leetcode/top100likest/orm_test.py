# -*- coding:utf-8 -*-
'''
author:zhangyu
date:2020/2/26
'''

# 导入依赖
from io import BytesIO

from PIL import Image
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类
Base = declarative_base()


# 定义User对象
class User(Base):
    # 表的名字
    __tablename__ = 'user'

    # 表的结构
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库链接
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/house')

# 创建DBSession类型
DBSession = sessionmaker(bind=engine)

# 添加
# 创建Session对象
session = DBSession()
# 创建User对象
new_user = User(id='1001', name='james')
# 添加到session
session.add(new_user)
# 提交
session.commit()
# 关闭session
session.close()
'''
# 查询
# 创建session
session = DBSession()
# 利用session创建查询，query(对象类).filter(条件).one()/all()
user = session.query(User).filter(User.id == '1001').one()
print('type:{0}'.format(type(user)))
print('name:{0}'.format(user.name))
# 关闭session
session.close()'''

'''
# 更新
session = DBSession()
user_result = session.query(User).filter_by(id='1001').first()
user_result.name = "durant"
session.commit()
session.close()'''

'''
# 删除
session = DBSession()
user_willdel = session.query(User).filter_by(id='1001').first()
session.delete(user_willdel)
session.commit()
session.close()'''


def converse_bytes_2_picture(algo: bytes) -> None:
    #
    '''
        将bytes转化为图片
    Args:
        algo:比特流
    '''
    # 将bytes结果转化为字节流
    bytes_stream = BytesIO(algo)
    roiimg = Image.open(bytes_stream)
    roiimg.show()
