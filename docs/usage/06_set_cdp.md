## Set Chrome Driver Path

When you will use `wappdriver` for the first time, it will ask you to input the path of Chrome Driver Executable in your system.

You can set the path programmatically 
```python
from wappdriver import set_chrome_driver_path
path = '/home/aahnik/Downloads/chrome_driver' 
set_chrome_driver_path(path)
```

**Replace the value of variable `path` with the path of chrome driver in your system.**