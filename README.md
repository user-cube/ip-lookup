# IP Lookup Tool
Get easily information about an IP Address.

## Install
It's possible to use this tool in Windows or Unix.

### Unix

```shell
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements
```

### Windows

```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## How to use
First you need to download [MaxMind databases](https://www.maxmind.com/en/home).
After the download is complete you need to set your database path.

### Unix
```shell
$ export DATABASE_PATH=/path/to/database
```

### Windows (cmd)
```shell
set DATABASE_PATH=/path/to/database
```

## Execute IP Lookup Tool
You can search for only one IP or a list of IPs.

### Single Search
```shell
$ python main.py --ips "8.8.8.8"
```

### List Search
```shell
$ python main.py --ips "8.8.8.8 8.8.4.4"
```