# @name:    Dorks-Searcher
# @repo:    https://github.com/4hs4n
# @author:  4HS4N.HAXOR
# Main-file V2.3

import argparse
from os import system, name 
import os 
import sys
def clear(): 
    return os.system('cls' if os.name == 'nt' else 'clear')

print ("")
A = """             
          /)
         //
.-------| |--------------------------------------------.__
|WMWMWMW| |>>>>>>>>>>>>>>>>>4HS4N.HAXOR>>>>>>>>>>>>>>>>>>>:>
`-------| |--------------------------------------------'^^
         \\
          \) 
          
   Dorks-Searcher CODED BY - 4HS4N.HAXOR

  - PLEASE USE -h FOR ( HELP ) AND START THE TOOLS -
  
    """
print ("")
print(A)

parser = argparse.ArgumentParser("scanner.py",formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("-g","--google", help="google mode", action='store_true' )
parser.add_argument("-s","--scada", help="scada mode ", action='store_true' )
parser.add_argument("-t","--tor", help="Tor mode ", action='store_true' )
parser.add_argument("-p","--proxy", help="Proxy mode ", action='store_true' )


args = parser.parse_args()

if args.google :
 clear() 
 from Modes import Gmode
 
if args.scada :
 clear ()
 from Modes import Scada
 
if args.tor :
 clear ()
 from Modes import Tor
  
if args.proxy :
 clear ()
 from Modes import Proxy

