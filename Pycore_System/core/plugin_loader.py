import os
import importlib.util
from core.logger import get_logger

logger = get_logger("PLUGIN")

PLUGIN_DIR = "plugins"

def load_plugin(command_registry: dict):
    if not os.path.exists(PLUGIN_DIR):
        return
    for file in os.listdir(PLUGIN_DIR):
        if file.endswith(".py") and not file.startswith("_"):
            path = os.path.join(PLUGIN_DIR, file)
            name = f"plugin_{file[:-3]}"

            try:
                spec = importlib.util.spec_from_file_location(name, path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                if hasattr(module, "register"):
                    module.register(command_registry)
                    logger.info(f"Loaded plugin: {file}")
                else:
                    logger.warning(f"No register() in {file}")
            except Exception as e:
                logger.error(f"Failed to load plugin: {file}: {e}")