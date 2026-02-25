from lista_partecipanti import listaPartecipanti

lista_partecipanti = listaPartecipanti()

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

    for nome in lista_voti:
        conteggio_attuale = lista_voti.count(nome)
        
        if conteggio_attuale >= massimo_voti:
            massimo_voti = conteggio_attuale
            giocatore_da_eliminare = nome

    while giocatore_da_eliminare in lista_voti:
        lista_voti.remove(giocatore_da_eliminare)

    
    return lista_voti



   