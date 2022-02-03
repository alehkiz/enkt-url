import importlib
import pkgutil
from flask import Blueprint, Flask

def register_blueprints(app : Flask):

    for m_info, name, ispkg in pkgutil.iter_modules(__path__):
        module = importlib.import_module(f'{__name__}.{name}')
        if hasattr(module, 'bp'):
            bp = getattr(module, 'bp')
            if isinstance(bp, Blueprint):
                app.register_blueprint(bp)