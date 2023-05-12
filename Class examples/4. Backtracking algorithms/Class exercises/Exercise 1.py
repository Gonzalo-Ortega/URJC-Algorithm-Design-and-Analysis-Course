# Exercise 1 # UNVERIFIED
# Sea W un conjunto de enteros positivos y M un entero positivo.
# Se pide diseñar e implementar un algoritmo para encontrar rodos
# los subconjuntos de W cuya suma sea exactamente M.

def is_solution(w, m, solution, k):
    summ = 0
    for i in range(k + 1):
        if solution[i] == 1:
            summ += w[i]
    return summ == m


def is_feasible(w, m, solution, k):
    summ = 0
    for i in range(k + 1):
        summ = w[i] * solution[i]
    return summ + w[k] <= m


def subsets_solution(w, m, solution, k):
    if is_solution(w, m, solution, k):
        print(solution)
    else:
        if k <= len(solution) - 1:
            k = k + 1
            subsets_solution(w, m, solution, k)
            if is_feasible(w, m, solution, k):
                pass


def main():
    w = [7, 2, 3, 4, 9]
    m = 9

    solution = [0] * len(w)

    k = -1  # Hasta donde construyo la solución

    subsets_solution(w, m, solution, k)
