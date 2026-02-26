import random

def listaPartecipanti():
    '''La funzione crea una lista contentente i nomi dei partecipanti'''

    while True:
        numero_partecipanti = int(input("inserisci il numero dei partecipanti:"))

        if numero_partecipanti >= 3 and numero_partecipanti <= 15:
            break

    lista_partecipanti = []
    for i in range(numero_partecipanti):
        nome = str(input("inserisci il tuo nome:"))
        lista_partecipanti.append(nome)

    return lista_partecipanti

lista_nomi = listaPartecipanti()

def paroleGioco():
    '''La funzione crea una lista contenente la parole del gioco'''

    lista_parole_totali = [
    ["astronauta", "ignoto"],
    ["gatto", "mistero"],
    ["pizza", "tondo"],
    ["computer", "mente"],
    ["fiume", "fluido"],
    ["albero", "silenzio"],
    ["sole", "calore"],
    ["luna", "riflesso"],
    ["mare", "infinito"],
    ["montagna", "vetta"],
    ["auto", "traccia"],
    ["bicicletta", "ritmo"],
    ["telefono", "eco"],
    ["libro", "chiave"],
    ["penna", "scivolo"],
    ["cane", "fedeltà"],
    ["uccello", "canto"],
    ["fiore", "fragranza"],
    ["cioccolato", "tentazione"],
    ["tavolo", "radice"],
    ["sedia", "riposo"],
    ["occhiali", "limite"],
    ["orologio", "tic"],
    ["porta", "soglia"],
    ["finestra", "respiro"],
    ["mouse", "traccia"],
    ["tastiera", "sequenza"],
    ["lampada", "bagliore"],
    ["specchio", "eco"],
    ["scarpa", "passo"],
    ["camicia", "pieghe"],
    ["pantaloni", "corda"],
    ["cappello", "ombra"],
    ["ombrello", "goccia"],
    ["zaino", "peso"],
    ["chiave", "segreto"],
    ["bicchiere", "trasparenza"],
    ["piatto", "cerchio"],
    ["coltello", "taglio"],
    ["forchetta", "punti"],
    ["cucchiaio", "rotondo"],
    ["torta", "festa"],
    ["gelato", "freddo"],
    ["caffè", "aroma"],
    ["tè", "foglia"],
    ["latte", "bianco"],
    ["pane", "crosta"],
    ["formaggio", "stagione"],
    ["burro", "morbido"],
    ["uovo", "inizio"],
    ["pesce", "scivolo"],
    ["pollo", "allevato"],
    ["maiale", "rosa"],
    ["mucca", "mugolio"],
    ["cavallo", "stella"],
    ["elefante", "memoria"],
    ["tigre", "strisce"],
    ["leone", "ruggito"],
    ["orso", "iberno"],
    ["lupo", "notte"],
    ["volpe", "astuzia"],
    ["coniglio", "salto"],
    ["cervo", "corna"],
    ["scoiattolo", "noci"],
    ["rana", "salto"],
    ["serpente", "scivolo"],
    ["ape", "alveare"],
    ["farfalla", "metamorfosi"],
    ["mosca", "fastidio"],
    ["zanzara", "sangue"],
    ["coccinella", "fortuna"],
    ["spada", "acciaio"],
    ["scudo", "protezione"],
    ["elmo", "testa"],
    ["armatura", "peso"],
    ["cavaliere", "onore"],
    ["castello", "torre"],
    ["re", "sovrano"],
    ["regina", "strategia"],
    ["principe", "erede"],
    ["principessa", "regale"],
    ["drago", "fuoco"],
    ["strega", "bastone"],
    ["maghetto", "segreto"],
    ["fantasma", "ombra"],
    ["zombie", "camminata"],
    ["vampiro", "notte"],
    ["lupo mannaro", "luna"],
    ["pirata", "tesoro"],
    ["nave", "legno"],
    ["barca", "acqua"],
    ["sub", "profondità"],
    ["pescatore", "canna"],
    ["marinaio", "ancora"],
    ["soldato", "ordine"],
    ["poliziotto", "distretto"],
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
    ["ballerina", "passo"],
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
    ["programmatore", "debug"],
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
    ["volcano", "eruzione"],
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
    ["capitale", "trono"],
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
    ["chiesa", "silenzio"],
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
    ["paracadute", "caduta"],
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
    parola_scelta = random.choice(lista_parole_totali)

    return parola_scelta



def impostore():
    '''La funzione sceglie l'impostore dalla lista dei nomi dei partecipanti'''

    while True:
        numero_impostori = int(input("inserisci il numero degli impostori:"))

        if numero_impostori >=1 and numero_impostori <= 3:
            break
        impostori = []
    
    for x in range(numero_impostori):
        impostore = random.choice(lista_nomi)
        impostori.append(impostore)

    return impostori

def distruibisciParole(lista_partecipanti, parola_scelta):
    '''La funzione distribuisce le parole ai giocatori e agli impostori'''

    parola_impostore = parola_scelta[1]
    parola_giocatori = parola_scelta[0]

    for nome in lista_partecipanti:
        if nome in impostore:
            print(nome, "la tua parola è:", parola_impostore)
        else:
            print(nome, "la tua parola è:", parola_giocatori)
    

def ordineGiocatori():
    '''La funzione stabilisce l'ordine con cui i giocatori inseriscono le parole'''

    lista_nomi.shuffle()

    return lista_nomi



def parolaDaInserire():
    '''La funzione fa inserire a ciascun giocatore una parola'''

    lista_parole = []

    for persona in range(lista_nomi):
        parola = str(input("inserisci una parola:"))
    
        while True:
            if parola == parola:
                print("Questa parola è gia stata inserita da un altro giocatore")
                parola = str(input("inserisci un'altra parola:"))
    
    lista_parole.append(parola)

    return lista_parole







    

