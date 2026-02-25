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
    # IMPOSTAZIONE DEL CODICE --> librerie
    #=====================================================================
 
    import pygame
    import sys
    
    #=====================================================================
    # IMPOSTAZIONE DEL CODICE --> preparazione schermata
    #=====================================================================    

    # Inizializzazione
    pygame.init()

    # Finestra
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Impostore")

    # Colori
    BG_COLOR = (15, 15, 30)
    TITLE_COLOR = (220, 50, 50)
    BTN_COLOR = (40, 40, 80)
    BTN_HOVER_COLOR = (70, 70, 130)
    BTN_BORDER_COLOR = (100, 100, 200)
    TEXT_COLOR = (255, 255, 255)

    # Font
    font_title = pygame.font.SysFont("Arial", 90, bold=True)
    font_btn = pygame.font.SysFont("Arial", 32)

    # Pulsanti
    btn_width, btn_height = 300, 70
    btn1_rect = pygame.Rect(WIDTH // 2 - btn_width // 2, 300, btn_width, btn_height)
    btn2_rect = pygame.Rect(WIDTH // 2 - btn_width // 2, 410, btn_width, btn_height)

    def draw_button(rect, label, hovered):
        font = pygame.font.SysFont("Arial", 32)
        color = BTN_HOVER_COLOR if hovered else BTN_COLOR
        pygame.draw.rect(screen, color, rect, border_radius=12)
        pygame.draw.rect(screen, BTN_BORDER_COLOR, rect, width=2, border_radius=12)
        text = font.render(label, True, TEXT_COLOR)
        screen.blit(text, text.get_rect(center=rect.center))

    def draw_home():
        screen.fill(BG_COLOR)

        # Titolo
        title = font_title.render("IMPOSTORE", True, TITLE_COLOR)
        screen.blit(title, title.get_rect(centerx=WIDTH // 2, top=80))

        # Sottotitolo
        sub_font = pygame.font.SysFont("Arial", 22)
        sub = sub_font.render("Chi è l'impostore tra voi?", True, (160, 160, 200))
        screen.blit(sub, sub.get_rect(centerx=WIDTH // 2, top=195))

        # Pulsanti
        mouse_pos = pygame.mouse.get_pos()
        draw_button(btn1_rect, "▶  Nuova Partita", btn1_rect.collidepoint(mouse_pos))
        draw_button(btn2_rect, "⚙  Impostazioni", btn2_rect.collidepoint(mouse_pos))

        pygame.display.flip()

    # --- Schermata placeholder: Nuova Partita ---
    def screen_nuova_partita():
        font = pygame.font.SysFont("Arial", 40)
        screen.fill(BG_COLOR)
        msg = font.render("Qui inizierà la partita...", True, TEXT_COLOR)
        screen.blit(msg, msg.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
        pygame.display.flip()

    # --- Schermata placeholder: Impostazioni ---
    def screen_impostazioni():
        font = pygame.font.SysFont("Arial", 40)
        screen.fill(BG_COLOR)
        msg = font.render("Qui ci saranno le impostazioni...", True, TEXT_COLOR)
        screen.blit(msg, msg.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
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

