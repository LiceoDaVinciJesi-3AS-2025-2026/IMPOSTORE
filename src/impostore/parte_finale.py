# ========================================================================
# Aggiungi queste righe in cima al tuo file grafica, con gli altri import
# ========================================================================
# from lista_partecipanti import parolaDaInserire, ordineGiocatori
# from votazione import votazioni, contaVoti, controllaImpostori
# from round import round


# ========================================================================
# Aggiungi queste variabili globali vicino alle altre in cima al file
# ========================================================================
# parole_inserite = {}       # {nome: parola}
# voti_inseriti = {}         # {nome: votato}
# lista_eliminati = []
# testo_input = ""
# indice_inserimento = 0
# indice_voto = 0


# ========================================================================
# SCHERMATA 1 — Inserimento parole
# Chiamata quando schermata_attuale == "inserimento_parola"
# ========================================================================

def disegna_schermata_inserimento_parola():
    schermata.blit(sfondo, (0, 0))

    nome_attuale = ordine_giocatori[indice_inserimento]

    titolo = FONT_titolo.render("INSERISCI", True, COLORE_titolo)
    schermata.blit(titolo, titolo.get_rect(centerx=LARGHEZZA // 2, top=30))

    txt_turno = FONT_piccolo.render(f"{indice_inserimento + 1} / {len(ordine_giocatori)}", True, (160, 160, 200))
    schermata.blit(txt_turno, txt_turno.get_rect(centerx=LARGHEZZA // 2, top=130))

    casella_nome = pygame.Rect(LARGHEZZA // 2 - 200, 170, 400, 55)
    pygame.draw.rect(schermata, COLORE_pulsante, casella_nome, border_radius=12)
    pygame.draw.rect(schermata, COLORE_pulsante_bordo, casella_nome, width=2, border_radius=12)
    t = FONT_testo.render(nome_attuale, True, COLORE_testo)
    schermata.blit(t, t.get_rect(center=casella_nome.center))

    istruzione = FONT_piccolo.render("Scrivi una parola collegata alla tua parola segreta:", True, (160, 160, 200))
    schermata.blit(istruzione, istruzione.get_rect(centerx=LARGHEZZA // 2, top=250))

    input_box = pygame.Rect(LARGHEZZA // 2 - 200, 285, 400, 55)
    pygame.draw.rect(schermata, (20, 20, 50), input_box, border_radius=10)
    pygame.draw.rect(schermata, COLORE_pulsante_bordo, input_box, width=2, border_radius=10)
    testo_render = FONT_testo.render(testo_input, True, COLORE_testo)
    schermata.blit(testo_render, testo_render.get_rect(midleft=(input_box.x + 14, input_box.centery)))

    if testo_input.strip().lower() in [p.lower() for p in parole_inserite.values()]:
        errore = FONT_piccolo.render("Parola gia usata!", True, (200, 80, 80))
        schermata.blit(errore, errore.get_rect(centerx=LARGHEZZA // 2, top=350))

    hint = FONT_piccolo.render("INVIO per confermare", True, (100, 100, 160))
    schermata.blit(hint, hint.get_rect(centerx=LARGHEZZA // 2, top=385))

    posizione_mouse = pygame.mouse.get_pos()
    pulsante = pygame.Rect(LARGHEZZA // 2 - PULSANTE_larghezza // 2, 430, PULSANTE_larghezza, PULSANTE_altezza)
    disegna_pulsanti(pulsante, "CONFERMA", pulsante.collidepoint(posizione_mouse))

    pygame.display.flip()
    return pulsante


# ========================================================================
# SCHERMATA 2 — Riepilogo parole + pulsante vai alle votazioni
# Chiamata quando schermata_attuale == "riepilogo_parole"
# ========================================================================

def disegna_schermata_riepilogo_parole():
    schermata.blit(sfondo, (0, 0))

    titolo = FONT_titolo.render("LE PAROLE", True, COLORE_titolo)
    schermata.blit(titolo, titolo.get_rect(centerx=LARGHEZZA // 2, top=30))

    sottotitolo = FONT_piccolo.render("Discutete: chi e l'impostore?", True, (160, 160, 200))
    schermata.blit(sottotitolo, sottotitolo.get_rect(centerx=LARGHEZZA // 2, top=125))

    # mostra le parole restituite da parolaDaInserire()
    y_start = 170
    for i, (nome, parola) in enumerate(parole_inserite.items()):
        riga = pygame.Rect(LARGHEZZA // 2 - 280, y_start + i * 52, 560, 44)
        pygame.draw.rect(schermata, COLORE_pulsante, riga, border_radius=10)
        pygame.draw.rect(schermata, COLORE_pulsante_bordo, riga, width=2, border_radius=10)
        t_nome = font_nome.render(nome, True, (160, 200, 255))
        schermata.blit(t_nome, t_nome.get_rect(midleft=(riga.x + 16, riga.centery)))
        t_parola = FONT_testo.render(parola.upper(), True, COLORE_testo)
        schermata.blit(t_parola, t_parola.get_rect(midright=(riga.right - 16, riga.centery)))

    posizione_mouse = pygame.mouse.get_pos()
    pulsante = pygame.Rect(LARGHEZZA // 2 - PULSANTE_larghezza // 2, 530, PULSANTE_larghezza, PULSANTE_altezza)
    disegna_pulsanti(pulsante, "VOTA", pulsante.collidepoint(posizione_mouse))

    pygame.display.flip()
    return pulsante


# ========================================================================
# SCHERMATA 3 — Votazione
# Chiamata quando schermata_attuale == "voto"
# ========================================================================

def disegna_schermata_voto():
    schermata.blit(sfondo, (0, 0))

    nome_attuale = ordine_giocatori[indice_voto]

    titolo = FONT_titolo.render("VOTA", True, COLORE_titolo)
    schermata.blit(titolo, titolo.get_rect(centerx=LARGHEZZA // 2, top=30))

    txt_turno = FONT_piccolo.render(f"{indice_voto + 1} / {len(ordine_giocatori)}", True, (160, 160, 200))
    schermata.blit(txt_turno, txt_turno.get_rect(centerx=LARGHEZZA // 2, top=130))

    casella_nome = pygame.Rect(LARGHEZZA // 2 - 200, 160, 400, 55)
    pygame.draw.rect(schermata, COLORE_pulsante, casella_nome, border_radius=12)
    pygame.draw.rect(schermata, COLORE_pulsante_bordo, casella_nome, width=2, border_radius=12)
    t = FONT_testo.render(nome_attuale, True, COLORE_testo)
    schermata.blit(t, t.get_rect(center=casella_nome.center))

    domanda = FONT_piccolo.render("Chi vuoi eliminare?", True, (160, 160, 200))
    schermata.blit(domanda, domanda.get_rect(centerx=LARGHEZZA // 2, top=230))

    # un pulsante per ogni candidato tranne se stesso
    candidati = [p for p in lista_partecipanti if p != nome_attuale]
    pulsanti_candidati = []
    posizione_mouse = pygame.mouse.get_pos()
    cols = 2
    btn_w, btn_h = 260, 52
    gap_x, gap_y = 20, 12
    x_start = LARGHEZZA // 2 - (cols * btn_w + (cols - 1) * gap_x) // 2
    y_start = 270
    for i, candidato in enumerate(candidati):
        bx = x_start + (i % cols) * (btn_w + gap_x)
        by = y_start + (i // cols) * (btn_h + gap_y)
        btn = pygame.Rect(bx, by, btn_w, btn_h)
        disegna_pulsanti(btn, candidato, btn.collidepoint(posizione_mouse))
        pulsanti_candidati.append((btn, candidato))

    pygame.display.flip()
    return pulsanti_candidati


# ========================================================================
# SCHERMATA 4 — Risultato eliminazione
# Chiamata quando schermata_attuale == "risultato_voto"
# Usa contaVoti() e controllaImpostori() già chiamate nel loop
# ========================================================================

def disegna_schermata_risultato_voto():
    schermata.blit(sfondo, (0, 0))

    titolo = FONT_titolo.render("ELIMINATO!", True, COLORE_titolo)
    schermata.blit(titolo, titolo.get_rect(centerx=LARGHEZZA // 2, top=60))

    y = 175
    for nome_el in lista_eliminati:
        era_imp = nome_el == nome_impostore
        t = FONT_testo.render(nome_el.upper(), True, (200, 80, 80) if era_imp else COLORE_testo)
        schermata.blit(t, t.get_rect(centerx=LARGHEZZA // 2, top=y))
        y += 45
        msg = FONT_piccolo.render(
            f"{nome_el} ERA l'impostore!" if era_imp else f"{nome_el} NON era l'impostore!",
            True, (60, 220, 120) if era_imp else (200, 80, 80))
        schermata.blit(msg, msg.get_rect(centerx=LARGHEZZA // 2, top=y))
        y += 40

    # riepilogo voti
    schermata.blit(FONT_piccolo.render("Voti ricevuti:", True, (160, 160, 200)),
                   FONT_piccolo.render("Voti ricevuti:", True, (160, 160, 200)).get_rect(centerx=LARGHEZZA // 2, top=y + 10))
    y += 35
    conteggio = {}
    for votato in voti_inseriti.values():
        conteggio[votato] = conteggio.get(votato, 0) + 1
    for nome_v, num_v in sorted(conteggio.items(), key=lambda x: -x[1]):
        r = FONT_piccolo.render(f"{nome_v}  ->  {num_v} voti", True, COLORE_testo)
        schermata.blit(r, r.get_rect(centerx=LARGHEZZA // 2, top=y))
        y += 26

    posizione_mouse = pygame.mouse.get_pos()
    pulsante = pygame.Rect(LARGHEZZA // 2 - PULSANTE_larghezza // 2, 510, PULSANTE_larghezza, PULSANTE_altezza)
    disegna_pulsanti(pulsante, "CONTINUA", pulsante.collidepoint(posizione_mouse))

    pygame.display.flip()
    return pulsante


# ========================================================================
# SCHERMATA 5 — Fine gioco (vittoria o sconfitta)
# Chiamata quando schermata_attuale == "vittoria" o "sconfitta"
# ========================================================================

def disegna_schermata_fine(vinto):
    schermata.blit(sfondo, (0, 0))

    if vinto:
        titolo_txt, colore_fin, sub_txt = "VITTORIA!", (60, 220, 120), "Avete eliminato tutti gli impostori!"
    else:
        titolo_txt, colore_fin, sub_txt = "SCONFITTA", (200, 80, 80), "Gli impostori hanno vinto!"

    titolo = FONT_titolo.render(titolo_txt, True, colore_fin)
    schermata.blit(titolo, titolo.get_rect(centerx=LARGHEZZA // 2, top=60))
    sub = FONT_testo.render(sub_txt, True, COLORE_testo)
    schermata.blit(sub, sub.get_rect(centerx=LARGHEZZA // 2, top=180))
    imp = FONT_piccolo.render(f"L'impostore era: {nome_impostore.upper()}", True, (200, 80, 80))
    schermata.blit(imp, imp.get_rect(centerx=LARGHEZZA // 2, top=250))

    posizione_mouse = pygame.mouse.get_pos()
    pulsante_rigioca = pygame.Rect(LARGHEZZA // 2 - PULSANTE_larghezza // 2, 370, PULSANTE_larghezza, PULSANTE_altezza)
    disegna_pulsanti(pulsante_rigioca, "GIOCA ANCORA", pulsante_rigioca.collidepoint(posizione_mouse))
    pulsante_esci = pygame.Rect(LARGHEZZA // 2 - PULSANTE_larghezza // 2, 460, PULSANTE_larghezza, PULSANTE_altezza)
    disegna_pulsanti(pulsante_esci, "ESCI", pulsante_esci.collidepoint(posizione_mouse))

    pygame.display.flip()
    return pulsante_rigioca, pulsante_esci


# ========================================================================
# AGGIUNTE AL LOOP PRINCIPALE
# ========================================================================
# Aggiungi queste variabili nel blocco "GESTIONE DEL LOOP":
#
#   pulsante_inserimento = None
#   pulsante_riepilogo = None
#   pulsanti_voto = []
#   pulsante_risultato = None
#   pulsante_fine_rigioca = None
#   pulsante_fine_esci = None
#
# ──────────────────────────────────────────────────────────────────────
# Nel blocco CLICK DEL MOUSE, dopo "elif schermata_attuale == 'gioco':"
# aggiungi:
#
#       elif schermata_attuale == "inserimento_parola":
#           if pulsante_inserimento and pulsante_inserimento.collidepoint(event.pos):
#               parola = testo_input.strip().lower()
#               nome = ordine_giocatori[indice_inserimento]
#               if parola and parola not in [p.lower() for p in parole_inserite.values()]:
#                   parole_inserite[nome] = parola
#                   testo_input = ""
#                   indice_inserimento += 1
#                   if indice_inserimento >= len(ordine_giocatori):
#                       parolaDaInserire(parole_inserite)   # <-- tua funzione
#                       schermata_attuale = "riepilogo_parole"
#
#       elif schermata_attuale == "riepilogo_parole":
#           if pulsante_riepilogo and pulsante_riepilogo.collidepoint(event.pos):
#               indice_voto = 0
#               voti_inseriti = {}
#               schermata_attuale = "voto"
#
#       elif schermata_attuale == "voto":
#           for btn, candidato in pulsanti_voto:
#               if btn.collidepoint(event.pos):
#                   voti_inseriti[ordine_giocatori[indice_voto]] = candidato
#                   indice_voto += 1
#                   if indice_voto >= len(ordine_giocatori):
#                       lista_voti = votazioni(voti_inseriti)        # <-- tua funzione
#                       lista_eliminati = contaVoti(lista_voti)      # <-- tua funzione
#                       lista_partecipanti = controllaImpostori(lista_eliminati)  # <-- tua funzione
#                       schermata_attuale = "risultato_voto"
#                   break
#
#       elif schermata_attuale == "risultato_voto":
#           if pulsante_risultato and pulsante_risultato.collidepoint(event.pos):
#               # chiama la tua funzione round() per decidere se continuare o finire
#               if len(impostori) > 0 and len(lista_partecipanti) > 2:
#                   parole_inserite = {}
#                   testo_input = ""
#                   indice_inserimento = 0
#                   ordine_giocatori = lista_partecipanti[:]
#                   random.shuffle(ordine_giocatori)
#                   schermata_attuale = "inserimento_parola"
#               elif len(impostori) == 0:
#                   schermata_attuale = "vittoria"
#               else:
#                   schermata_attuale = "sconfitta"
#
#       elif schermata_attuale in ("vittoria", "sconfitta"):
#           if pulsante_fine_rigioca and pulsante_fine_rigioca.collidepoint(event.pos):
#               nomi_giocatori.clear()
#               nome_corrente = ""
#               schermata_attuale = "nomi_giocatori"
#           if pulsante_fine_esci and pulsante_fine_esci.collidepoint(event.pos):
#               pygame.quit()
#               sys.exit()
#
# ──────────────────────────────────────────────────────────────────────
# Nel blocco TASTIERA, aggiungi:
#
#       elif schermata_attuale == "inserimento_parola":
#           if event.key == pygame.K_BACKSPACE:
#               testo_input = testo_input[:-1]
#           elif event.key == pygame.K_RETURN:
#               parola = testo_input.strip().lower()
#               nome = ordine_giocatori[indice_inserimento]
#               if parola and parola not in [p.lower() for p in parole_inserite.values()]:
#                   parole_inserite[nome] = parola
#                   testo_input = ""
#                   indice_inserimento += 1
#                   if indice_inserimento >= len(ordine_giocatori):
#                       parolaDaInserire(parole_inserite)
#                       schermata_attuale = "riepilogo_parole"
#           else:
#               if len(testo_input) < 20:
#                   testo_input += event.unicode
#
# ──────────────────────────────────────────────────────────────────────
# Nel blocco RENDERING, aggiungi dopo "elif schermata_attuale == 'gioco':":
#
#       elif schermata_attuale == "inserimento_parola":
#           pulsante_inserimento = disegna_schermata_inserimento_parola()
#       elif schermata_attuale == "riepilogo_parole":
#           pulsante_riepilogo = disegna_schermata_riepilogo_parole()
#       elif schermata_attuale == "voto":
#           pulsanti_voto = disegna_schermata_voto()
#       elif schermata_attuale == "risultato_voto":
#           pulsante_risultato = disegna_schermata_risultato_voto()
#       elif schermata_attuale == "vittoria":
#           pulsante_fine_rigioca, pulsante_fine_esci = disegna_schermata_fine(True)
#       elif schermata_attuale == "sconfitta":
#           pulsante_fine_rigioca, pulsante_fine_esci = disegna_schermata_fine(False)
#
# ──────────────────────────────────────────────────────────────────────
# Infine, nel blocco "gioco", dove ora hai:
#   if indice_giocatore_corrente >= len(ordine_giocatori):
#       schermata_attuale = "fine_turni"
#
# sostituisci "fine_turni" con "inserimento_parola" e aggiungi prima:
#   parole_inserite = {}
#   testo_input = ""
#   indice_inserimento = 0