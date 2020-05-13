#Author:Anliu

import os,sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
#/a/b/c/file--/b/
#/a/b/file1c/

from core import main

if __name__ == '__main__':
    main.run()
