import random

def generate_random_number():
    return round(random.random(), 1)

C_0 = 500                           # capitale iniziale
C_Max = 500000                      # capitale massimo
δ = 10                              # somma fissa da scommettere
P_max = 50000                       # numero massimo di partite giocate

def play_game():
    C = C_0
    partita = 0
    max_capitale_raggiunto = C      # traccia il capitale massimo raggiunto

    while C > 0 and C < C_Max and partita < P_max:
        partita += 1
        win_prob = 1.0
        if random.random() < win_prob:
            C += δ
            print(f"Partita {partita}: Hai vinto! Capitale attuale: {C} (Vinto: {δ}) | Probabilità di vincita: {win_prob:.1f}")
        else:
            C -= δ
            print(f"Partita {partita}: Hai perso! Capitale attuale: {C} (Perso: {δ}) | Probabilità di vincita: {win_prob:.1f}")
        if C > max_capitale_raggiunto:
            max_capitale_raggiunto = C

    if C >= C_Max:
        print(f"Hai raggiunto il capitale massimo di {C_Max} in {partita} partite!")
    elif C <= 0:
        print(f"Hai perso tutto il capitale in {partita} partite.")
        print(f"Il capitale massimo raggiunto durante le partite è stato: {max_capitale_raggiunto}")
    else:
        print(f"Hai raggiunto il numero massimo di partite ({P_max}) con un capitale di {C}.")
        print(f"Il capitale massimo raggiunto durante le partite è stato: {max_capitale_raggiunto}")
    return C

final_capital = play_game()
print(f"Capitale finale: {final_capital}")