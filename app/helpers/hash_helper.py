import hashlib


def hasher(data):
    m = hashlib.md5()
    m.update(str(data).encode())
    return m.hexdigest()
