- Log in: https://www.pythonanywhere.com
- git clone https://github.com/basu-asesh/pythonanywhere_demo.git
- mv pythonanywhere_demo mysite

## OPTIONAL
- Update WSGI config
- Edit /var/www/usab_pythonanywhere_com_wsgi.py.
- Change the import to match your file:



```python
import sys
import os

project_home = '/home/usab/mysite'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from my_app import app as application   # ✅ use the actual filename!
```

