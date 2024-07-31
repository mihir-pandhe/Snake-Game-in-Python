import random
import os
import time
import sys
import msvcrt

WIDTH, HEIGHT = 20, 10

snake = [(WIDTH // 2, HEIGHT // 2)]
snake_direction = "RIGHT"
food = (random.randint(1, WIDTH - 2), random.randint(1, HEIGHT - 2))
score = 0
speed = 0.5


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def initialize_game():
    global snake, snake_direction, food, score, speed
    snake = [(WIDTH // 2, HEIGHT // 2)]
    snake_direction = "RIGHT"
    food = (random.randint(1, WIDTH - 2), random.randint(1, HEIGHT - 2))
    score = 0
    speed = 0.5


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

    if new_head == food:
        place_food()
        update_score()
    else:
        snake.pop()


def check_collision():
    head_x, head_y = snake[0]
    if head_x < 1 or head_x >= WIDTH - 1 or head_y < 1 or head_y >= HEIGHT - 1:
        return True
    if (head_x, head_y) in snake[1:]:
        return True
    return False


def place_food():
    global food
    food = (random.randint(1, WIDTH - 2), random.randint(1, HEIGHT - 2))
    while food in snake:
        food = (random.randint(1, WIDTH - 2), random.randint(1, HEIGHT - 2))


def update_score():
    global score, speed
    score += 10
    speed = max(0.1, 0.5 - score / 1000)


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

    fx, fy = food
    board[fy][fx] = "O"

    for row in board:
        print("".join(row))
    print(
        f"\nScore: {score} | Speed: {1/speed:.2f} | Use WASD to move. Press 'Q' to quit."
    )


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
        time.sleep(speed)


if __name__ == "__main__":
    main()
