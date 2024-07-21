### Start server command
python proxy.py localhost 21 localhost 9999 True

### Start ftpserver
python3 -m pyftpdlib -p 2121 -u jml -P password

### Connect to ftp-server
ftp localhost 21
