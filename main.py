from random import randint as r
print("""
     ╔═══════════════════╗
     ║ CrazyRandomizer69 ║
     ╚═══════════════════╝
     ╔═══════════════════╗
     ║-a(about) -w(start)║
     ╚═══════════════════╝
""")
#start working
inp=input("Input operation>>")
while inp=="-a":
    #about
    print("""
    Github>> CrazyGamer69
    Telegram>> CrazyGamer69
    Telegram channel>> CrazyGamer69_c
    """)
    #repeat input
    inp=input("Input operation>>")
#generate
while inp=="-w":
    f_num=int(input("Input first number>>"))
    s_num=int(input("Input second number>>"))
    winner=r(f_num, s_num)
    print("Winner>>", winner)
    #repeat generation
    inp=input("Input operation>>")
