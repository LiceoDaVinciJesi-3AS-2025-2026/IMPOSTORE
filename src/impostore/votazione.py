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


    