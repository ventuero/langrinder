from importlib import import_module


def import_class(full_path: str):
    module_path, class_name = full_path.rsplit(".", 1)
    module = import_module(module_path)
    return getattr(module, class_name)
