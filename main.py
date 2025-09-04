import random

def generate_random_number():
    return round(random.random(), 1)

p = generate_random_number()        # probabilità di vincere la partita

C_0 = 500                           # capitale iniziale
C_Max = 5000000                     # capitale massimo
δ = 10                              # somma fissa da scommettere
P_max = 50                          # numero massimo di partite giocate

def play_game():
    C = C_0
    partita = 0

    while C > 0 and C < C_Max and partita < P_max:
        partita += 1
        win_prob = p  # probabilità di vincita per questa partita
        if random.random() < win_prob:
            C += δ
            print(f"Partita {partita}: Hai vinto! Capitale attuale: {C} (Vinto: {δ}) | Probabilità di vincita: {win_prob:.1f}")
        else:
            C -= δ
            print(f"Partita {partita}: Hai perso! Capitale attuale: {C} (Perso: {δ}) | Probabilità di vincita: {win_prob:.1f}")

    if C >= C_Max:
        print(f"Hai raggiunto il capitale massimo di {C_Max} in {partita} partite!")
    elif C <= 0:
        print(f"Hai perso tutto il capitale in {partita} partite.")
    else:
        print(f"Hai raggiunto il numero massimo di partite ({P_max}) con un capitale di {C}.")
    return C

final_capital = play_game()
print(f"Capitale finale: {final_capital}")
