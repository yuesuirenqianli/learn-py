import os


def get_cwd():
    return os.getcwd()


def get_abs_path(path):
    return os.path.abspath(path)


def has_exists(path):
    return os.path.exists(path)
