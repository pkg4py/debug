### debug

* tiny python debugging utility

### Example

* [see example](example.py)

### Usage

* such as `a.py`

```py
debug = Debug('example:debug1')
debug('name: %s, age: %d', 'haoxin', 18)
```

* run with debugging

```bash
DEBUG=example:* python a.py

# or

DEBUG=example:debug* python a.py
```

### License
MIT
