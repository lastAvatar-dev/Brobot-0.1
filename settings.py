import os

DEBUG = os.getenv('DEBUG', False)

if DEBUG:
    print("Debugging Mode!")
    from dotenv import load_dotenv
    from pathlib import Path
    env_path = Path(".") / ".env.debug"
    load_dotenv(dotenv_path=env_path)
    from setting_files._development import *
else:
    print("Running Mode!")
    from setting_files._production import *