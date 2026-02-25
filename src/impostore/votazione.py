from lista_partecipanti import listaPartecipanti
from lista_partecipanti import impostore

lista_partecipanti = listaPartecipanti()
impostori = impostore()

def votazioni():
    '''La funzione permette ai giocatori di decidere chi eliminare'''

    lista_voti = []

    for giocatore in range(lista_partecipanti):
        vota = str(input("inserisci il nome del giocatore da eliminare:"))
        
        while True:
            if vota not in lista_partecipanti:
                print("Questo nome non è presente tra i partecipanti")
                vota = str(input("inserisci il nome di un giocatore presente tra i partecipanti:"))
            else:
                break
            
        lista_voti.append(vota)

    return lista_voti

def contaVoti(lista_voti):
    '''La funzione controlla la lista dei voti ed elimina il giocatore che ha ricevuto più voti'''

    giocatore_da_eliminare = ""
    massimo_voti = 0
    lista_eliminati = []

    for nome in lista_voti:
        conteggio_attuale = lista_voti.count(nome)
        
        if conteggio_attuale >= massimo_voti:
            massimo_voti = conteggio_attuale
            giocatore_da_eliminare = nome

    while giocatore_da_eliminare in lista_voti:
        lista_voti.remove(giocatore_da_eliminare)
        lista_eliminati.append(giocatore_da_eliminare)

    
    return lista_eliminati

def controllaImpostori(lista_eliminati):
    ''' La funzione controlla se sono stati eliminati gli impostori'''

    for nome in lista_eliminati:
        if nome in impostori:
            print(nome, "era un impostore")
        else:
            print("non sono stati eliminati degli impostori")
    
        lista_partecipanti.remove(nome)

    return lista_partecipanti




   