"""flyos启动入口"""
import os

HOME = os.getenv("HOME")
FLYOS = os.getenv("FLYOS")

os.system("clear")

if not os.path.exists(HOME+"/.flyos/"): # 检测是否已经初始化
    os.system(f"python {FLYOS}/.firstuse/register.py")

os.system('clear')
os.system("python $FLYOS/update.py")
os.system("bash $FLYOS/kernel/boot/bootkernel/bootlogo.sh")
#/data/data/com.termux/files/usr/etc/flyos/kernel/boot/bootkernel/