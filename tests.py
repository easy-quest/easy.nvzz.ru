#!/usr/bin/python3                                                                
import requests                                                                   
import time                                                                       
import os                                                                         
os.system('clear')                                                                
time.sleep(4)                                                                     
print('''                                                                         
                +---+---+---+---+---+---+                                              
                | P | y | t | h | o | n |                                              
                +---+---+---+---+---+---+ 
''')                                                                              
                                                                                  
time.sleep(5)                                                                     
os.system("help")                                                                 
                                        
req = requests.get(url)                                                           
src = req.text                                                                    
print(src)

def main():
  url = input("Введите адрес сайта  :  ")

if __name__ == '__main__':
  main()
