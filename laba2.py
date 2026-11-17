import sys

INF = int(1e9)

def print_matrix(matrix, name):
    print(f"\n--- Матриця {name} ---")
    for row in matrix:
        print("".join(f"{('INF' if x >= INF // 2 else str(x)):>5}" for x in row))

def print_path(u, v, next_node):
    if next_node[u][v] == -1:
        print(f"Шляху від {u} до {v} не існує.")
        return
    path = [u]
    current = u
    while current != v:
        current = next_node[current][v]
        path.append(current)
    print("Шлях:", " -> ".join(map(str, path)))

def floyd_warshall(graph):
    V = len(graph)
    dist = [row[:] for row in graph]
    next_node = [[-1 if graph[i][j] == INF or i == j else j for j in range(V)] for i in range(V)]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != INF and dist[k][j] != INF and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    # Перевірка на від'ємні цикли
    has_negative_cycle = any(dist[i][i] < 0 for i in range(V))
    if has_negative_cycle:
        print("\n!!! УВАГА: Граф містить цикл з від'ємною вагою !!!")

    print_matrix(dist, "мінімальних відстаней")
    print_matrix(next_node, "найкоротших шляхів (наступна вершина)")

    if has_negative_cycle:
        print("\nПошук конкретного шляху вимкнено через від'ємний цикл.")
        return

    print("\n--- Пошук шляху для конкретної пари вершин ---")
    while True:
        try:
            u_input = input(f"Введіть початкову вершину (від 0 до {V - 1}, або 'exit' для виходу): ")
            if u_input.lower() == 'exit':
                break
            u = int(u_input)
            v = int(input(f"Введіть кінцеву вершину (від 0 до {V - 1}): "))

            if 0 <= u < V and 0 <= v < V:
                if dist[u][v] >= INF // 2:
                    print("Відстань: Нескінченність (шляху немає)")
                else:
                    print(f"Мінімальна відстань: {dist[u][v]}")
                    print_path(u, v, next_node)
            else:
                print("Некоректні номери вершин!")
        except ValueError:
            print("Помилка: введено некоректні дані. Введіть ціле число.")

if __name__ == "__main__":
    # Варіант 10 (ребро = 1, відсутність ребра = INF)
    variant10_graph = [
        [0,   INF, 1,   1,   1],
        [INF, 0,   INF, 1,   1],
        [1,   INF, 0,   INF, 1],
        [1,   1,   INF, 0,   INF],
        [1,   1,   1,   INF, 0]
    ]

    # Тестовий набір даних 1 (Тест 1 з Додатку 2)
    test1_graph = [
        [0,   INF, INF, INF, INF, INF, INF],
        [INF, 0,   -1,  5,   INF, INF, INF],
        [INF, 4,   0,   3,   INF, -2,  6],
        [7,   INF, -4,  0,   INF, 8,   8],
        [INF, INF, 10,  INF, 0,   INF, 9],
        [12,  INF, INF, 13,  INF, 0,   INF],
        [-5,  INF, 15,  INF, -6,  INF, 0]
    ]

    while True:
        print("\n=========================================")
        print("ЛАБОРАТОРНА РОБОТА №2 (Варіант 10 - Python)")
        print("=========================================")
        print("1. Завдання 1: Запустити Флойда-Уоршелла для Варіанту 10")
        print("2. Завдання 2: Запустити Флойда-Уоршелла для Тесту 2 (Додаток 2)")
        print("0. Вихід")
        
        choice = input("Оберіть дію: ").strip()
        if choice == '0':
            break
        elif choice == '1':
            print("\nВиконання алгоритму для Варіанту 10:")
            floyd_warshall(variant10_graph)
        elif choice == '2':
            print("\nВиконання алгоритму для Тесту 2 (Додаток 2):")
            floyd_warshall(test1_graph)
        else:
            print("Некоректний вибір. Спробуйте ще раз.")
