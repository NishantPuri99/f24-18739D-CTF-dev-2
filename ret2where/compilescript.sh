gcc -m32 -fno-stack-protector -z execstack -no-pie -Wno-implicit-function-declaration -o ret2win ret2win.c
chmod +x ret2win