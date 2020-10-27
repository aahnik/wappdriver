## Update Variables 

When you run `wappdriver` for the first time, the values of selectors is fetched from the internet.

If you want to update them
```python
from wappdriver import update_vars
update_vars()
```
If any new updates are availaible, they will be downloaded.