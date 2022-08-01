import os
import time
from colorama import Fore, Back, Style
import itertools
import threading
import sys
import webbrowser



AceAgain = False
clear = lambda: os.system('cls')
clear()
done = False
def animate():
    for c in itertools.cycle(['Made By : AceDommete', ' JOIN : @AceDommete1']):
        if done:
            break
        sys.stdout.write(Fore.CYAN + '\rLoading | '+ Fore.RED + c )
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write('\rMade With <3 By AceDommete')

t = threading.Thread(target=animate)
t.start()

time.sleep(5)
done = True


clear()
clear()
print(Fore.RED + """
                                 .','                                                               
                                 :c':c.                                                             
                                 ;:,:;c.                                                            
                                 'c;oo;c;                                                           
                                  :::Oxc::,.                                                        
                                  .c;lOOdc:;,.                                                      
                                   .c;lOO0xlc:;,'                                                   
                         ...     .,,lx:cxOO0Odllc;,,,'.                                             
                       .c:;;,,'. ,c';ldl:lkOO000kolllc:,,,'.                                        
                       .c;,c:::;,co;ld:c:,;lxOOOO00KKOxollc:;,,,..                                  
                        .::;oxoc;;;.'x0xc:,..,lxO00OO000KKOxolllc;,,'.                              
                          ,c;cxddol;':k00Oxo:,',:cldkO00OOOOO00Okdllc:,,'.                          
                           'l;:ddooc:,:okOOkxxdolc:clodxxkkkkkkOOO00Odlc:;;'                        
                          ';:'.ldollc;,,cdkOkkkxxdddooolllloddxkkOkkOO00xlc::,                      
                       .,:;'.'':ddoooc:;,,:oxkOOkkkkxxxxdddollcloolokOkO00Od:c:.                    
                      ':;'',,,;ldooooolc:;;,;codkOOOkkkkkkxxxxdool,.':dkOO00x;c;                    
                    .::,,::;,;cdddooooolccc::;;;::clxxkkkkkkkkkkxxdc. .,okO00d;:;.                  
                   ,c,;lllcc:;;;:codooollllccccc;,,:ccclodxxkkkkkxdddl;,,cxOO0x:::,.                
                  ;c,:ollllc:;;;,,,:oooolllllccc;;:lollc:::ccloodxxdddddoclxOOOOdcc:,,,,,;,         
                 ;:'coolllc:;;;;:;,';oollllllllc;'':oollllllcccccc:;:cldddlcdkkOO0kdllllc;c;        
                ;c'cdollcc::;::;,,'.,odolllc::;,,'.':lollllooooddol,.;c:::cllodkkkOO00000l;c.       
               'c,:doolc:::::;,'','';cc:;,',;;;;;,,'',:clllooooodddo,cd;,,;::;:oxkkkkO000d;c'       
               :;,odolc::cc;,'',,,,,,,'''..;oolcc::;;'..',;clllodddx:,c'  .,,;:;,cxkkkOO0d;c'       
              ,c'cddlc:ccc,'',,,,,;;,,,'''.,odoll:;,;;;;;,,,,;clloddo,::      ',;;;cxkkOOc;c.       
              :;,ddoc:cc:,'',,,,,;;,;;,,''..ldoc,,:;,'...'',;;,;clodx:,c.        ':;;dkOd,c,        
             .c,:xdlccc:''',,,,,;,,;;;;,,,'.,oo';c;.         ,c,,loddo,:;         .:;:kd;c;         
             'c,lxdlcc;'',,,,,;;;,;:::::;;;'.,,,c.        .',,:,,llodd:,c,         ;:'::c,          
             ,:,oxoll:,,,,,;;;;:,,::clllc:::'.'c;         :c';,;cllloddc,;;,'.     .:;;;.           
             ;:,ddoo:,,;:;;;;;:;';,;llllc::c',l'          .::,;:llllloodo:;;,c'      ..             
             ;:,dddc,,;::;;;;;:,':,.:ooooc:c',c.            ';;;;;;;;;;;;:::;;.                     
             ;:,dxc.';:c:;;;;;:,'::..;looocc,'c'              .',,''',''',,'.                       
             ,:,od, '::cc;;;;::'':c,...:odol:.:;                                                    
             'c,ll'..:ccc:;;;::'';c:'....;loo,'c'                                                   
             .c;:;:d',lcc:;;;::'';cc;''....,:c,,c.                                                  
              ::''ck:'clcc;;;::,';:cc;,'''......::.                                                 
              'c,;c,:;,llc:;;;:,';::cc;;;;;,,,..:c;.                                                
               .,,. .c,;ooc:;;:;',;::llc::::;;;,',::;.                                              
                     'c,:ooc:;::'',::ccolcccc::;;,'',;;'                                            
                      'c,;odl:;:;.',::ccll:;;cccccc:;,,;;;'                                         
                       .c;;odolc:,.',,;:cll:,'.'',,,;;,..,o.                                        
                        .::,ldooo;..'',,;:cllc:,.........':;,.                                      
                          ,:;;odol'.....',,;::cll::;,'.''..';;,,'.                                  
                           .::,:odl':o:;;;,'..'',;::cc::::;;,'.,;;,;'                               
                             .:;;:ol,:l,',,,',,;;;;;;;::::::;;;;,'.;l.                              
                               ';:;:c;;c'      ......'''','''''','''.                               
                                 .;;:;'':;.                                                         
                                   .';;,;l'                                                         
                                      .''.   
""")
time.sleep(1)
print(Fore.CYAN + "\nWelcome To Ace Extrap Maker!! \n")
time.sleep(2)
print(Fore.YELLOW + "\nWhat You Will Need? \n")
time.sleep(2)
print(Fore.GREEN + """
1. A Valid CC (Spammed/Live/Charged)
2. Bin
3. Patience
""")
time.sleep(3)
print(Fore.MAGENTA + "If You Are Done With The Requirements, Take You Bin And \n Generate Some CC Using namso-gen.com \n")
time.sleep(3)
clear()
clear()



def step2(cc1, cc2):
  liststr1 = list(cc1)
  liststr2 = list(cc2)
  a = int(liststr1[9])
  b = int(liststr1[10])
  ms = round(((a + b)/2)*5)
  c = int(liststr2[9])
  d = int(liststr2[10])
  ms2 = round(((c + d)/2)*5)

  msfinal = ms + ms2
  msfinall = str(msfinal)
  liststr1[9] = "x"
  liststr2[9] = "x"
  liststr1[10] = "x"
  liststr2[10] = "x"

  mslist = list(msfinall)

  for i in range(8,10):
    for j in range(0,2):
      liststr1[i] = msfinall[j]
      liststr2[i] = msfinall[j]
  joinedfinal1 = "".join(liststr1)
  joinedfinal2 = "".join(liststr2)
  print(f"\nHere Is Your Extrap : {joinedfinal1}")
  print(f"\nHere Is Your Second Extrap : {joinedfinal2} \n")

  choice = input(Fore.RED + "Do You Want To Make Another Extrap (Y/N)? : ").upper()
  if choice == "Y" or "YES":
    chk()
  else:
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("t.me/acedommete1")
    quit()



def maker(ace1, ace2, ace):
    clear()

    #Ace : For Gen1

    lastfrmgen1 = 0
    lisst = [int(x) for x in str(ace1)]
    s = [str(i) for i in lisst[0:12]]
    lastfrmgen1 = int("".join(s))

    #Ace : For Gen2

    lastfrmgen2 = 0
    lisst = [int(x) for x in str(ace2)]
    s1 = [str(i) for i in lisst[0:12]]
    lastfrmgen2 = int("".join(s1))

    #Ace : For Live

    lastfrmlive = 0
    lisst = [int(x) for x in str(ace)]
    s3 = [str(i) for i in lisst[-4:]]
    lastfrmlive = int("".join(s3))

    sjoinedgen1 = str(lastfrmgen1)
    sjoinedgen2 = str(lastfrmgen2)
    sjoinedlive = str(lastfrmlive)

    joinedgen1 = sjoinedgen1 + sjoinedlive
    joinedgen2 = sjoinedgen2 + sjoinedlive

    clear()

    print(Fore.CYAN + """
           d8888                  8888888b.                                                888            
          d88888                  888  "Y88b                                               888            
         d88P888                  888    888                                               888            
        d88P 888  .d8888b .d88b.  888    888  .d88b.  88888b.d88b.  88888b.d88b.   .d88b.  888888 .d88b.  
       d88P  888 d88P"   d8P  Y8b 888    888 d88""88b 888 "888 "88b 888 "888 "88b d8P  Y8b 888   d8P  Y8b 
      d88P   888 888     88888888 888    888 888  888 888  888  888 888  888  888 88888888 888   88888888 
     d8888888888 Y88b.   Y8b.     888  .d88P Y88..88P 888  888  888 888  888  888 Y8b.     Y88b. Y8b.     
    d88P     888  "Y8888P "Y8888  8888888P"   "Y88P"  888  888  888 888  888  888  "Y8888   "Y888 "Y8888

                                ----> Do Join @AceDommete1 On Telegram!!! <----
    """)
    print(Fore.MAGENTA + "")
    listgen1 = list(joinedgen1)
    listgen1[7] = "x"
    listgen1[9] = "x"
    listgen1[11] = "x"
    listgen1joined = "".join(listgen1)

    listgen2 = list(joinedgen2)
    listgen2[7] = "x"
    listgen2[9] = "x"
    listgen2[11] = "x"
    listgen2joined = "".join(listgen2)

    print(f"\n\nBasic Extrapped CC 1 : {listgen1joined} \n")
    time.sleep(1)
    print(Fore.BLUE + "")
    print(f"Basic Extrapped CC 2 : {listgen2joined} \n")

    print(Fore.RED + "Now We Can Proceed, \n")
    print(Fore.CYAN + "Copy These And Generate CC Using Them \n")
    time.sleep(1)
    print(Fore.RED + "Opening CC Gen  <3 \n")
    time.sleep(3)
    webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("namso-gen.com")
    print("\n")
    sgen1 = input(Fore.CYAN + "Enter Any CC Number From The Extrap I Gave You To Generate : ")
    sgen2 = input(Fore.CYAN + "Enter Any Other CC Number From The Other Extrap I Gave You : ")
    sgen1list = list(sgen1)
    sgen2list = list(sgen2)
    for digit in sgen1list[-5:]:
      for i in  range(11, 16):
        sgen1list[i] = "x"
    sgen1list[8] = "x"
    stringnew = "".join(sgen1list)

    for digit in sgen2list[-5:]:
      for i in  range(11, 16):
        sgen2list[i] = "x"
    sgen2list[8] = "x"
    stringnew2 = "".join(sgen2list)
    step2(stringnew, stringnew2)

    

def chk():
    clear()
    print(Fore.CYAN + """
           d8888                  8888888b.                                                888            
          d88888                  888  "Y88b                                               888            
         d88P888                  888    888                                               888            
        d88P 888  .d8888b .d88b.  888    888  .d88b.  88888b.d88b.  88888b.d88b.   .d88b.  888888 .d88b.  
       d88P  888 d88P"   d8P  Y8b 888    888 d88""88b 888 "888 "88b 888 "888 "88b d8P  Y8b 888   d8P  Y8b 
      d88P   888 888     88888888 888    888 888  888 888  888  888 888  888  888 88888888 888   88888888 
     d8888888888 Y88b.   Y8b.     888  .d88P Y88..88P 888  888  888 888  888  888 Y8b.     Y88b. Y8b.     
    d88P     888  "Y8888P "Y8888  8888888P"   "Y88P"  888  888  888 888  888  888  "Y8888   "Y888 "Y8888

                                ----> Do Join @AceDommete1 On Telegram!!! <----
    """)
    gen1 = int(input(Fore.RED + "Enter The First Generated CC Number (Only CC Number) : \033[1;32;40m"))
    gen2 = int(input(Fore.RED + "Enter The Second Generated CC Number (Only CC Number) :\033[1;32;40m "))
    livecc = int(input("\033[1;32;40mEnter Any Live CC Number : \033[38;2;255;255;255m"))
    if len(str(gen1)) < 16 or len(str(gen1)) > 16 and len(str(gen2)) < 16 or len(str(gen2)) > 16 and len(str(livecc)) < 16 or len(str(livecc)) > 16:
        clear()
        print("Bruh! Enter Valid CC Numbers...")
        time.sleep(2)
        clear()
        global AceAgain
        AceAgain = True
    else :
        maker(gen1, gen2, livecc)
    while AceAgain==True:
        chk()
    
chk()