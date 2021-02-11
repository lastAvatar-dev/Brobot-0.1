import os

DEBUG = os.getenv('DEBUG', False)

if DEBUG:
    print("Debugging Mode!")
    from dotenv import load_dotenv
    load_dotenv()
    from setting_files._development import *
else:
    print("Running Mode!")
    from dotenv import load_dotenv
    load_dotenv()
    from setting_files._production import *