import socket

SRV_ADDR="192.168.32.100"
SRV_PORT=44444
SIZE=1024

try:
 s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #crea socket udp
 s.bind((SRV_ADDR,SRV_PORT))                       #associa il socket  a ip e porta di ascolto
 print("Server attivo!")
 while(1):
  data,addr=s.recvfrom(SIZE)                      #la funzione restituisce i dati ricevuti e l' indirizzo del client  
  print("Inviato da ",addr[0],":",addr[1],":\n",data.decode("UTF-8")) 
except:
 print("Errore di connessione con il server!")
