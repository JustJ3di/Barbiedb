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
## launch server from terminal
$ ``` python run_server.py ip_address port ```


## launch the client
```py
    from Barbie import Client

    c = Client().start()
```


## how value as stored ?
As a json file, after that you give a name to YOUR db whit the command ```set$mydb``` you can store the result with ```store``` in a file name_your_db.json