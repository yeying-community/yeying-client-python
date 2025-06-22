import uuid


def unicode_encode(name):
    return name.encode("unicode-escape").decode("utf-8")


def unicode_decode(name):
    return name.encode("utf-8").decode("unicode-escape")


def generate_uuid():
    return str(uuid.uuid4())


def is_empty(s):
    return False if s and not s.isspace() else True
