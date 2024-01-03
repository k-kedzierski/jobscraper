import importlib
from typing import Type

from jobscraper.site.base import BaseSite

def dynamic_import(class_name: str) -> Type[BaseSite]:
    module_name = class_name.lower()
    module_path = f"jobscraper.site.{module_name}"

    module = importlib.import_module(name=module_path)

    class_ = getattr(module, class_name)

    return class_