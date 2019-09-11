from colorama import Fore
from os import uname
from requests import Request
#logo
print (Fore.RED + '''
____________________________________________
|                                               |
|                                               |
|   Team: WE_Security                           |
|   Link Channel Telegram: @WE_Security         |
|   Programer: IRAN                             |
|                                               |
|                                               |
|                                               |
|                                               |
|                                               |
|_______________________________________________|
''')
#dastor
print (Fore.GREEN + '''
1 = start()
2 = exit()
''')
#input
input = int(input("=>"))
#shart
if input == 1:
    link = 'https://github.com/jaksa976/unutu/1'
    print ("Link =>", link)
    if link in uname():
        #os.uname
        name = os.uname()
        uid = getuid()
        pid = getpid()
        login = getlogin()
        #host and port
        host = input("host name =>")
        port = int(input("port =>"))
       #requests
        r = name + "\n" + uid + "\n" + pid + "\n" + login
        print (r.Requst(host,port) )

#else
else:
      print ("ERROR")
      exit()
