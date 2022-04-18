import os
import sys
def someTest():
    print("some test");


ROOT_DIR = os.path.abspath(os.curdir);
print(ROOT_DIR);

from pathlib import Path

print(str(Path.home()))
