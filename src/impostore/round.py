from lista_partecipanti import distruibisciParole, generaImpostori, listaPartecipanti, ordineGiocatori, parolaDaInserire, paroleGioco
from votazione import contaVoti, controllaImpostori, votazioni

impostore = []

def round():
    global impostore

    '''La funzione permette di andare avanti con i round, inserendo nuove parole sempre riferite
    a quella data all'inzio fino a quando non vengono eliminati tutti gli impostori o la 
    lista dei partecipanti è composta sola da 2 giocatori'''

    #creo un ciclo che permette di andare avanti con i round, inserendo nuove parole sempre riferite a quella data all'inzio
    #i round vanno avanti fino a quando non vengono eliminati tutti gli impostori o la lista dei partecipanti è composta sola da 2 giocatori
    while len(impostore) > 0 and len(lista_partecipanti) > 2:
        lista_parole = parolaDaInserire()
        lista_voti = votazioni()
        lista_eliminati = contaVoti(lista_voti)
        lista_partecipanti = controllaImpostori(lista_eliminati)
    
    
    if len(impostore) == 0:
        print("Hai vinto, hai eliminato tutti gli impostori")
    else:
        print("Hai perso, sono rimasti solo 2 giocatori e uno di loro è un impostore")
    
def gioca():
    global impostore

    '''La funzione permette all'utente di giocare al gioco impostore'''
    
    print("Benvenuto al gioco impostore, il tuo obiettivo è quello di eliminare tutti gli impostori presenti tra i partecipanti"
    "prima che rimangano solo 2 giocatori, uno dei quali è un impostore")

    #creo le variabili in modo che vengano eseguite in ordine tutte le funzioni necessarie per giocare al gioco impostore
    lista_partecipanti = listaPartecipanti()
    parola_scelta = paroleGioco()
    impostore = generaImpostori()
    distribuisci_parola = distruibisciParole(lista_partecipanti, parola_scelta, impostore)
    ordine = ordineGiocatori()
    lista_parole = parolaDaInserire()
    votazione = votazioni()
    conta_voti = contaVoti(votazione)
    controlla_impostori = controllaImpostori(conta_voti)
    round()

if __name__ == "__main__":
    gioca()


    
    