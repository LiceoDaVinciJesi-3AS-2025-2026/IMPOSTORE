import random

def listaPartecipanti():
    '''La funzione crea una lista contentente i nomi dei partecipanti'''

    #creo un ciclo infinito che permette di inserire un numero di partecipanti compreso tra 3 e 15 
    #se il numero è fuori da questo range viene chiesto di inserirlo nuovamente
    while True:
        numero_partecipanti = int(input("inserisci il numero dei partecipanti:"))

        if numero_partecipanti >= 3 and numero_partecipanti <= 15:
            break
    #creo una lista vuota
    lista_partecipanti = []
    #creo un ciclo che permette di inserire i nomi dei partecipanti e li aggiunge alla lista dei partecipanti
    for i in range(numero_partecipanti):
        nome = str(input("inserisci il tuo nome:"))
        lista_partecipanti.append(nome)

    return lista_partecipanti
#salvo la lista dei nomi dei partecipanti in una variabile globale per poterla utilizzare in altre funzioni
lista_nomi = listaPartecipanti()

def paroleGioco():
    '''La funzione crea una lista contenente la parole del gioco'''

    #creo una lista unica di parole, ognuna composta da una parola per i giocatori e una parola per gli impostori
    lista_parole_totali = [
    ["astronauta", "pianeti"],
    ["gatto", "baffi"],
    ["pizza", "legna"],
    ["computer", "diamantini"],
    ["fiume", "acqua"],
    ["albero", "autunno"],
    ["sole", "occhiali"],
    ["luna", "riflesso"],
    ["mare", "estate"],
    ["montagna", "neve"],
    ["auto", "gara"],
    ["bicicletta", "pedoni"],
    ["telefono", "filo"],
    ["libro", "scuola"],
    ["penna", "pasta"],
    ["cane", "padrone"],
    ["uccello", "canto"],
    ["fiore", "profumo"],
    ["cioccolato", "tentazione"],
    ["tavolo", "radice"],
    ["sedia", "riposo"],
    ["occhiali", "gradi"],
    ["orologio", "tic"],
    ["porta", "chiave"],
    ["finestra", "vento"],
    ["mouse", "indicatore"],
    ["tastiera", "lettere"],
    ["lampada", "casa"],
    ["specchio", "eco"],
    ["scarpa", "laccio"],
    ["camicia", "bottoni"],
    ["pantaloni", "cintura"],
    ["cappello", "ombra"],
    ["ombrello", "goccia"],
    ["zaino", "peso"],
    ["chiave", "segreto"],
    ["bicchiere", "liquido"],
    ["piatto", "cerchio"],
    ["coltello", "taglio"],
    ["forchetta", "denti"],
    ["cucchiaio", "brodo"],
    ["torta", "festa"],
    ["gelato", "freddo"],
    ["caffè", "corretto"],
    ["tè", "foglia"],
    ["latte", "bianco"],
    ["pane", "crosta"],
    ["formaggio", "stagione"],
    ["burro", "morbido"],
    ["uovo", "ricetta"],
    ["pesce", "palla"],
    ["pollo", "fast food"],
    ["maiale", "fango"],
    ["mucca", "macchie"],
    ["cavallo", "siena"],
    ["elefante", "memoria"],
    ["tigre", "strisce"],
    ["leone", "agosto"],
    ["orso", "miele"],
    ["lupo", "notte"],
    ["volpe", "astuzia"],
    ["coniglio", "salto"],
    ["cervo", "corna"],
    ["scoiattolo", "noci"],
    ["rana", "salto"],
    ["serpente", "sonagli"],
    ["ape", "alveare"],
    ["farfalla", "metamorfosi"],
    ["mosca", "fastidio"],
    ["zanzara", "sangue"],
    ["coccinella", "fortuna"],
    ["spada", "acciaio"],
    ["scudo", "protezione"],
    ["elmo", "testa"],
    ["armatura", "achille"],
    ["cavaliere", "onore"],
    ["castello", "torre"],
    ["re", "corona"],
    ["regina", "pizza"],
    ["principe", "erede"],
    ["principessa", "ballo"],
    ["drago", "fuoco"],
    ["strega", "mela"],
    ["maghetto", "harry potter"],
    ["fantasma", "lenzuolo"],
    ["zombie", "camminata"],
    ["vampiro", "notte"],
    ["lupo mannaro", "luna"],
    ["pirata", "tesoro"],
    ["nave", "oceano"],
    ["barca", "acqua"],
    ["sub", "profondità"],
    ["pescatore", "canna"],
    ["marinaio", "ancora"],
    ["soldato", "ordine"],
    ["poliziotto", "divisa"],
    ["pompiere", "fiamma"],
    ["medico", "cura"],
    ["infermiere", "turno"],
    ["professore", "cattedra"],
    ["studente", "appunti"],
    ["artista", "tela"],
    ["musicista", "note"],
    ["cantante", "voce"],
    ["attore", "scena"],
    ["regista", "ciak"],
    ["scrittore", "inchiostro"],
    ["poeta", "verso"],
    ["fotografo", "scatto"],
    ["ballerina", "palco"],
    ["chef", "pentola"],
    ["pasticcere", "glassa"],
    ["cuoco", "padella"],
    ["giardiniere", "terra"],
    ["contadino", "seme"],
    ["pilota", "quota"],
    ["astronomo", "stelle"],
    ["scienziato", "esperimento"],
    ["ingegnere", "progetto"],
    ["architetto", "modello"],
    ["meccanico", "olio"],
    ["idraulico", "tubo"],
    ["elettricista", "circuito"],
    ["programmatore", "informatica"],
    ["hacker", "sistema"],
    ["robot", "movimento"],
    ["drone", "volo"],
    ["auto da corsa", "veloce"],
    ["bicicletta da corsa", "strada"],
    ["motocicletta", "corsa"],
    ["camion", "carico"],
    ["treno", "rotaia"],
    ["metro", "sottosuolo"],
    ["aereo", "decollare"],
    ["elicottero", "rotore"],
    ["razzo", "lancio"],
    ["satellite", "orbita"],
    ["astronave", "missione"],
    ["stazione spaziale", "sospesa"],
    ["pianeta", "terra"],
    ["luna", "satellite"],
    ["sole", "stella"],
    ["galassia", "spirale"],
    ["buco nero", "vuoto"],
    ["cometa", "scia"],
    ["asteroide", "corsia"],
    ["cratere", "impatto"],
    ["vulcano", "eruzione"],
    ["terremoto", "scossa"],
    ["uragano", "vento"],
    ["tornado", "vortice"],
    ["tempesta", "tuono"],
    ["neve", "bianco"],
    ["ghiaccio", "rigido"],
    ["lago", "specchio"],
    ["oceano", "profondità"],
    ["spiaggia", "sabbia"],
    ["deserto", "silenzio"],
    ["foresta", "ombra"],
    ["giungla", "verde"],
    ["collina", "pendio"],
    ["valle", "ombra"],
    ["isola", "isolata"],
    ["penisola", "punta"],
    ["città", "rumore"],
    ["villaggio", "piccolo"],
    ["paese", "popolazione"],
    ["capitale", "soldi"],
    ["mercato", "bancarella"],
    ["negozio", "vetrina"],
    ["supermercato", "scaffale"],
    ["ristorante", "piatti"],
    ["bar", "chiacchiere"],
    ["caffetteria", "tazza"],
    ["biblioteca", "silenzio"],
    ["scuola", "campanella"],
    ["università", "lezione"],
    ["ospedale", "cura"],
    ["farmacia", "medicina"],
    ["stazione", "treno"],
    ["aeroporto", "attesa"],
    ["porto", "ancora"],
    ["parco", "gioco"],
    ["giardino", "verde"],
    ["palestra", "sudore"],
    ["stadio", "tifo"],
    ["cinema", "schermo"],
    ["teatro", "sipario"],
    ["museo", "arte"],
    ["galleria", "quadri"],
    ["monumento", "storia"],
    ["chiesa", "croce"],
    ["moschea", "preghiera"],
    ["tempio", "santuario"],
    ["sinagoga", "candela"],
    ["pagoda", "legno"],
    ["tenda", "campeggio"],
    ["rifugio", "montagna"],
    ["capanna", "legno"],
    ["igloo", "ghiaccio"],
    ["yacht", "acqua"],
    ["canoa", "remo"],
    ["kayak", "fiume"],
    ["sci", "discesa"],
    ["snowboard", "freddo"],
    ["slittino", "pista"],
    ["paracadute", "volare"],
    ["alianti", "vento"],
    ["mongolfiera", "aria"],
    ["aquilone", "volo"],
    ["palloncino", "leggerezza"],
    ["festa", "allegria"],
    ["compleanno", "candela"],
    ["matrimonio", "nozze"],
    ["anniversario", "ricordo"],
    ["vacanza", "fuga"],
    ["viaggio", "valigia"],
    ["esame", "ansia"],
    ["interrogazione", "domanda"],
    ["anna", "acqua"],
    ["lavoro", "scrivania"],
    ["ufficio", "documenti"],
    ["azienda", "società"],
    ["fabbrica", "produzione"],
    ["strada", "asfalto"],
    ["autostrada", "velocità"],
    ["ponte", "collegamento"],
    ["galleria", "tunnel"],
    ["semaforo", "attesa"],
    ["incrocio", "scelta"],
    ["rotatoria", "cerchio"],
    ["parcheggio", "auto"],
    ["ascensore", "piano"],
    ["scala", "gradino"],
    ["muro", "barriera"],
    ["recinzione", "confine"],
    ["cancello", "ingresso"],
    ["orto", "verdura"],
    ["frutteto", "albero"],
    ["vigna", "uva"],
    ["piscina", "acqua"]
    ]
    #scelgo una parola a caso dalla lista delle parole totali
    parola_scelta = random.choice(lista_parole_totali)

    return parola_scelta

def impostore(lista_nomi, numero_impostori=1):
    '''La funzione sceglie gli impostori dalla lista dei nomi dei partecipanti'''

    # Validazione del numero di impostori
    if not (1 <= numero_impostori <= 3):
        raise ValueError("Il numero di impostori deve essere compreso tra 1 e 3")

    impostori = []

    # Sceglie a caso gli impostori dalla lista dei partecipanti
    for x in range(numero_impostori):
        impostore = random.choice(lista_nomi)
        impostori.append(impostore)

    return impostori

def distribuisciParole(lista_partecipanti, parola_scelta):
    '''La funzione distribuisce le parole ai giocatori e agli impostori'''
    #creo una variabile che contiene la parola per gli impostori e una variabile che contiene la parola per i giocatori
    parola_impostore = parola_scelta[1]
    parola_giocatori = parola_scelta[0]

    #creo un ciclo che distribuisce la parola per gli impostori a tutti gli impostori e la parola per i giocatori a tutti i giocatori
    for nome in lista_partecipanti:
        if nome in impostore:
            print(nome, "la tua parola è:", parola_impostore)
        else:
            print(nome, "la tua parola è:", parola_giocatori)
    

def ordineGiocatori():
    '''La funzione stabilisce l'ordine con cui i giocatori inseriscono le parole'''

    #mescolo la lista dei nomi dei partecipanti per stabilire l'ordine con cui i giocatori inseriscono le parole
    lista_nomi.shuffle()

    return lista_nomi

def parolaDaInserire(lista_parole_inserite):
    '''La funzione raccoglie una parola per ciascun giocatore'''

    lista_parole = []

    # Per ogni giocatore aggiunge la sua parola alla lista
    for persona in lista_nomi:
        parola = lista_parole_inserite[persona]

        # Controlla che la parola non sia già stata inserita da un altro giocatore
        if parola in lista_parole:
            print(f"{persona} ha inserito una parola già presente, verrà ignorata")
        else:
            lista_parole.append(parola)

    return lista_parole







    

