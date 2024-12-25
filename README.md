## Description

`throttle` is a Python package that provides a class `Throttle` to control the rate of execution of a block of code. It is useful when you want to print debug messages at a certain rate.

## Example

```python
from throttle import Throttle

throttle = Throttle(1)  # minimum interval is 1 second

while True:
    if throttle:
        print('printing...')
```
