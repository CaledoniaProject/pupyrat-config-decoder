# Introduction

Extract and decode pupyrat client configuration from generated binary files. Python 2.X is required to run this script.

# Usage

Install required dependency

```
pip2 install -r requirements.txt
```

To dump configuration

```
# ./main.py file1
...
pupyimporter.pupy_add_package(...)
...
import sys
sys.modules.pop('network.conf', '')
import network.conf
LAUNCHER = 'connect'
LAUNCHER_ARGS = ['--host', 'XXXX:XX', '-t', 'ssl']
CONFIGURATION_CID = XXX
DELAYS = [[1, 1000, 2000]]
pupy.cid = CONFIGURATION_CID
debug = False
SCRIPTLETS = ''
```

