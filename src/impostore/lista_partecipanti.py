import random

def listaPartecipanti():
    '''La funzione crea una lista contentente i nomi dei partecipanti'''

    while True:
        numero_partecipanti = int(input("inserisci il numero dei partecipanti:"))

        if numero_partecipanti >= 3 and numero_partecipanti <= 15:
            break
    

    for nomi in range(numero_partecipanti):
        nomi = str(input("inserisci il tuo nome:"))


    lista_partecipanti = []
    for i in range(numero_partecipanti):
        nome = str(input("inserisci il tuo nome:"))
        lista_partecipanti.append(nome)

    return lista_partecipanti

lista_nomi = listaPartecipanti()

def paroleGioco():
    '''La funzione crea una lista contenente la parole del gioco'''

    lista_parole_totali = [
    ["PONTE", "Comando", "Denti", "Sospeso"]
    ["CARTA", "Albero", "Fabriano", "Riciclo"]
    ["TESTA", "Corpo", "Uovo", "Pensiero"]
    ["MORTE", "Condanna", "Cigno", "Secca"]
    ["CAMPANA", "Vetro", "Morto", "Doppia"]
    ["COLLO", "Bottiglia", "Piede", "Cigno"]
    ["ORDINE", "Arrivo", "Architetti", "Pubblico"]
    ["SCALA", "Quaranta", "Grigio", "Mercalli"]
    ["BOCCA", "Cucita", "Fuoco", "Verità"]
    ["FILO", "Arianna", "Rasoio", "Perle"]
    ["GIRO", "Vite", "Boa", "Bussola"]
    ["MORSO", "Freno", "Mela", "Rancore"]
    ["PULCE", "Orecchio", "Mercato", "Salto"]
    ["FONDO", "Cassa", "Schiena", "Magazzino"]
    ["LANCIO", "Agenzia", "Disco", "Paracadute"]
    ["SANGUE", "Freddo", "Blu", "Donazione"]
    ["GELO", "Reale", "Cadere", "Rottura"]
    ["VITA", "Stretta", "Mondana", "Smeraldo"]
    ["PESO", "Specifico", "Piuma", "Morto"]
    ["PUNTO", "Croce", "Rottura", "Interrogativo"]
    ["FACCIA", "Bronzo", "Medaglia", "Tosta"]
    ["CORPO", "Reato", "Guardia", "Ballo"]
    ["CHIAVE", "Volta", "Inglese", "Violino"]
    ["PASSO", "Carrabile", "Falso", "Gatto"]
    ["OMBRA", "Governo", "Portata", "Zona"]
    ["BOLLA", "Sapone", "Accompagnamento", "Speculativa"]
    ["VOCE", "Capitolo", "Bianca", "Grosso"]
    ["VENTO", "Rosa", "Favore", "Coda"]
    ["GIOCO", "Forza", "Incastro", "Squadra"]
    ["SALE", "Zucca", "Attico", "Integrale"]
    ["CORDA", "Violino", "Pazzia", "Tesa"]
    ["PEZZO", "Ricambio", "Novanta", "Unico"]
    ["MANO", "Libera", "Morta", "Forchetta"]
    ["QUADRO", "Clinico", "Svedese", "Autore"]
    ["ARIA", "Condizionata", "Castello", "Fritta"]
    ["LINEA", "Confine", "Cortesia", "Condotta"]
    ["FERRO", "Cavallo", "Stiro", "Calza"]
    ["CORTINA", "Ferro", "Fumo", "Ampezzo"]
    ["PUNTA", "Diamante", "Piedi", "Stella"]
    ["PANE", "Cassetta", "Amore", "Spezzato"]
    ["LUME", "Ragione", "Candela", "Naso"]
    ["CATENA", "Montaggio", "Alimentare", "Reazione"]
    ["SCACCO", "Matto", "Re", "Tavoliere"]
    ["SEGNO", "Zodiacale", "Croce", "Tempi"]
    ["FIORE", "Occhiello", "Bach", "Pelle"]
    ["MACCHINA", "Caffè", "Guerra", "Tempo"]
    ["PIANO", "Terra", "Sequenza", "Inclinato"]
    ["COLORE", "Bandiera", "Caldo", "Locale"]
    ["CIRCOLO", "Vizioso", "Polare", "Artistico"]
    ["GRADO", "Parentela", "Separazione", "Alcolico"]
    ["COLPO", "Fulmine", "Spugna", "Sole"]
    ["POLVERE", "Stelle", "Sparo", "Bagnata"]
    ["FORZA", "Maggiore", "Natura", "Bruta"]
    ["PAROLA", "Chiave", "Croce", "Onore"]
    ["BANCO", "Prova", "Scuola", "Nebbia"]
    ["STAGIONE", "Morta", "Saldi", "Sinfonia"]
    ["CANALE", "Radice", "Scolo", "Social"]
    ["PIANETA", "Rossone", "Nano", "Scimmie"]
    ["VERO", "Cuoio", "Nome", "Falso"]
    ["TAVOLO", "Verde", "Rotonda", "Trattativa"]
    ["PALLA", "Prigioniera", "Balzo", "Neve"]
    ["NERO", "Seppia", "Umore", "Cronaca"]
    ["BIANCO", "Natale", "Bandiera", "Latte"]
    ["ROSSO", "Sera", "Labbra", "Rabbia"]
    ["VERDE", "Petrolio", "Speranza", "Pisello"]
    ["NOTTE", "Bianca", "Piccola", "Brava"]
    ["LUCE", "Posizione", "Riflessa", "Gas"]
    ["BOTTONE", "Automatico", "Rosa", "Pancia"]
    ["CAPO", "Espiatorio", "Stato", "Filo"]
    ["PORTA", "Finestra", "Blindata", "Fortuna"]
    ["VISTA", "Punti", "Corto", "Galleria"]
    ["TAGLIO", "Freddo", "Cesareo", "Netto"]
    ["BOTTA", "Risposta", "Calda", "Fortuna"]
    ["BACIO", "Perugina", "Giuda", "Cinema"]
    ["SOGNO", "Americano", "Precloro", "Cassetto"]
    ["STELLA", "Cadente", "Alpina", "Michelin"]
    ["CROCE", "Rossa", "Ferro", "Cavalletta"]
    ["RETE", "Fognaria", "Social", "Letto"]
    ["GOMMA", "Masticare", "Pane", "Bruciata"]
    ["FUOCO", "Amico", "Paglia", "Artificio"]
    ["ACQUA", "Passata", "Santa", "Rubinetto"]
    ["TERRA", "Promessa", "Santa", "Ferma"]
    ["VINO", "Tavola", "Rosso", "Messa"]
    ["LUNA", "Storta", "Miele", "Parco"]
    ["SOLE", "Nero", "Tramonto", "Colpo"]
    ["MARCIA", "Reale", "Ingranaggio", "Funebre"]
    ["CUORE", "Carciofo", "Pietra", "Spezzato"]
    ["PELLE", "Oca", "Diavolo", "Fiore"]
    ["SGUARDO", "Perso", "Intesa", "Orizzonte"]
    ["SPALLA", "Forte", "Comprimario", "Cruda"]
    ["PUNTA", "Piedi", "Stella", "Matita"]
    ["COLLEGAMENTO", "Ipertestuale", "Diretta", "Ponte"]
    ["VALORE", "Assoluto", "Mercato", "Bollato"]
    ["CODA", "Paglia", "Pavone", "Occhio"]
    ["CAMPO", "Minato", "Battaglia", "Fiori"]
    ["BOTTE", "Ferro", "Piena", "Risposta"]
    ["CASA", "Dolce", "Madre", "Bianca"]
    ["GIORNO", "Giudizio", "Memoria", "Lavoro"]
    ["LETTERA", "Morta", "Vettura", "Presentazione"]
    ["LINGUA", "Lunga", "Morta", "Gatto"]
    ["AZIONE", "Cattolica", "Legale", "Titolo"]
    ["BASE", "Dati", "Militare", "Altezza"]
    ["CACCIA", "Tesoro", "Strega", "Grossa"]
    ["CALCIO", "Angolo", "Rigore", "Inizio"]
    ["CAMERA", "Deputati", "Commercio", "Aria"]
    ["CANTO", "Cigno", "Corale", "Libero"]
    ["CAPITALE", "Umana", "Sociale", "Venture"]
    ["CARICO", "Pendente", "Rottura", "Massimo"]
    ["CASO", "Clinico", "Disperato", "Coscienza"]
    ["CERCHIO", "Magico", "Bottiglia", "Fuoco"]
    ["CERVELLO", "Fuga", "Gallina", "Elettronico"]
    ["CHIAMATA", "Carico", "Imbarco", "Diretta"]
    ["CHIESA", "Sconsacrata", "Madre", "Stato"]
    ["CHILO", "Metro", "Grammmo", "Troppo"]
    ["CICLO", "Vitale", "Mercato", "Breve"]
    ["CINTURA", "Sicurezza", "Castità", "Nera"]
    ["CLASSE", "Media", "Ferro", "Operaia"]
    ["CLIENTE", "Abituale", "Fisso", "Sovrano"]
    ["COGNOME", "Nome", "Arte", "Nubile"]
    ["COLONNA", "Ercole", "Vertebrale", "Sonora"]
    ["COMUNE", "Denominatore", "Senso", "Accordo"]
    ["CONTO", "Corrente", "Rovescia", "Arancio"]
    ["COPERTURA", "Nuvolosa", "Assicurativa", "Tetto"]
    ["COPPIA", "Fissa", "Motrice", "Di fatto"]
    ["CORRENTE", "Alternata", "Continua", "Aria"]
    ["CORSA", "Armamenti", "Taxi", "Ostacoli"]
    ["COSTO", "Opportunità", "Vita", "Beneficio"]
    ["COSTRUZIONE", "Diretta", "Passiva", "Abusiva"]
    ["CRISI", "Nervi", "Identità", "Economica"]
    ["CULTURA", "Generale", "Fisica", "Popolare"]
    ["CURVA", "Nord", "Gomito", "Apprendimento"]
    ["DADO", "Tratto", "Brodo", "Gioco"]
    ["DANNO", "Erariale", "Morale", "Collaterale"]
    ["DATO", "Fatto", "Tratto", "Statistico"]
    ["DEBITO", "Ossigeno", "Pubblico", "Riconoscenza"]
    ["DECISIONE", "Arbitrale", "Presa", "Ultima"]
    ["DELITTO", "Onore", "Perfetto", "Castigo"]
    ["DESTINO", "Cinico", "Baro", "Segnato"]
    ["DIFESA", "Ufficio", "Personale", "Oltranza"]
    ["DIMENSIONE", "Ignota", "Terza", "Massima"]
    ["DIRITTO", "Studio", "Autore", "Dovere"]
    ["DISCORSO", "Diretto", "Corona", "Vuoto"]
    ["DISEGNO", "Legge", "Libero", "Animato"]
    ["DISTANZA", "Sicurezza", "Sociale", "Abissale"]
    ["DIVISIONE", "Cellulare", "Meccanica", "Punto"]
    ["DOLCE", "Attesa", "Vita", "Stilnovo"]
    ["DOMANDA", "Offerta", "Retorica", "Risposta"]
    ["DONNA", "Carriera", "Pulizie", "Schermo"]
    ["DOPPIO", "Gioco", "Senso", "Taglio"]
    ["DOVERE", "Cronaca", "Compiuto", "Piacere"]
    ["ECCEZIONE", "Regola", "Sollevata", "Unica"]
    ["EFFETTO", "Serra", "Domino", "Collaterale"]
    ["ELEMENTO", "Disturbo", "Chimico", "Sorpresa"]
    ["ERBA", "Gatta", "Voglio", "Cattiva"]
    ["ERRORE", "Sistema", "Umano", "Stampa"]
    ["ESAME", "Coscienza", "Riparazione", "Ammissione"]
    ["ESPERIENZA", "Limite", "Diretta", "Campo"]
    ["ESPRESSIONE", "Voto", "Viso", "Regolare"]
    ["ESTRATTO", "Conto", "Nascita", "Erbe"]
    ["ETÀ", "Oro", "Ferro", "Ragione"]
    ["FATTO", "Compiuto", "Bene", "Cronaca"]
    ["FEDE", "Nuziale", "Cieca", "Pubblica"]
    ["FIGURA", "Merda", "Retorica", "Spicco"]
    ["FILM", "Luce", "Orrore", "Muto"]
    ["FILTRO", "Aria", "Amore", "Solare"]
    ["FINALE", "Partita", "Ligure", "Sorpresa"]
    ["FINE", "Settimana", "Corsa", "Mondo"]
    ["FIRMA", "Digitale", "Calce", "Autore"]
    ["FISSA", "Dimora", "Idea", "Posto"]
    ["FIUME", "Parole", "Piena", "Carsico"]
    ["FOGLIO", "Via", "Rosa", "Presenze"]
    ["FOLLA", "Oceano", "Delirio", "Solitaria"]
    ["FORMA", "Fisica", "Reato", "Piena"]
    ["FORTUNA", "Cieca", "Sfacciata", "Mare"]
    ["FORZA", "Vendita", "Bruta", "Gravità"]
    ["FOSSA", "Comune", "Leone", "Marianne"]
    ["FOTO", "Tessera", "Gruppo", "Finish"]
    ["FRUTTO", "Bosco", "Stagione", "Peccato"]
    ["FUGA", "Cervelli", "Gas", "Notizie"]
    ["FUNZIONE", "Pubblica", "Rito", "dUso"]
    ["FUTURO", "Prossimo", "Anteriore", "Remoto"]
    ["GAMBA", "Legno", "Tesa", "Quarta"]
    ["GARA", "Appalto", "Solidarietà", "Persa"]
    ["GENERAZIONE", "Fenomeni", "Spontanea", "Futura"]
    ["GENERE", "Umano", "Letterario", "Prima"]
    ["GENTE", "Comune", "Mare", "Bene"]
    ["GESTO", "Atletico", "Consulto", "Disperato"]
    ["GIALLO", "Zafferano", "Paglierino", "Cronaca"]
    ["GIARDINO", "Infanzia", "Segreto", "Pensile"]
    ["GINOCCHIO", "Lavandaia", "Valgo", "Terra"]
    ["GIOCATORE", "Azzardo", "Borsa", "Riserva"]
    ["GIORNATA", "Porte aperte", "Storica", "Lavoro"]
    ["GIOVANE", "Promessa", "Leone", "Dentro"]
    ["GIUDICE", "Pace", "Gara", "Popolare"]
    ["GIUDIZIO", "Universale", "Valore", "Direttissimo"]
    ["GIUNTA", "Comunale", "Regionale", "Nuova"]
    ["GIUSTIZIA", "Sommaria", "Privata", "Divina"]
    ["GOLEADOR", "Bar", "Calcio", "centesimi"]
    ["GOMMA", "Masticare", "Pane", "Ricambio"]
    ["GOVERNO", "Tecnico", "Ombra", "Crisi"]]

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







    

