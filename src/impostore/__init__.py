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
    pygame.init()

    # crea una finestra con il titolo "Impostore" che appare nella barra del titolo in alto
    screen = pygame.display.set_mode((800,600))
    screen.fill("red")

    pygame.display.set_caption("Impostore")

    
    running = True

    while running:
        # serve a gestire la X di chiusura in alto
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # colora lo schermo di verde
        screen.fill("green")

        # aggiorna il contenuto dello schermo
        pygame.display.flip()

    # Chiude pygame
    pygame.quit()



