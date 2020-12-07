import hashlib


def get_md5_pwd(pwd):
    md5_obj = hashlib.md5()
    md5_obj.update(pwd.encode('utf-8'))
    salt = '计金山是DSB'
    md5_obj.update(salt.encode('utf-8'))
    return md5_obj.hexdigest()
