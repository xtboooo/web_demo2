import hashlib


def get_md5_pwd(pwd):
    # 创建md5对象
    md5_obj = hashlib.md5()
    # 传入密码,进行加密
    md5_obj.update(pwd.encode('utf-8'))
    # 盐
    salt = '计金山是DSB'
    # 密码加盐
    md5_obj.update(salt.encode('utf-8'))
    # 返回加密后的密码
    return md5_obj.hexdigest()
