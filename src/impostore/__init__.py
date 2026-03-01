def main() -> None:

    #=====================================================================
    # IMPOSTAZIONE DEL CODICE --> librerie
    #=====================================================================
 
    import pygame
    import sys
    
    #=====================================================================
    # IMPOSTAZIONE DEL CODICE --> preparazione schermata
    #=====================================================================    

    # Richiama tutte le funzioni presenti in pygame
    pygame.init()

    # Questa sezione di codice fa comparire sullo schermo una finestra che fa partire il gioco
    LARGHEZZA, ALTEZZA = 800, 600
    screen = pygame.display.set_mode((LARGHEZZA, HEIGHT))
    pygame.display.set_caption("Impostore")

    # Colori
    BG_COLOR = (15, 15, 30)
    TITLE_COLOR = (220, 50, 50)
    BTN_COLOR = (40, 40, 80)
    BTN_HOVER_COLOR = (70, 70, 130)
    BTN_BORDER_COLOR = (100, 100, 200)
    TEXT_COLOR = (255, 255, 255)

    # Font del titolo e delle scritte
    font_title = pygame.font.SysFont("Arial", 90, bold=True)
    font_btn = pygame.font.SysFont("Arial", 32)

    # viene definita l'altezza e la larghezza dei pulsanti
    btn_width, btn_height = 300, 70
    # posizione e forma (rettangolare)
    btn1_rect = pygame.Rect(LARGHEZZA // 2 - btn_width // 2, 300, btn_width, btn_height)
    btn2_rect = pygame.Rect(LARGHEZZA // 2 - btn_width // 2, 410, btn_width, btn_height)

    #=======================================================
    
    def draw_button(rect, label, hovered):
        # font nei pulsanti
        font = pygame.font.SysFont("Arial", 32)
        # colore che cambia quando il mouse si trova sopra il pulsante
        color = BTN_HOVER_COLOR if hovered else BTN_COLOR
        
        # permette di avere i bordi smussati definendo un reggio 
        pygame.draw.rect(screen, color, rect, border_radius=12)
        # viene creato un bordo intorna ad ogni pulsante
        pygame.draw.rect(screen, BTN_BORDER_COLOR, rect, width=2, border_radius=12)
        
        # generazione e renderizzazione della scritta all'interno dei pulsanti
        text = font.render(label, True, TEXT_COLOR)
        screen.blit(text, text.get_rect(center=rect.center))

    def draw_home():
        # colora lo schermo
        screen.fill(BG_COLOR)

        # renderizza il titolo con il font che abbiamo definiti prima
        title = font_title.render("IMPOSTORE", True, TITLE_COLOR)
        screen.blit(title, title.get_rect(centerx=LARGHEZZA // 2, top=80))

        # scrive un frase sotto il titolo
        sub_font = pygame.font.SysFont("Arial", 22)
        sub = sub_font.render("Chi è l'impostore tra voi?", True, (160, 160, 200))
        screen.blit(sub, sub.get_rect(centerx=LARGHEZZA // 2, top=195))

        # renderizzati i pulsanti che cambiano colore
        mouse_pos = pygame.mouse.get_pos()
        draw_button(btn1_rect, "Nuova Partita", btn1_rect.collidepoint(mouse_pos))
        draw_button(btn2_rect, "Impostazioni", btn2_rect.collidepoint(mouse_pos))

        # aggiorna la schermata appena generata
        pygame.display.flip()

    # --- Schermata placeholder: Nuova Partita ---
    def screen_nuova_partita():
        
        # font che viene usto per scrivere il testo
        font = pygame.font.SysFont("Arial", 40)
        screen.fill(BG_COLOR) # --> colora lo schermo 
        msg = font.render("Qui inizierà la partita...", True, TEXT_COLOR)
        
        #disegna il testo al centro dello schermo
        screen.blit(msg, msg.get_rect(center=(LARGHEZZA // 2, ALTEZZA // 2)))
        pygame.display.flip()

    # --- Schermata placeholder: Impostazioni ---
    def screen_impostazioni():
        font = pygame.font.SysFont("Arial", 40)
        screen.fill(BG_COLOR)
        msg = font.render("Qui ci saranno le impostazioni...", True, TEXT_COLOR)
        screen.blit(msg, msg.get_rect(center=(LARGHEZZA // 2, ALTEZZA // 2)))
        pygame.display.flip()

    # Stato corrente
    current_screen = "home"

    # Loop principale
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if current_screen == "home":
                    if btn1_rect.collidepoint(event.pos):
                        current_screen = "nuova_partita"
                    elif btn2_rect.collidepoint(event.pos):
                        current_screen = "impostazioni"

            # Tasto ESC per tornare alla home
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                current_screen = "home"

        # Rendering in base allo stato
        if current_screen == "home":
            draw_home()
        elif current_screen == "nuova_partita":
            screen_nuova_partita()
        elif current_screen == "impostazioni":
            screen_impostazioni()

        clock.tick(60)

