## Tired bot

If your computer or internet is very slow, you may face timeout exceptions, or messages not being sent properly. In this case we call our bot exhausted or tired.
 
You can solve this by overriding the default timeout value.This can be done by passing an optional argument to the `WhatsApp` context manager.

```python
from wappdriver import WhatsApp

with WhatsApp(timeout=100) as bot:
    bot.send('aahnik',  'Exhausted ?')
```
The default value of timeout is 50s ( when you dont pass the argument)

If bot is exhausted, increase timeout.
