import numpy as np

# Função para verificar a viabilidade de uma solução
def is_feasible(solution, constraints, bounds):
    for constraint, bound in zip(constraints, bounds):
        if np.dot(constraint, solution) > bound:
            return False
    return True

# Algoritmo Branch and Bound
def branch_and_bound(profits, constraints, bounds, current_solution=None, best_solution=None, best_profit=0, level=0):
    if current_solution is None:
        current_solution = [0] * len(profits)

    if best_solution is None:
        best_solution = current_solution[:]

    if level == len(profits):
        if is_feasible(current_solution, constraints, bounds):
            current_profit = np.dot(profits, current_solution)
            if current_profit > best_profit:
                best_solution = current_solution[:]
                best_profit = current_profit
        return best_solution, best_profit

    # Ramificação: iterar sobre todos os possíveis valores inteiros para a variável atual
    for value in range(bounds[level] + 1):
        new_solution = current_solution[:]
        new_solution[level] = value

        if is_feasible(new_solution, constraints, bounds):
            best_solution, best_profit = branch_and_bound(profits, constraints, bounds, new_solution, best_solution, best_profit, level + 1)

    return best_solution, best_profit

# Dados do problema
profits = [5, 5, 5]  # Lucros das cervejas A, B, C
constraints = [
    [6, 3, 5],  # Moagem
    [5, 4, 3],  # Aquecimento
    [3, 2, 2],  # Pasteurização
    [0, 0, 1]   # Demanda da cerveja C
]
bounds = [500, 350, 150, 20]  # Limites das restrições

# Resolve o problema usando o algoritmo Branch and Bound
best_solution, best_profit = branch_and_bound(profits, constraints, bounds)

# Imprime os resultados
print("Melhor solução encontrada:")
print("Cerveja A produzida:", best_solution[0])
print("Cerveja B produzida:", best_solution[1])
print("Cerveja C produzida:", best_solution[2])
print("Lucro total:", best_profit)
