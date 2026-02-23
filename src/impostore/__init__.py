def main() -> None:

    #=======================================
    # Divisione del codice 
    # INSERIMENTO NOMI PARTECIPANTI --> in una lista
    # PAROLE DEL GIOCO --> ['parole del gioco', 'indizi impostore(massimo tre)']
    # INDIZI IMPOSTORE --> max tre
    # NUMERO IMPOSTORI --> massimo tre
    # SCELTA IMPOSTORI --> lista parteccipanti con random.choice()
    # ORDINE DEI GIOCATORI --> random.shuffle() 
    # INSERIMENTO DELLA PAROLA DI OGNI PARTECIPANTE 
    # voti partecipanti



    #=====================================================================
    # IMPOSTAZIONE DEL CODICE --> variabili necessarie per tutto il codice
    #=====================================================================

    import pygame
    
    # per iniziare pygame (come per accedere alle funzioni presenti in pygame)
    pygame.init()
    
    altezza_schermata = 800
    lunghezza_schermata = 800
    
    # definizione dei font nella schermata di gioco 
    font_titolo = pygame.font.SysFont('Calibri', 70)
    font_normale = pygame.font.SysFont('Calibri', 30)
    
    #=========================================
    # GENERARE UNA SCHERMATA --> gestione 
    #=========================================
    
    # scritte che compaiono quando prov a chiudere il gioco
    scritta_fine_gioco = font_titolo.render('Hai chiuso il gioco!', True, 'white')
    scritta_chiusura_gioco = font_normale.render('premi ESC per uscire del gioco', True, 'white')

    # genera una scharmata con il titolo in alto 
    screen = pygame.display.set_mode( (altezza_schermata, lunghezza_schermata) )
    pygame.display.set_caption("Il mio primo gioco con PyGame!")

    running = True

    while running:
        # serve a gestire la chiusura della pagina del gioco
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill("red")
        screen.blit(scritta_fine_gioco, (100,100))
        screen.blit(scritta_chiusura_gioco, (100,300))
        pygame.display.flip()

    pygame.quit()



