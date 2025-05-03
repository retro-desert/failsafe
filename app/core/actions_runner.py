"""Actions runner"""
import importlib
import inspect
import pkgutil

from app.core.base import Action
from app.core.container import Container


class ActionRunner:
    """Run actions"""
    def __init__(self, container: Container):
        self.container = container
        self.log = container.logger(__name__)
        self.actions = discover_actions()

    def run_all(self):
        """Run all actions"""
        self.log.warning("Failsafe triggered. Executing actions...")
        for action in self.actions:
            try:
                action.run()
            except Exception as err:
                self.log.error("%s: %s", action.__class__.__name__, err)


def discover_actions():
    """Discover actions to run"""
    actions = []
    for _, module_name, _ in pkgutil.iter_modules(["app/actions"]):
        if module_name == "base":
            continue

        module = importlib.import_module(f"app.actions.{module_name}")
        for _, obj in inspect.getmembers(module, inspect.isclass):
            if issubclass(obj, Action) and obj is not Action:
                actions.append(obj())
    return actions
