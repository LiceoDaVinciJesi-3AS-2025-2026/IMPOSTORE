#========================================================================
# FILE GESTIONE GRAFICA --> funzioni per visualizzare il gioco
#========================================================================

import pygame
import sys
import random

# la lista parole viene importata dal file esterno lista_parole.py
# se la funzione si chiama diversamente, cambia 'paroleGioco' con il nome corretto
try:
    import lista_parole
    USA_FILE_PAROLE = True
except ImportError:
    USA_FILE_PAROLE = False

# richiama tutte le funzioni di pygame
pygame.init()

#========================================================================
# --------------------------- COLORI E FONT ----------------------------
#========================================================================

COLORE_titolo = (30, 255, 255)               # turchese elettrico
COLORE_pulsante = (40, 40, 80)               # blu notte scuro
COLORE_pulsante_sovrapposto = (70, 70, 130)  # blu medio-scuro
COLORE_pulsante_bordo = (100, 100, 200)      # blu elettrico soft
COLORE_testo = (255, 255, 255)               # bianco
COLORE_testo2 = (20, 20, 60)
COLORE_testo3 = (200, 60, 60)
COLORE_testo4 = (160, 50, 50)

FONT_titolo = pygame.font.SysFont("Arial", 90, bold=True)
FONT_testo = pygame.font.SysFont("Arial", 32)
FONT_piccolo = pygame.font.SysFont("Arial", 22)
font_nome = pygame.font.SysFont("Arial", 24, bold=True)
font_x = pygame.font.SysFont("Arial", 20, bold=True)

#========================================================================
# FINESTRA PRINCIPALE --> impostazioni generali e pulsanti
#========================================================================

LARGHEZZA, ALTEZZA = 800, 600
schermata = pygame.display.set_mode((LARGHEZZA, ALTEZZA))
pygame.display.set_caption('IMPOSTORE')

# adattamento dello sfondo
sfondo = pygame.image.load("sfondo_ridimensionato.jpg")
immagine_sfondo = pygame.transform.scale(sfondo, (LARGHEZZA, ALTEZZA))

foto_originale = pygame.image.load("RondoDaSosa_2.jpg")
foto = pygame.transform.scale(foto_originale, (280, 280))

# posizione e forma dei pulsanti nella finestra
PULSANTE_larghezza, PULSANTE_altezza = 300, 70
PULSANTE_1 = pygame.Rect(LARGHEZZA // 2 - PULSANTE_larghezza // 2, 300, PULSANTE_larghezza, PULSANTE_altezza)
PULSANTE_2 = pygame.Rect(LARGHEZZA // 2 - PULSANTE_larghezza // 2, 410, PULSANTE_larghezza, PULSANTE_altezza)

# variabili globali per la gestione dei giocatori
nome_corrente = ""
giocatore_corrente = 0
nomi_giocatori = []
numero_giocatori = 15
scroll_lista = 0

# variabili globali per la gestione della partita
# è un tipo di variabile dichiarata fuori da tutte le funzioni, quindi accessibile e modificabile da qualsiasi punto del codice
ordine_giocatori = []
indice_giocatore_corrente = 0
parola_partita = ""        # parola per i giocatori normali --> coppia[0] presa da lista_parole
parola_indizio = ""        # indizio per l'impostore --> coppia[1] presa da lista_parole
nomi_impostori = []        # lista con i nomi degli impostori (1, 2 o 3 a seconda del numero di giocatori)
coperta_y = 0
coperta_trascinando = False
coperta_offset = 0

# variabili globali per la schermata ordine di gioco
indice_ordine_gioco = 0    # tiene traccia di quale giocatore deve dire la parola in questo momento

# variabili globali per la schermata votazioni
indice_votante = 0                  # tiene traccia di quale giocatore sta votando in questo momento
voti = {}                           # dizionario {nome: numero_voti_ricevuti}
scroll_votazioni = 0                # scroll della tendina nella schermata votazioni
risultato_eliminazione = ""         # stringa con il risultato: 'IMPOSTORE ELIMINATO' o 'NESSUN IMPOSTORE ELIMINATO'
giocatori_eliminati = []            # lista dei giocatori eliminati durante la partita (impostori e non)


#========================================================================
# LISTA PAROLE DI RISERVA --> usata se lista_parole.py non è disponibile
# ogni elemento è una lista di due parole:
#   - [0] --> parola per i giocatori normali
#   - [1] --> indizio per l'impostore
#========================================================================

lista_parole_riserva = [
    ["astronauta", "pianeti"], ["gatto", "baffi"], ["pizza", "legna"],
    ["computer", "diamantini"], ["fiume", "acqua"], ["albero", "autunno"],
    ["sole", "occhiali"], ["luna", "riflesso"], ["mare", "estate"],
    ["montagna", "neve"], ["auto", "gara"], ["telefono", "filo"],
]


#========================================================================
# FUNZIONI --> generazione dei pulsanti
#========================================================================

def disegna_pulsanti(forma, testo, sovrapposizione_mouse):
    '''Questa funzione permette di disegnare dei pulsanti nelle varie schermate
       Prende come parametri:
          - forma --> definisce un rettangolo
          - testo --> incolla la scritta sopra il pulsante
          - sovrapposizione_mouse --> verifica la posizione del corsore del mouse
    '''
    # il pulsante è di colore blu notte scuro nelle condizioni normali
    # se il mouse si trova sopra il pulsante, diventa blu notte soft
    colore_pulsante_finestra = COLORE_pulsante_sovrapposto if sovrapposizione_mouse else COLORE_pulsante

    # funzione (dove_disegnare, colore, forma, angoli_smussati)
    pygame.draw.rect(schermata, colore_pulsante_finestra, forma, border_radius=12)
    pygame.draw.rect(schermata, COLORE_pulsante_bordo, forma, width=2, border_radius=12)

    # funzione che trasforma il testo in un immagine
    # funzione (testo, antialiasing: rende lettere più smussate, colore)
    testo = FONT_testo.render(testo, True, COLORE_testo)

    # prende le dimensioni del rettangolo e incolla il testo al centro
    schermata.blit(testo, testo.get_rect(center=forma.center))


#========================================================================
# FUNZIONE --> gestisce le variabili globali
#========================================================================

def inizia_partita():

    # dichiara che le variabili che verranno modificate sono quelle globali dichiarate in cima al file, non copie locali
    global ordine_giocatori, indice_giocatore_corrente
    global nomi_impostori, coperta_y, coperta_trascinando
    global parola_partita, parola_indizio
    global indice_ordine_gioco, voti, indice_votante, risultato_eliminazione

    ordine_giocatori = nomi_giocatori[:]
    random.shuffle(ordine_giocatori)

    # determina il numero di impostori in base al numero di giocatori:
    #   - 3 fino a 6 giocatori  --> 1 impostore
    #   - 6 fino a 10 giocatori --> 2 impostori
    #   - 11 fino a 15 giocatori --> 3 impostori
    n = len(nomi_giocatori)
    if n <= 6:
        numero_impostori = 1
    elif n <= 10:
        numero_impostori = 2
    else:
        numero_impostori = 3

    # sceglie a caso i nomi degli impostori dalla lista dei giocatori senza ripetizioni
    nomi_impostori = random.sample(ordine_giocatori, numero_impostori)

    indice_giocatore_corrente = 0
    indice_ordine_gioco = 0
    indice_votante = 0
    coperta_y = 0
    coperta_trascinando = False
    risultato_eliminazione = ""

    # azzera i voti per tutti i giocatori
    voti = {nome: 0 for nome in ordine_giocatori}

    # sceglie una coppia di parole a caso
    # coppia[0] --> parola per i giocatori normali
    # coppia[1] --> indizio per l'impostore
    if USA_FILE_PAROLE:
        lista = lista_parole.paroleGioco()
    else:
        lista = lista_parole_riserva
    coppia = random.choice(lista)
    parola_partita = coppia[0]
    parola_indizio = coppia[1]


def nuovo_round():
    '''Resetta le variabili per iniziare un nuovo round mantenendo i giocatori rimasti'''
    global indice_giocatore_corrente, indice_ordine_gioco, indice_votante
    global coperta_y, coperta_trascinando, risultato_eliminazione
    global ordine_giocatori, nomi_impostori, voti
    global parola_partita, parola_indizio

    # aggiorna l'ordine dei giocatori rimuovendo quelli eliminati
    ordine_giocatori = nomi_giocatori[:]
    random.shuffle(ordine_giocatori)

    # ricalcola gli impostori tra i giocatori rimasti
    n = len(nomi_giocatori)
    if n <= 6:
        numero_impostori = 1
    elif n <= 10:
        numero_impostori = 2
    else:
        numero_impostori = 3

    # non si possono avere più impostori dei giocatori rimasti
    numero_impostori = min(numero_impostori, len(nomi_giocatori) - 1)
    nomi_impostori = random.sample(ordine_giocatori, numero_impostori)

    indice_giocatore_corrente = 0
    indice_ordine_gioco = 0
    indice_votante = 0
    coperta_y = 0
    coperta_trascinando = False
    risultato_eliminazione = ""

    # azzera i voti per tutti i giocatori rimasti
    voti = {nome: 0 for nome in ordine_giocatori}

    # sceglie una nuova coppia di parole
    if USA_FILE_PAROLE:
        lista = lista_parole.paroleGioco()
    else:
        lista = lista_parole_riserva
    coppia = random.choice(lista)
    parola_partita = coppia[0]
    parola_indizio = coppia[1]


#========================================================================
# FUNZIONI --> generazione delle finestre
#========================================================================

def disegna_finestra_principale():
    '''Questa funzione disegna la finestra principale che si visualizza quando avvi il gioco'''

    # incolla l'immagine nello sfondo
    schermata.blit(sfondo, (0, 0))

    # genera le scritte e le incolla nella schermata
    titolo = FONT_titolo.render("IMPOSTORE", True, COLORE_titolo)
    schermata.blit(titolo, titolo.get_rect(centerx=LARGHEZZA // 2, top=80))
    testo_piccolo = FONT_piccolo.render("Chi è l'impostore tra voi?", True, COLORE_testo)
    schermata.blit(testo_piccolo, testo_piccolo.get_rect(centerx=LARGHEZZA // 2, top=195))

    # ritornano le coordinate del mouse in un preciso istante --> ritorna una tupla (x, y)
    posizione_mouse = pygame.mouse.get_pos()

    # disegnano i pulsanti secondo la funzione già definita
    # la funzione ".collidepoint()" ritorna True se il mouse si trova sopra l'area del pulsante
    disegna_pulsanti(PULSANTE_1, "Nuova Partita", PULSANTE_1.collidepoint(posizione_mouse))
    disegna_pulsanti(PULSANTE_2, "Impostazioni", PULSANTE_2.collidepoint(posizione_mouse))

    # aggiorna la schermata
    pygame.display.flip()


def disegna_finestra_impostazioni():
    '''Questa funzione disegna una schermata chiamata IMPOSTAZIONI'''

    # incolla l'immagine nello sfondo
    schermata.blit(sfondo, (0, 0))

    # genera il testo e lo centra rispetto a tutta la schermata
    messaggio_impostazioni = FONT_testo.render("Qui ci saranno le impostazioni...", True, COLORE_testo)
    schermata.blit(messaggio_impostazioni, messaggio_impostazioni.get_rect(center=(LARGHEZZA // 2, ALTEZZA // 2)))

    # aggiorna la schermata
    pygame.display.flip()


def disegna_schermata_inizio_partita():
    '''Questa funzione disegna una schermata con due pulsanti
          - NOMI GIOCATORI compare subito
          - INIZIA compare quando hai inserito almeno 3 nomi
    '''

    # incolla l'immagine sullo schermo
    schermata.blit(sfondo, (0, 0))

    # genera il titolo e lo incolla centrato nella pagina in alto
    titolo_inizio_partita = FONT_titolo.render("INIZIO PARTITA", True, COLORE_titolo)
    schermata.blit(titolo_inizio_partita, titolo_inizio_partita.get_rect(centerx=LARGHEZZA // 2, top=80))

    # vengono definite le coordinate del mouse
    posizione_mouse = pygame.mouse.get_pos()

    # viene generato il pulsante e centrato nello schermo
    PULSANTE_NOMI = pygame.Rect(LARGHEZZA // 2 - PULSANTE_larghezza // 2, 300, PULSANTE_larghezza, PULSANTE_altezza)
    disegna_pulsanti(PULSANTE_NOMI, "NOMI GIOCATORI", PULSANTE_NOMI.collidepoint(posizione_mouse))

    # il secondo pulsante compare solo quando la lista dei giocatori è maggiore di 3
    # infatti il gioco funziona solo quando partecipano più di tre giocatori
    if len(nomi_giocatori) >= 3:
        PULSANTE_INIZIA = pygame.Rect(LARGHEZZA // 2 - PULSANTE_larghezza // 2, 390, PULSANTE_larghezza, PULSANTE_altezza)
        disegna_pulsanti(PULSANTE_INIZIA, "INIZIA", PULSANTE_INIZIA.collidepoint(posizione_mouse))

    # aggiorna la schermata
    pygame.display.flip()


def disegna_finestra_nomi_giocatori():
    '''Questa funzione gestisce tutto il meccanismo di inserimento dei nomi dei giocatori'''

    # incolla la foto sullo schermo
    schermata.blit(sfondo, (0, 0))

    # genera l'immagine del titolo
    titolo_nomi_giocatori = FONT_titolo.render("NOMI GIOCATORI", True, COLORE_titolo)
    schermata.blit(titolo_nomi_giocatori, titolo_nomi_giocatori.get_rect(centerx=LARGHEZZA // 2, top=30))

    # ritorna la tupla con le coordinate del mouse
    posizione_mouse = pygame.mouse.get_pos()

    # visualizza il numero di partecipanti che hanno inserito il nome nel gioco
    etichetta = FONT_piccolo.render(f"Giocatore {len(nomi_giocatori) + 1}:", True, COLORE_testo)
    schermata.blit(etichetta, (50, 155))

    # crea il rettangolo per l'inserimento dei nomi dei giocatori
    input_box = pygame.Rect(50, 185, 280, 55)
    pygame.draw.rect(schermata, COLORE_pulsante, input_box, border_radius=10)
    pygame.draw.rect(schermata, COLORE_pulsante_bordo, input_box, width=2, border_radius=10)

    # visualizza il testo che l'utente sta scrivendo all'interno del rettangolo
    # centra il testo in modo che non tocchi il bordo del rettangolo
    testo_input = FONT_testo.render(nome_corrente, True, COLORE_testo)
    schermata.blit(testo_input, testo_input.get_rect(midleft=(input_box.x + 12, input_box.centery)))

    # genera il secondo pulsante che permette di aggiungere alla lista il nome inserito nella casella di input
    pulsante_aggiungi = pygame.Rect(50, 260, 280, 55)
    disegna_pulsanti(pulsante_aggiungi, "AGGIUNGI", pulsante_aggiungi.collidepoint(posizione_mouse))

    # se hai inserito almeno tre nomi dei giocatori, compare anche il tasto di CONFERMA che fa iniziare il gioco
    if len(nomi_giocatori) >= 3:
        pulsante_conferma = pygame.Rect(50, 340, 280, 55)
        disegna_pulsanti(pulsante_conferma, "CONFERMA", pulsante_conferma.collidepoint(posizione_mouse))

    # puoi inserire il nome alla lista anche cliccando sul tasto invio
    # questa dinamica viene gestita nel LOOP in fondo
    hint = FONT_piccolo.render("INVIO per aggiungere", True, (160, 160, 200))
    schermata.blit(hint, (50, 430))

    # viene renderizzato un rettangolo nella parte destra della schermata
    lista_box = pygame.Rect(420, 130, 340, 420)
    pygame.draw.rect(schermata, (20, 20, 50), lista_box, border_radius=14)
    pygame.draw.rect(schermata, COLORE_pulsante_bordo, lista_box, width=2, border_radius=14)

    # nella parte alta del rettangolo viene indicato il numero di giocatori che hanno inserito il nome nella lista
    titolo_lista = FONT_piccolo.render(f"Giocatori inseriti: {len(nomi_giocatori)}", True, (160, 160, 200))
    schermata.blit(titolo_lista, (lista_box.x + 10, lista_box.y + 10))

    # viene definita l'altezza della casella che contiene il nome
    ALTEZZA_CASELLA = 58
    # calcolo dello spazio che occuperebbero tutte le caselle
    contenuto_totale = len(nomi_giocatori) * ALTEZZA_CASELLA
    area_visibile = lista_box.height - 45

    # calcola fino a quanti pixel puoi scendere al massimo
    # se ci sono meno caselle dello spazio disponibile, non c'è possibilità di scorrere in basso
    max_scroll = max(0, contenuto_totale - area_visibile)
    scroll_lista_clampato = max(0, min(scroll_lista, max_scroll))

    # Crea una lista vuota che raccoglierà le posizioni dei pulsanti X di ogni casella nome
    # Viene poi restituita dalla funzione e usata nel loop per rilevare i click sulle X.
    rects_x = []
    clip_area = pygame.Rect(lista_box.x, lista_box.y + 40, lista_box.width, lista_box.height - 45)
    # tutte le caselle in più che normalmente uscirebbero del rettangolo principale vengono ritagliate in modo che non escano dalla sua area
    schermata.set_clip(clip_area)

    # questo ciclo scorre la lista dei nomi
    # ENUMERATE fornisce sia l'indice numerico 'i' (0, 1, 2...) che il valore nome ad ogni iterazione
    for i, nome in enumerate(nomi_giocatori):

        # Calcola la posizione verticale di ogni casella e scorre tutte le caselle verso l'alto
        casella_y = lista_box.y + 45 + i * ALTEZZA_CASELLA - scroll_lista_clampato
        casella = pygame.Rect(lista_box.x + 10, casella_y, lista_box.width - 20, 48)

        # Controlla se il mouse è sopra la casella e sceglie il colore: più chiaro se hover, leggermente più scuro altrimenti
        # è lo stesso meccanismo che ho usato nella funzione che definisce i pulsanti
        hover_casella = casella.collidepoint(posizione_mouse)
        colore_finale = (220, 220, 245) if hover_casella else (200, 200, 230)

        # disegna prima il rettangolo pieno biancastro, poi il bordo blu elettrico sopra, entrambi con angoli arrotondati
        pygame.draw.rect(schermata, colore_finale, casella, border_radius=8)
        pygame.draw.rect(schermata, COLORE_pulsante_bordo, casella, width=2, border_radius=8)

        # Genera e incolla il nome del giocatore allineato a sinistra dentro la casella
        testo_nome = font_nome.render(nome, True, COLORE_testo2)
        schermata.blit(testo_nome, testo_nome.get_rect(midleft=(casella.x + 12, casella.centery)))

        # crea, colora e disegna il pulsante rosso con la X a destra della casella, poi salva la sua posizione nella lista per rilevare i click
        x_rect = pygame.Rect(casella.right - 40, casella.y + 8, 32, 32)
        hover_x = x_rect.collidepoint(posizione_mouse)
        colore_x = COLORE_testo3 if hover_x else COLORE_testo4
        pygame.draw.rect(schermata, colore_x, x_rect, border_radius=6)
        testo_x = font_x.render("X", True, (255, 255, 255))  # bianco lucente
        schermata.blit(testo_x, testo_x.get_rect(center=x_rect.center))
        rects_x.append(x_rect)

    schermata.set_clip(None)

    # Controlla se serve la barra di scorrimento, cioè solo quando i nomi sono troppi per stare tutti visibili
    if contenuto_totale > area_visibile and max_scroll > 0:

        # Calcola l'altezza e la posizione verticale della barra: più nomi ci sono più è piccola, e si sposta in basso man mano che scorri
        barra_h = int(area_visibile * (area_visibile / contenuto_totale))
        barra_y = lista_box.y + 45 + int(scroll_lista_clampato / max_scroll * (area_visibile - barra_h))

        # Crea e disegna la barretta di scorrimento sul bordo destro del rettangolo lista.
        barra = pygame.Rect(lista_box.right - 10, barra_y, 6, barra_h)
        pygame.draw.rect(schermata, COLORE_pulsante_bordo, barra, border_radius=3)

    # Aggiorna la schermata mostrando tutto ciò che è stato disegnato
    pygame.display.flip()

    # Restituisce la lista con le posizioni di tutte le X, così il loop principale può rilevare i click su di esse
    return rects_x


def disegna_schermata_gioco():
    '''Questa funzione permette di disegnare la schermata di gioco.
       - i giocatori normali vedono parola_partita --> coppia[0]
       - gli impostori vedono "IMPOSTORE" + parola_indizio --> coppia[1]
    '''

    schermata.blit(sfondo, (0, 0))

    titolo = FONT_titolo.render("IMPOSTORE", True, COLORE_titolo)
    schermata.blit(titolo, titolo.get_rect(centerx=LARGHEZZA // 2, top=30))

    nome_attuale = ordine_giocatori[indice_giocatore_corrente]
    posizione_mouse = pygame.mouse.get_pos()

    # colonna sinistra --> foto e pulsante conferma
    schermata.blit(foto, (40, 150))
    pulsante_conferma = pygame.Rect(40, 450, 280, 55)
    disegna_pulsanti(pulsante_conferma, "CONFERMA", pulsante_conferma.collidepoint(posizione_mouse))

    # colonna destra --> casella nome
    casella_nome = pygame.Rect(420, 150, 320, 60)
    pygame.draw.rect(schermata, COLORE_pulsante, casella_nome, border_radius=12)
    pygame.draw.rect(schermata, COLORE_pulsante_bordo, casella_nome, width=2, border_radius=12)

    testo_nome = FONT_testo.render(nome_attuale, True, COLORE_testo)
    schermata.blit(testo_nome, testo_nome.get_rect(center=casella_nome.center))

    # rettangolo con la parola
    parola_box = pygame.Rect(420, 240, 320, 130)
    pygame.draw.rect(schermata, (20, 20, 50), parola_box, border_radius=12)
    pygame.draw.rect(schermata, COLORE_pulsante_bordo, parola_box, width=2, border_radius=12)

    # controlla se il giocatore corrente è nella lista degli impostori
    # se sì --> vede "IMPOSTORE" in rosso + l'indizio sotto in rosso più chiaro
    # se no --> vede la parola normale in bianco
    if nome_attuale in nomi_impostori:
        font_parola = pygame.font.SysFont("Arial", 36, bold=True)
        testo_imp = font_parola.render("IMPOSTORE", True, (200, 50, 50))       # rosso lucente
        schermata.blit(testo_imp, testo_imp.get_rect(centerx=parola_box.centerx, top=parola_box.y + 15))
        font_indizio = pygame.font.SysFont("Arial", 26, bold=False)
        testo_ind = font_indizio.render(f"il tuo indizio: {parola_indizio}", True, (220, 120, 120))  # rosso chiaro
        schermata.blit(testo_ind, testo_ind.get_rect(centerx=parola_box.centerx, top=parola_box.y + 70))
    else:
        font_parola = pygame.font.SysFont("Arial", 36, bold=True)
        testo_parola = font_parola.render(parola_partita, True, COLORE_testo)  # parola casuale --> coppia[0]
        schermata.blit(testo_parola, testo_parola.get_rect(center=parola_box.center))

    # rettangolo coprente trascinabile
    coperta_rect = pygame.Rect(420, 240 + int(coperta_y), 320, 130)
    pygame.draw.rect(schermata, COLORE_pulsante, coperta_rect, border_radius=12)
    pygame.draw.rect(schermata, COLORE_pulsante_bordo, coperta_rect, width=2, border_radius=12)
    if coperta_y < 50:
        hint_coperta = FONT_piccolo.render("trascina per scoprire ↓", True, (160, 160, 200))
        schermata.blit(hint_coperta, hint_coperta.get_rect(center=coperta_rect.center))

    pygame.display.flip()
    return pulsante_conferma, coperta_rect


def disegna_schermata_ordine_gioco():
    '''Questa funzione disegna la schermata ORDINE DI GIOCO.
       Mostra in ordine i giocatori che devono dire una parola a voce.
       Con il pulsante SUCCESSIVO si passa al giocatore successivo.
       Quando tutti hanno detto la loro parola si passa alle votazioni.
    '''

    schermata.blit(sfondo, (0, 0))
    posizione_mouse = pygame.mouse.get_pos()

    # titolo della schermata
    titolo = FONT_titolo.render("ORDINE DI GIOCO", True, COLORE_titolo)
    schermata.blit(titolo, titolo.get_rect(centerx=LARGHEZZA // 2, top=30))

    # mostra il giocatore corrente che deve dire la parola
    nome_attuale = ordine_giocatori[indice_ordine_gioco]

    # rettangolo che contiene il nome del giocatore corrente
    casella_giocatore = pygame.Rect(LARGHEZZA // 2 - 200, 160, 400, 65)
    pygame.draw.rect(schermata, COLORE_pulsante, casella_giocatore, border_radius=12)
    pygame.draw.rect(schermata, COLORE_pulsante_bordo, casella_giocatore, width=2, border_radius=12)
    testo_nome = FONT_testo.render(nome_attuale, True, COLORE_testo)
    schermata.blit(testo_nome, testo_nome.get_rect(center=casella_giocatore.center))

    # scritta che indica cosa deve fare il giocatore
    hint = FONT_piccolo.render("è il tuo turno: di' una parola!", True, (160, 160, 200))
    schermata.blit(hint, hint.get_rect(centerx=LARGHEZZA // 2, top=240))

    # indicatore del progresso --> quanti giocatori hanno già detto la parola
    progresso = FONT_piccolo.render(f"{indice_ordine_gioco + 1} / {len(ordine_giocatori)}", True, COLORE_testo)
    schermata.blit(progresso, progresso.get_rect(centerx=LARGHEZZA // 2, top=280))

    # pulsante SUCCESSIVO --> passa al giocatore successivo
    pulsante_successivo = pygame.Rect(LARGHEZZA // 2 - 150, 340, 300, 65)
    disegna_pulsanti(pulsante_successivo, "SUCCESSIVO", pulsante_successivo.collidepoint(posizione_mouse))

    pygame.display.flip()
    return pulsante_successivo


def disegna_schermata_votazioni():
    '''Questa funzione disegna la schermata VOTAZIONI.
       A sinistra: il nome del giocatore che deve votare.
       A destra: la tendina con tutti i nomi, ordinata per voti ricevuti.
       Ogni click su un nome aggiunge un voto a quel giocatore.
       Dopo che tutti hanno votato compare il risultato.
    '''

    schermata.blit(sfondo, (0, 0))
    posizione_mouse = pygame.mouse.get_pos()

    # titolo della schermata
    titolo = FONT_titolo.render("VOTAZIONI", True, COLORE_titolo)
    schermata.blit(titolo, titolo.get_rect(centerx=LARGHEZZA // 2, top=20))

    # scritta sotto il titolo
    sottotitolo = FONT_piccolo.render("Chi è l'impostore??", True, (160, 160, 200))
    schermata.blit(sottotitolo, sottotitolo.get_rect(centerx=LARGHEZZA // 2, top=115))

    # ===== COLONNA SINISTRA --> nome del giocatore che vota =====

    # rettangolo con il nome del giocatore corrente che deve votare
    indice_sicuro = min(indice_votante, len(ordine_giocatori) - 1)
    nome_votante = ordine_giocatori[indice_sicuro]
    
    casella_votante = pygame.Rect(30, 155, 340, 65)
    pygame.draw.rect(schermata, COLORE_pulsante, casella_votante, border_radius=12)
    pygame.draw.rect(schermata, COLORE_pulsante_bordo, casella_votante, width=2, border_radius=12)
    testo_votante = FONT_testo.render(nome_votante, True, COLORE_testo)
    schermata.blit(testo_votante, testo_votante.get_rect(center=casella_votante.center))

    hint_vota = FONT_piccolo.render("vota chi pensi sia l'impostore", True, (160, 160, 200))
    schermata.blit(hint_vota, (30, 230))

    # rettangolo dove compare il risultato dopo l'ultimo voto
    risultato_box = pygame.Rect(30, 270, 340, 65)
    pygame.draw.rect(schermata, (20, 20, 50), risultato_box, border_radius=12)
    pygame.draw.rect(schermata, COLORE_pulsante_bordo, risultato_box, width=2, border_radius=12)

    # se c'è già un risultato lo mostra nel rettangolo
    if risultato_eliminazione != "":
        font_ris = pygame.font.SysFont("Arial", 18, bold=True)
        # colore verde se impostore eliminato, arancione altrimenti
        colore_ris = (50, 220, 100) if "ELIMINATO" in risultato_eliminazione and "NESSUN" not in risultato_eliminazione else (220, 150, 50)
        testo_ris = font_ris.render(risultato_eliminazione, True, colore_ris)
        schermata.blit(testo_ris, testo_ris.get_rect(center=risultato_box.center))

    # pulsante CONTINUA --> nuovo round (compare solo dopo che è stato mostrato il risultato)
    pulsante_continua = None
    pulsante_salta = None
    if risultato_eliminazione != "":
        pulsante_continua = pygame.Rect(30, 355, 160, 55)
        disegna_pulsanti(pulsante_continua, "CONTINUA", pulsante_continua.collidepoint(posizione_mouse))
        # pulsante SALTA --> va direttamente alla schermata risultati finali
        pulsante_salta = pygame.Rect(210, 355, 160, 55)
        disegna_pulsanti(pulsante_salta, "SALTA", pulsante_salta.collidepoint(posizione_mouse))

    # ===== COLONNA DESTRA --> tendina con i nomi ordinati per voti =====

    # ordina i giocatori per numero di voti ricevuti (dal più votato in alto)
    nomi_ordinati = sorted(voti.keys(), key=lambda n: voti[n], reverse=True)

    lista_box = pygame.Rect(400, 140, 370, 420)
    pygame.draw.rect(schermata, (20, 20, 50), lista_box, border_radius=14)
    pygame.draw.rect(schermata, COLORE_pulsante_bordo, lista_box, width=2, border_radius=14)

    titolo_lista = FONT_piccolo.render("Clicca per votare:", True, (160, 160, 200))
    schermata.blit(titolo_lista, (lista_box.x + 10, lista_box.y + 10))

    ALTEZZA_CASELLA = 58
    contenuto_totale = len(nomi_ordinati) * ALTEZZA_CASELLA
    area_visibile = lista_box.height - 45

    max_scroll_vot = max(0, contenuto_totale - area_visibile)
    scroll_vot_clampato = max(0, min(scroll_votazioni, max_scroll_vot))

    # lista che raccoglie i rettangoli cliccabili dei nomi nella tendina
    rects_voto = []

    clip_area = pygame.Rect(lista_box.x, lista_box.y + 40, lista_box.width, lista_box.height - 45)
    # ritaglio per non far uscire le caselle dal rettangolo principale
    schermata.set_clip(clip_area)

    for i, nome in enumerate(nomi_ordinati):

        casella_y = lista_box.y + 45 + i * ALTEZZA_CASELLA - scroll_vot_clampato
        casella = pygame.Rect(lista_box.x + 10, casella_y, lista_box.width - 20, 48)

        hover_casella = casella.collidepoint(posizione_mouse)
        # il giocatore non può votare se stesso --> casella grigia non cliccabile
        if nome == nome_votante:
            colore_finale = (100, 100, 120)
        else:
            colore_finale = (220, 220, 245) if hover_casella else (200, 200, 230)

        pygame.draw.rect(schermata, colore_finale, casella, border_radius=8)
        pygame.draw.rect(schermata, COLORE_pulsante_bordo, casella, width=2, border_radius=8)

        # mostra il nome del giocatore a sinistra
        testo_nome = font_nome.render(nome, True, COLORE_testo2)
        schermata.blit(testo_nome, testo_nome.get_rect(midleft=(casella.x + 12, casella.centery)))

        # mostra il numero di voti ricevuti a destra nella casella
        font_voti = pygame.font.SysFont("Arial", 20, bold=True)
        testo_voti = font_voti.render(f"▲ {voti[nome]}", True, (80, 80, 160))
        schermata.blit(testo_voti, testo_voti.get_rect(midright=(casella.right - 10, casella.centery)))

        rects_voto.append((casella, nome))

    schermata.set_clip(None)

    # barra di scorrimento se i nomi sono troppi
    if contenuto_totale > area_visibile and max_scroll_vot > 0:
        barra_h = int(area_visibile * (area_visibile / contenuto_totale))
        barra_y = lista_box.y + 45 + int(scroll_vot_clampato / max_scroll_vot * (area_visibile - barra_h))
        barra = pygame.Rect(lista_box.right - 10, barra_y, 6, barra_h)
        pygame.draw.rect(schermata, COLORE_pulsante_bordo, barra, border_radius=3)

    pygame.display.flip()
    return rects_voto, pulsante_continua, pulsante_salta


def disegna_schermata_risultati():
    '''Questa funzione disegna la schermata RISULTATI finali.
       Mostra chi erano gli impostori nella partita.
    '''

    schermata.blit(sfondo, (0, 0))
    posizione_mouse = pygame.mouse.get_pos()

    # titolo della schermata
    titolo = FONT_titolo.render("RISULTATI", True, COLORE_titolo)
    schermata.blit(titolo, titolo.get_rect(centerx=LARGHEZZA // 2, top=40))

    # scritta che introduce la lista degli impostori
    sottotitolo = FONT_piccolo.render("Gli impostori erano:", True, (160, 160, 200))
    schermata.blit(sottotitolo, sottotitolo.get_rect(centerx=LARGHEZZA // 2, top=150))

    # mostra ogni impostore in un rettangolo rosso
    for i, nome in enumerate(nomi_impostori):
        casella = pygame.Rect(LARGHEZZA // 2 - 200, 190 + i * 70, 400, 55)
        pygame.draw.rect(schermata, (80, 20, 20), casella, border_radius=12)
        pygame.draw.rect(schermata, (200, 50, 50), casella, width=2, border_radius=12)
        testo = FONT_testo.render(nome, True, (200, 50, 50))
        schermata.blit(testo, testo.get_rect(center=casella.center))

    # pulsante per tornare alla schermata principale
    pulsante_menu = pygame.Rect(LARGHEZZA // 2 - 150, 470, 300, 65)
    disegna_pulsanti(pulsante_menu, "MENU PRINCIPALE", pulsante_menu.collidepoint(posizione_mouse))

    pygame.display.flip()
    return pulsante_menu


#========================================================================
# GESTIONE DEL LOOP --> gestione e organizzazione
#========================================================================

schermata_attuale = "finestra_principale"
rects_x_nomi = []                             # lista che contiene le posizioni dei pulsanti 'X'
pulsante_conferma_gioco = None                # salva la posizione del pulsante CONFERMA nella schermata di gioco
coperta_rect_gioco = None                     # salva la posizione del rettangolo coprente nella schermata di gioco
pulsante_successivo_ordine = None             # salva la posizione del pulsante SUCCESSIVO nella schermata ordine di gioco
rects_voto_votazioni = []                     # lista dei rettangoli cliccabili nella schermata votazioni
pulsante_continua_votazioni = None            # pulsante CONTINUA nella schermata votazioni
pulsante_salta_votazioni = None               # pulsante SALTA nella schermata votazioni
pulsante_menu_risultati = None                # pulsante MENU PRINCIPALE nella schermata risultati

orologio = pygame.time.Clock()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #========================================================
        # GESTIONE CLICK DEL MOUSE
        #========================================================
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            if schermata_attuale == "finestra_principale":
                if PULSANTE_1.collidepoint(event.pos):
                    schermata_attuale = "inizio_partita"
                elif PULSANTE_2.collidepoint(event.pos):
                    schermata_attuale = "impostazioni"

            elif schermata_attuale == "inizio_partita":
                PULSANTE_NOMI = pygame.Rect(LARGHEZZA // 2 - PULSANTE_larghezza // 2, 300, PULSANTE_larghezza, PULSANTE_altezza)
                if PULSANTE_NOMI.collidepoint(event.pos):
                    schermata_attuale = "nomi_giocatori"
                if len(nomi_giocatori) >= 3:
                    PULSANTE_INIZIA = pygame.Rect(LARGHEZZA // 2 - PULSANTE_larghezza // 2, 390, PULSANTE_larghezza, PULSANTE_altezza)
                    if PULSANTE_INIZIA.collidepoint(event.pos):
                        inizia_partita()
                        schermata_attuale = "gioco"

            elif schermata_attuale == "nomi_giocatori":
                for i, x_rect in enumerate(rects_x_nomi):
                    if x_rect.collidepoint(event.pos):
                        nomi_giocatori.pop(i)
                        break
                pulsante_aggiungi = pygame.Rect(50, 260, 280, 55)
                if pulsante_aggiungi.collidepoint(event.pos):
                    if nome_corrente.strip() != "" and len(nomi_giocatori) < numero_giocatori:
                        nomi_giocatori.append(nome_corrente.strip())
                        nome_corrente = ""
                if len(nomi_giocatori) >= 3:
                    pulsante_conferma = pygame.Rect(50, 340, 280, 55)
                    if pulsante_conferma.collidepoint(event.pos):
                        nome_corrente = ""
                        schermata_attuale = "inizio_partita"

            elif schermata_attuale == "gioco":
                if pulsante_conferma_gioco is not None and coperta_rect_gioco is not None:

                    # inizia trascinamento
                    if coperta_rect_gioco.collidepoint(event.pos):
                        coperta_trascinando = True
                        coperta_offset = event.pos[1] - (240 + coperta_y)

                    # click su CONFERMA --> passa al giocatore successivo
                    if pulsante_conferma_gioco.collidepoint(event.pos):
                        coperta_y = 0
                        coperta_trascinando = False
                        indice_giocatore_corrente += 1
                        # quando tutti i giocatori hanno visto la loro parola si passa all'ordine di gioco
                        if indice_giocatore_corrente >= len(ordine_giocatori):
                            indice_ordine_gioco = 0
                            schermata_attuale = "ordine_gioco"

            elif schermata_attuale == "ordine_gioco":
                if pulsante_successivo_ordine is not None and pulsante_successivo_ordine.collidepoint(event.pos):
                    indice_ordine_gioco += 1
                    # quando tutti i giocatori hanno detto la loro parola si passa alle votazioni
                    if indice_ordine_gioco >= len(ordine_giocatori):
                        indice_votante = 0
                        scroll_votazioni = 0
                        schermata_attuale = "votazioni"

            elif schermata_attuale == "votazioni":

                # click su un nome nella tendina --> aggiunge un voto a quel giocatore
                indice_sicuro = min(indice_votante, len(ordine_giocatori) - 1)
                nome_votante_corrente = ordine_giocatori[indice_sicuro]
                
                for casella, nome in rects_voto_votazioni:
                    # il giocatore non può votare se stesso
                    if casella.collidepoint(event.pos) and nome != nome_votante_corrente:
                        voti[nome] += 1
                        indice_votante += 1

                        # quando tutti hanno votato si calcola il risultato
                        if indice_votante >= len(ordine_giocatori):
                            # trova il giocatore con più voti
                            eliminato = max(voti, key=lambda n: voti[n])
                            if eliminato in nomi_impostori:
                                risultato_eliminazione = f"IMPOSTORE ELIMINATO: {eliminato}"
                                # rimuove il giocatore eliminato dalla lista
                                nomi_giocatori.remove(eliminato)
                                nomi_impostori.remove(eliminato)
                            else:
                                risultato_eliminazione = "NESSUN IMPOSTORE ELIMINATO"
                                # rimuove comunque il giocatore eliminato dalla lista
                                nomi_giocatori.remove(eliminato)
                        break

                # click su CONTINUA --> nuovo round se ci sono ancora impostori
                if pulsante_continua_votazioni is not None and pulsante_continua_votazioni.collidepoint(event.pos):
                    if len(nomi_impostori) == 0 or len(nomi_giocatori) < 3:
                        # non ci sono più impostori o giocatori insufficienti --> risultati finali
                        schermata_attuale = "risultati"
                    else:
                        nuovo_round()
                        schermata_attuale = "ordine_gioco"

                # click su SALTA --> vai direttamente ai risultati finali
                if pulsante_salta_votazioni is not None and pulsante_salta_votazioni.collidepoint(event.pos):
                    schermata_attuale = "risultati"

            elif schermata_attuale == "risultati":
                if pulsante_menu_risultati is not None and pulsante_menu_risultati.collidepoint(event.pos):
                    # reset completo per una nuova partita
                    nomi_giocatori = []
                    nomi_impostori = []
                    giocatori_eliminati = []
                    schermata_attuale = "finestra_principale"

        # rilascio tasto mouse --> smette di trascinare
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            coperta_trascinando = False

        # movimento mouse --> trascina la copertura
        if event.type == pygame.MOUSEMOTION and coperta_trascinando:
            nuova_y = event.pos[1] - coperta_offset - 240
            coperta_y = max(0, min(nuova_y, 130))

        #========================================================
        # GESTIONE TASTIERA
        #========================================================
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                schermata_attuale = "finestra_principale"
            if schermata_attuale == "nomi_giocatori":
                if event.key == pygame.K_BACKSPACE:
                    nome_corrente = nome_corrente[:-1]
                elif event.key == pygame.K_RETURN:
                    if nome_corrente.strip() != "" and len(nomi_giocatori) < numero_giocatori:
                        nomi_giocatori.append(nome_corrente.strip())
                        nome_corrente = ""
                else:
                    if len(nome_corrente) < 15:
                        nome_corrente += event.unicode

        # rotella del mouse per scorrere la lista nomi
        if event.type == pygame.MOUSEWHEEL:
            if schermata_attuale == "nomi_giocatori":
                scroll_lista += event.y * -20
            elif schermata_attuale == "votazioni":
                scroll_votazioni += event.y * -20

    #========================================================
    # ritorno automatico della copertura verso l'alto
    #========================================================
    if not coperta_trascinando and coperta_y > 0 and schermata_attuale == "gioco":
        coperta_y = max(0, coperta_y - 8)

    #========================================================
    # RENDERING SCHERMATA CORRENTE
    #========================================================
    if schermata_attuale == "finestra_principale":
        disegna_finestra_principale()
    elif schermata_attuale == "inizio_partita":
        disegna_schermata_inizio_partita()
    elif schermata_attuale == "impostazioni":
        disegna_finestra_impostazioni()
    elif schermata_attuale == "nomi_giocatori":
        rects_x_nomi = disegna_finestra_nomi_giocatori()
    elif schermata_attuale == "gioco":
        pulsante_conferma_gioco, coperta_rect_gioco = disegna_schermata_gioco()
    elif schermata_attuale == "ordine_gioco":
        pulsante_successivo_ordine = disegna_schermata_ordine_gioco()
    elif schermata_attuale == "votazioni":
        rects_voto_votazioni, pulsante_continua_votazioni, pulsante_salta_votazioni = disegna_schermata_votazioni()
    elif schermata_attuale == "risultati":
        pulsante_menu_risultati = disegna_schermata_risultati()

    orologio.tick(60)
