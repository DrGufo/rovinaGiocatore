import random

def generate_random_number():
    return round(random.random(), 1)

p = generate_random_number()        # probabilità di vincere la partita

C_0 = 500                           # capitale iniziale

C_Max = 1500                       # capitale massimo

δ = 10                            # somma fissa da scommettere

P_max = 50000                      # numero massimo di partite giocate

