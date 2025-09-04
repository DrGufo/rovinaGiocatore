import random

def generate_random_number():
    return round(random.random(), 1)

p = generate_random_number()        # probabilità di vincere la partita

C_0 = 500                           # capitale iniziale

C_Max = 5000000                       # capitale massimo

δ = 10                            # somma fissa da scommettere

P_max = 50                    # numero massimo di partite giocate

'''3.1 SCENARIO
Un giocatore d’azzardo parte con un capitale iniziale C_0 e gioca una serie di partite indipendenti con
esito dicotomico. In ogni partita:
 Il giocatore può vincere o perdere una somma fissa δ (ad esempio, 1 unità).
 La probabilità di vincere una singola partita è p (con 0<p<1).
Il giocatore continua a giocare fino a quando:
 Raggiunge un capitale massimo prefissato C_max (successo).
 Perde tutto il capitale (rovina).
3.2 OBIETTIVO
1. Simulare il capitale del giocatore nel tempo usando un approccio Monte Carlo: ad ogni passo
andrà simulato il risultato della singola partita e aggiornato il capitale. Si imposti un numero
massimo di partite (per evitare cicli infiniti) di almeno 50.000 partite.'''

#stampa esito partita, capitale attuale e vinto ad ogni partita

def play_game():
    C = C_0
    partita = 0

    while C > 0 and C < C_Max and partita < P_max:
        partita += 1
        if random.random() < p:
            C += δ
            print(f"Partita {partita}: Hai vinto! Capitale attuale: {C} (Vinto: {δ})")
        else:
            C -= δ
            print(f"Partita {partita}: Hai perso! Capitale attuale: {C} (Perso: {δ})")

    if C >= C_Max:
        print(f"Hai raggiunto il capitale massimo di {C_Max} in {partita} partite!")
    elif C <= 0:
        print(f"Hai perso tutto il capitale in {partita} partite.")
    else:
        print(f"Hai raggiunto il numero massimo di partite ({P_max}) con un capitale di {C}.")
        return C
    return C
final_capital = play_game()
print(f"Capitale finale: {final_capital}")