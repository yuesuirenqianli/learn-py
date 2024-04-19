import os


def has_dir(path):
    return os.path.isdir(path)


def has_file(path):
    return os.path.isfile(path)


def get_dir_name(path):
    return os.path.dirname(path)


def get_file_name(path):
    return os.path.basename(path)


def get_cwd():
    return os.getcwd()


def get_abs_path(path):
    return os.path.abspath(path)


def has_exists(path):
    return os.path.exists(path)
