import socket,random

restart=""
SIZE=1024

while(restart.lower()!="n"):                   
 try:
  TARGET=input("Inserisci l'indirizzo ip target --> ")
  while(1):
   try:
    PORT=int(input("Inserisci numero di porta --> "))
    break
   except:
    print("Errore input! Riprova")

  s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)       #crea socket udp
  data=str(random.getrandbits(SIZE)).encode('UTF-8')      #genera  1024 byte casuali  
  numPacket=int(input("Inserisci il numero di pacchetti da inviare: "))
  for n in range(0,numPacket): 
   s.sendto(data,(TARGET,PORT))                           #invia dati al server
  print("Pacchetti inviati a",TARGET,":",PORT)
  restart=input(" Vuoi Inviare nuovi pacchetti?(S/N))")
  while(restart.lower()!="n" and restart.lower()!="s"): 
   restart=input("Errore! Riprova (S/N)")
  if(restart.lower()=="n"):
   break
 except:
  while(restart.lower()!="n" and restart.lower()!="s"): 
   restart=input("Errore! Vuoi riprovare?(S/N)")
