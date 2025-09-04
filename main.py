import random

def generate_random_number():
    return round(random.random(), 1)

p = generate_random_number()        # probabilità di vincere la partita

C_0 = 500                           # capitale iniziale

C_Max = 5000000                       # capitale massimo

δ = 10                            # somma fissa da scommettere

P_max = 50000                      # numero massimo di partite giocate

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

def simulate_game(p, C_0, C_Max, δ, P_max):
    C = C_0
    for partita in range(P_max):
        if C >= C_Max:
            print(f"Successo! Capitale raggiunto: {C} dopo {partita} partite.")
            return C
        elif C <= 0:
            print(f"Rovina! Capitale esaurito dopo {partita} partite.")
            return C
        else:
            if random.random() < p:
                C += δ  # Vincita
            else:
                C -= δ  # Perdita
    print(f"Numero massimo di partite raggiunto. Capitale finale: {C}.")
    return C
final_capital = simulate_game(p, C_0, C_Max, δ, P_max)
print(f"Capitale finale del giocatore: {final_capital}")