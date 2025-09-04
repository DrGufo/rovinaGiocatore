import random

def generate_random_number():
    return round(random.random(), 1)

p = generate_random_number()        # probabilità di vincere la partita

C_0 = 500                           # capitale iniziale

C_Max = 5000000                       # capitale massimo

δ = 10                            # somma fissa da scommettere

P_max = 50000                      # numero massimo di partite giocate

#Simulare il capitale del giocatore nel tempo usando un approccio Monte Carlo: ad ogni passo
#andrà simulato il risultato della singola partita e aggiornato il capitale. Si imposti un numero
#massimo di partite (per evitare cicli infiniti) di almeno 50.000 partite.

C = C_0
n_partite = 0
while C > 0 and C < C_Max and n_partite < P_max:
    if random.random() < p:
        C += δ
    else:
        C -= δ
    n_partite += 1
    if n_partite % 1000 == 0:
        print(f"Partite giocate: {n_partite}, Capitale attuale: {C}")
print(f"Partite giocate: {n_partite}, Capitale finale: {C}")
#Si stampi a video il capitale del giocatore ogni 1000 partite giocate.