#========================================================================
# FILE GESTIONE GRAFICA --> funzioni per visualizzare il gioco
#========================================================================

import pygame
import sys
import random

from lista_partecipanti import paroleGioco

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
parola_partita = "prova"
nome_impostore = ""
coperta_y = 0
coperta_trascinando = False
coperta_offset = 0


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
    global nome_impostore, coperta_y, coperta_trascinando

    ordine_giocatori = nomi_giocatori[:]
    random.shuffle(ordine_giocatori)
    nome_impostore = random.choice(ordine_giocatori)
    indice_giocatore_corrente = 0
    coperta_y = 0
    coperta_trascinando = False 


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
    
    # disegan i pulsanti secondo la funzione già definita
    # la funzione ".collidepoint()" ritorna True se il mouse si trova sopra l'area del pulsante
    disegna_pulsanti(PULSANTE_1, "Nuova Partita", PULSANTE_1.collidepoint(posizione_mouse))
    disegna_pulsanti(PULSANTE_2, "Impostazioni", PULSANTE_2.collidepoint(posizione_mouse))
    
    # aggiorna la scheramta 
    pygame.display.flip()


def disegna_finestra_impostazioni():
    '''Questa funzione disegna una schermata chiamata IMPOSTAZIONI
          - vengono fornite le istruzioni principali per giocare
          
    '''
    
    # incolla l'immagine nello sfondo
    schermata.blit(sfondo, (0, 0))
    
    # genera il testo e lo centra rispetto a tutta la schermata
    messaggio_impostazioni = FONT_testo.render("Qui ci saranno le impostazioni...", True, COLORE_testo)
    schermata.blit(messaggio_impostazioni, messaggio_impostazioni.get_rect(center=(LARGHEZZA // 2, ALTEZZA // 2)))
    
    # aggiorna la scheramta
    pygame.display.flip()


def disegna_schermata_inizio_partita():
    '''Questa funzione diegna una schermata con due pulsanti
          - INIZIO PARTITA compare subito
          - INIZIA comapre quando hai compilato e confermato le informazioni nella pagina precedente
          
    '''
    
    # incolla l'immagine sullo schermo
    schermata.blit(sfondo, (0, 0))
    
    # genere il titolo e lo incolla centrato nella pagina in alto
    titolo_inizio_partita = FONT_titolo.render("INIZIO PARTITA", True, COLORE_titolo)
    schermata.blit(titolo_inizio_partita, titolo_inizio_partita.get_rect(centerx=LARGHEZZA // 2, top=80))
    
    # viengono definite le coordinate del mouse
    posizione_mouse = pygame.mouse.get_pos()
    
    # viene generato il pulsante e centrato nello schermo
    PULSANTE_NOMI = pygame.Rect(LARGHEZZA // 2 - PULSANTE_larghezza // 2, 300, PULSANTE_larghezza, PULSANTE_altezza)
    disegna_pulsanti(PULSANTE_NOMI, "NOMI GIOCATORI", PULSANTE_NOMI.collidepoint(posizione_mouse))
    
    # il secondo pulsante comare solo quando la lista dei giocatori è maggiore di 3
    # infatti il gioco funziona solo quando partecipano più di tre giocatori
    if len(nomi_giocatori) >= 3:
        PULSANTE_INIZIA = pygame.Rect(LARGHEZZA // 2 - PULSANTE_larghezza // 2, 390, PULSANTE_larghezza, PULSANTE_altezza)
        disegna_pulsanti(PULSANTE_INIZIA, "INIZIA", PULSANTE_INIZIA.collidepoint(posizione_mouse))
    
    # aggiorna la schermata
    pygame.display.flip()


def disegna_finestra_nomi_giocatori():
    '''Questa funzione gestisce tutto il meccanismo di inserimento dei nomi dei giocatori'''
    
    # incolla la foto sullo chermo
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
    
    # visualizza il testo che l'utente sta scrivendo all'inteno del rettangolo
    # centra il testo in modo che non tocchi il bordo del rettangolo
    testo_input = FONT_testo.render(nome_corrente, True, COLORE_testo)
    schermata.blit(testo_input, testo_input.get_rect(midleft=(input_box.x + 12, input_box.centery)))

    # genera il secondo pulsante che permette di aggiungere alla lista il nome inserito nella casella di input
    pulsante_aggiungi = pygame.Rect(50, 260, 280, 55)
    disegna_pulsanti(pulsante_aggiungi, "AGGIUNGI", pulsante_aggiungi.collidepoint(posizione_mouse))
    
    # se hai inserito almeno tre nomi dei giocatori, comapre anche il tasto di CONFERMA che fa iniziare il gioco
    if len(nomi_giocatori) >= 3:
        pulsante_conferma = pygame.Rect(50, 340, 280, 55)
        disegna_pulsanti(pulsante_conferma, "CONFERMA", pulsante_conferma.collidepoint(posizione_mouse))

    # puoi inserire il nome alla lista anche cliccando sul tasto invio
    # questa dinamica viene gestita nel LOOP infondo
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
    area_visibile = lista_box.height - 45 # 
    
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
        testo_x = font_x.render("X", True, (255, 255, 255)) # bianco lucente
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
    '''Questa funzione permette di disegnare la scheramta '''
    
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

    if nome_attuale == nome_impostore:
        parola_da_mostrare = "IMPOSTORE"
        colore_parola = (200, 50, 50) # rosso lucente 
    else:
        parola_da_mostrare = parola_partita
        colore_parola = COLORE_testo

    font_parola = pygame.font.SysFont("Arial", 36, bold=True)
    testo_parola = font_parola.render(parola_da_mostrare, True, colore_parola)
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


#========================================================================
# GESTIONE DEL LOOP --> gestione e organizzazione
#========================================================================

schermata_attuale = "finestra_principale"
rects_x_nomi = []                             # lista che conriente le posizioni dei pulanti 'X'
pulsante_conferma_gioco = None                # salva la posizione del pulsante CONFERMA nella schermata di gioco
coperta_rect_gioco = None                     # salva la posizione del rettangolo coprente nella schermata di gioco

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

                    # click su CONFERMA
                    if pulsante_conferma_gioco.collidepoint(event.pos):
                        coperta_y = 0
                        coperta_trascinando = False
                        indice_giocatore_corrente += 1
                        if indice_giocatore_corrente >= len(ordine_giocatori):
                            schermata_attuale = "fine_turni"

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
        if event.type == pygame.MOUSEWHEEL and schermata_attuale == "nomi_giocatori":
            scroll_lista += event.y * -20

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

    orologio.tick(60)
    
    
if __name__ == "__main__":
    main()
    