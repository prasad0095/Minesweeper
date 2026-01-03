import random

ROWS = 8
COLS = 8
MINES = 10

# Game boards
board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
visible = [["■" for _ in range(COLS)] for _ in range(ROWS)]
revealed = [[False for _ in range(COLS)] for _ in range(ROWS)]

game_over = False


def place_mines():
    count = 0
    while count < MINES:
        r = random.randint(0, ROWS - 1)
        c = random.randint(0, COLS - 1)
        if board[r][c] != -1:
            board[r][c] = -1
            count += 1


def calculate_numbers():
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == -1:
                continue
            mines = 0
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS:
                        if board[nr][nc] == -1:
                            mines += 1
            board[r][c] = mines


def display_board():
    print("\n   ", end="")
    for i in range(COLS):
        print(i, end=" ")
    print("\n")

    for i in range(ROWS):
        print(i, "|", end=" ")
        for j in range(COLS):
            print(visible[i][j], end=" ")
        print()


def reveal_cell(r, c):
    if r < 0 or r >= ROWS or c < 0 or c >= COLS:
        return
    if revealed[r][c]:
        return

    revealed[r][c] = True

    if board[r][c] == 0:
        visible[r][c] = " "
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                reveal_cell(r + dr, c + dc)
    else:
        visible[r][c] = str(board[r][c])


def check_win():
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] != -1 and not revealed[r][c]:
                return False
    return True


def game_loop():
    global game_over
    place_mines()
    calculate_numbers()

    while not game_over:
        display_board()

        try:
            r = int(input("\nEnter row: "))
            c = int(input("Enter column: "))
        except ValueError:
            print("Invalid input!")
            continue

        if r < 0 or r >= ROWS or c < 0 or c >= COLS:
            print("Out of bounds!")
            continue

        if board[r][c] == -1:
            print("\n💣 BOOM! You hit a mine.")
            for i in range(ROWS):
                for j in range(COLS):
                    if board[i][j] == -1:
                        visible[i][j] = "*"
            display_board()
            game_over = True
            break

        reveal_cell(r, c)

        if check_win():
            print("\n🎉 Congratulations! You won the game!")
            display_board()
            break


if __name__ == "__main__":
    print("=== MINESWEEPER (Python) ===")
    game_loop()
