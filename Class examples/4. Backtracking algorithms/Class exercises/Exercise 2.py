# Dado un conjunto de n enteros, necesitamos decidir si puede ser
# descompuesto en dos subconjuntos disjuntos cuyos elementos sumen la
# misma cantidad. # INCOMPLETE

v = [3, 8, 7, 2, 4]
k = 0
solution = [0] * len(v)

is_sol, sol = summ_bt(v, k, solution)