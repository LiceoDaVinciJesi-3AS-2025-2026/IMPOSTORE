from lista_partecipanti import listaPartecipanti
from lista_partecipanti import impostore

lista_partecipanti = listaPartecipanti()
impostori = impostore()

def votazioni():
    '''La funzione permette ai giocatori di decidere chi eliminare'''
    #creo una lista vuota che conterrà i voti dei giocatori
    lista_voti = []
    #creo un ciclo che permette a ciascun giocatore di votare chi eliminare e aggiunge il voto alla lista dei voti
    for giocatore in range(lista_partecipanti):
        vota = str(input("inserisci il nome del giocatore da eliminare:"))
        #creo un ciclo infinito che permette di inserire un nome presente tra i partecipanti
        while True:
            if vota not in lista_partecipanti:
                print("Questo nome non è presente tra i partecipanti")
                vota = str(input("inserisci il nome di un giocatore presente tra i partecipanti:"))
            else:
                break
        #aggiungo il voto alla lista dei voti  
        lista_voti.append(vota)

    return lista_voti

def contaVoti(lista_voti):
    '''La funzione controlla la lista dei voti ed elimina il giocatore che ha ricevuto più voti'''
    #creo una variabile che conterrà il nome del giocatore eliminato, una variabile che conterrà il numero massimo di voti ricevuti e una lista che conterrà i nomi dei giocatori eliminati
    giocatore_eliminato = " "
    massimo_voti = 0
    lista_eliminati = []

    #esamina uno per uno i nomi presenti nella lista dei voti ricevuti
    for nome in lista_voti:
        conteggio_attuale = lista_voti.count(nome)
         #verifica se il numero di voti attuale supera o eguaglia il record precedente
        if conteggio_attuale >= massimo_voti:
            massimo_voti = conteggio_attuale #aggiorna il record del numero massimo di voti ricevuti
            giocatore_eliminato = nome #aggiorna il nome del giocatore eliminato
            lista_eliminati.append(nome) #aggiunge il nome del giocatore eliminato alla lista dei giocatori eliminati

    return lista_eliminati

def controllaImpostori(lista_eliminati):
    ''' La funzione controlla se sono stati eliminati gli impostori'''
    #creo un ciclo che controlla se i giocatori eliminati sono impostori o meno
    for nome in lista_eliminati:
        if nome in impostori:
            print(nome, "era un impostore") #stampa un messaggio che indica che il giocatore eliminato era un impostore
        else:
            print("non sono stati eliminati degli impostori") #stampa un messaggio che indica che non sono stati eliminati degli impostori
        #elimina il giocatore eliminato dalla lista dei partecipanti
        lista_partecipanti.remove(nome)

    return lista_partecipanti 




   