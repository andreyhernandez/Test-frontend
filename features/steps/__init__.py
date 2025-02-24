import os
import pkgutil
import sys

__all__ = []
PATH = [os.path.dirname(__file__)]

for loader, module_name, is_pkg in pkgutil.walk_packages(PATH):
    __all__.append(module_name)

    if sys.version_info < (3, 10):  # Python 3.8 y 3.9
        _module = loader.find_module(module_name).load_module(module_name)
    else:  # Python 3.10+
        import importlib

        _module = importlib.import_module(f"features.steps.{module_name}")

    globals()[module_name] = _module
