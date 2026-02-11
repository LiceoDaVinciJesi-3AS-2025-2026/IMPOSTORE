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



    #=======================================
    # impostazioni codice iniziale
    #========================================

    import pygame
    
    # per iniziare pygame (come per accedere alle funzioni presenti in pygame)
    pygame.init()

    screen = pygame.display.set_mode( (800, 600) )
    pygame.display.set_caption("Il mio primo gioco con PyGame!")

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Se l'evento è la pressione di un tasto...
            # ... e il tasto è il tasto ESC.. esc(i)!
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

    screen.fill("green")
    pygame.display.flip()

    pygame.quit()



