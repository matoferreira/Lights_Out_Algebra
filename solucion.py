import numpy as np

def lights_out_resolver(board):
    num_rows_board = len(board)
    num_rows = num_rows_board * num_rows_board
    lights_out_matrix = matriz_toggle(num_rows_board)
    entries = get_entries(board)
    entries = entries.transpose()
    entries.resize(num_rows, 1)
    augmented_matrix = np.hstack((lights_out_matrix, entries))
    remove_zeros(augmented_matrix, num_rows)
    sustitution(augmented_matrix, num_rows)
    solution = augmented_matrix[:, -1]
    solution = solution.reshape((num_rows_board, num_rows_board))
    return solution

def matriz_toggle(num_rows_board):
    num_rows = num_rows_board * num_rows_board
    toggle_matrix = np.zeros((num_rows, num_rows), dtype=int)
    for i in range(num_rows):
        for j in range(num_rows):
            set_matriz_toggle_element(toggle_matrix, i, j, num_rows_board)
    return toggle_matrix

def set_matriz_toggle_element(toggle_matrix, i, j, num_rows_board):
    if i == j:
        toggle_matrix[i, j] = 1
    elif (i // num_rows_board == j // num_rows_board and abs(i - j) == 1) or (i % num_rows_board == j % num_rows_board and abs(i - j) == num_rows_board):
        toggle_matrix[i, j] = 1

def get_entries(board):
    return np.array(board).flatten()

def remove_zeros(augmented_matrix, num_rows):
    for row in range(num_rows - 1):
        if augmented_matrix[row, row] == 0:
            swap_row(augmented_matrix, row)
        for i in range(row + 1, num_rows):
            if augmented_matrix[i, row] == 1:
                augmented_matrix[i] = (augmented_matrix[i] + augmented_matrix[row]) % 2

def swap_row(augmented_matrix, row):
    non_zero_row = np.argmax(augmented_matrix[row + 1 :, row])
    augmented_matrix[[row, non_zero_row + row + 1]] = augmented_matrix[[non_zero_row + row + 1, row]]

def sustitution(augmented_matrix, num_rows):
    for col in range(num_rows - 1, 0, -1):
        for i in range(col - 1, -1, -1):
            if augmented_matrix[i, col] == 1:
                augmented_matrix[i] = (augmented_matrix[i] + augmented_matrix[col]) % 2


#Susstituir el array colocando cada fila del tablero de juego como un vector lineal
#Matriz 3x3
print(lights_out_resolver(np.array([[0, 1, 1], [0, 0, 1], [0, 1, 1]])))

#Matriz 4x4
#print(lights_out_resolver(np.array([[1, 0, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 0, 0]])))

#Matriz 5x5
#print(lights_out_resolver(np.array([[0, 0, 1, 1, 1], [0, 1, 1, 1, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 1, 0, 0, 1]])))
