# Barbiedb

Little db key value database in memory (like redis)
the command are (for now)
set
get
delete
store
clear
name
all this command have to separeted by $

so for example
```set$key$value```

## launch the server
```python
    from Barbie import Server

    s = Server().start()
```
## launch the client
```py
    from Barbie import Client

    c = Client().start()
```