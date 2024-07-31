import os
import time
import sys
import msvcrt

WIDTH, HEIGHT = 20, 10

snake = [(WIDTH // 2, HEIGHT // 2)]
snake_direction = "RIGHT"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def initialize_game():
    global snake, snake_direction
    snake = [(WIDTH // 2, HEIGHT // 2)]
    snake_direction = "RIGHT"


def move_snake():
    head_x, head_y = snake[0]
    if snake_direction == "UP":
        head_y -= 1
    elif snake_direction == "DOWN":
        head_y += 1
    elif snake_direction == "LEFT":
        head_x -= 1
    elif snake_direction == "RIGHT":
        head_x += 1

    new_head = (head_x, head_y)
    snake.insert(0, new_head)
    snake.pop()


def check_collision():
    head_x, head_y = snake[0]
    if head_x < 1 or head_x >= WIDTH - 1 or head_y < 1 or head_y >= HEIGHT - 1:
        return True
    if (head_x, head_y) in snake[1:]:
        return True
    return False


def print_board():
    clear_screen()
    board = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]

    for x in range(WIDTH):
        board[0][x] = "#"
        board[HEIGHT - 1][x] = "#"
    for y in range(HEIGHT):
        board[y][0] = "#"
        board[y][WIDTH - 1] = "#"

    for x, y in snake:
        if 1 <= x < WIDTH - 1 and 1 <= y < HEIGHT - 1:
            board[y][x] = "*"

    for row in board:
        print("".join(row))
    print("\nUse WASD to move. Press 'q' to quit.")


def get_input():
    global snake_direction
    if msvcrt.kbhit():
        key = msvcrt.getch().decode("utf-8").upper()
        if key == "W" and snake_direction != "DOWN":
            snake_direction = "UP"
        elif key == "S" and snake_direction != "UP":
            snake_direction = "DOWN"
        elif key == "A" and snake_direction != "RIGHT":
            snake_direction = "LEFT"
        elif key == "D" and snake_direction != "LEFT":
            snake_direction = "RIGHT"
        elif key == "Q":
            sys.exit()


def main():
    initialize_game()
    while True:
        get_input()
        move_snake()
        if check_collision():
            print("Game Over!")
            break
        print_board()
        time.sleep(0.5)


if __name__ == "__main__":
    main()
