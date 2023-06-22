import copy
from typing import Optional

import pygame
import sys
import random
from constants import *
import numpy as np

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE AI')
screen.fill(BG_COLOUR)


class Board:
    def __init__(self):
        self.squares = np.zeros((BOARD_ROWS, BOARD_COLS))
        # argument needs to be a tuple! ()
        self.empty_sqrs = self.squares  # creation of a list
        self.marked_sqrs = 0

    def mark_square(self, row, col, player):
        """to mark a square and to know number of marked sq"""
        self.squares[row][col] = player
        self.marked_sqrs += 1

    def available_square(self, row, col):
        return self.squares[row][col] == 0

    def is_full(self):
        return self.marked_sqrs == 9

    def is_empty(self):
        return self.marked_sqrs == 0

    def get_empty_sqrs(self) -> list[tuple]:
        empty_sqrs = []
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if self.available_square(row, col):
                    empty_sqrs.append(row, col)
        return empty_sqrs

    def final_state(self, show=False) -> int:

        """return 0 if there is no win yet (doesnt mean a tie)
           return 1 if player1 wins
           return 2 i player2 wins"""

        # vertical wins
        for col in range(BOARD_COLS):
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                # draw_vertical_winning_line(col, player)
                if show:
                    color = CIRCLE_COLOUR if self.squares[0][col] == 2 else CROSS_COLOUR
                    start_pos = (col * SQ_SIZE + SQ_SIZE // 2, 20)
                    end_pos = (col * SQ_SIZE + SQ_SIZE // 2, HEIGHT - 20)
                    pygame.draw.line(screen, color, start_pos, end_pos, LINE_WIDTH)
                return self.squares[0][col]  # return a player (if player 1 it returns number 1)

        # horizontal win check
        for row in range(BOARD_ROWS):
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                # draw_horizontal_winning_line(row, player)
                if show:
                    color = CIRCLE_COLOUR if self.squares[0][col] == 2 else CROSS_COLOUR
                    start_pos = (20, row * SQ_SIZE + SQ_SIZE // 2)
                    end_pos = (WIDTH - 20, row * SQ_SIZE + SQ_SIZE // 2)
                    pygame.draw.line(screen, color, start_pos, end_pos, LINE_WIDTH)
                return self.squares[row][0]

        # check for diagonals win
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            # draw_desc_diagonal_win_line(player)
            if show:
                color = CIRCLE_COLOUR if self.squares[0][col] == 2 else CROSS_COLOUR
                start_pos = (20, 20)
                end_pos = (WIDTH - 20, HEIGHT - 20)
                pygame.draw.line(screen, color, start_pos, end_pos, LINE_WIDTH)
            return self.squares[0][0]

        if self.squares[0][2] == self.squares[1][1] == self.squares[2][0] != 0:
            # draw_asc_diagonal_win_line(player)
            if show:
                color = CIRCLE_COLOUR if self.squares[0][col] == 2 else CROSS_COLOUR
                start_pos = (20, HEIGHT - 20)
                end_pos = (WIDTH - 20, 20)
                pygame.draw.line(screen, color, start_pos, end_pos, LINE_WIDTH)
            return self.squares[0][2]
        return 0


class AI:
    """ implements counter player random or minimax"""

    def __init__(self, level=1, player=2):
        self.player = player
        self.level = level

    def random_choice(self, board):
        empty_sqrs = board.get_empty_sqrs()
        indx = random.randrange(0, len(empty_sqrs))
        return empty_sqrs[indx]  # (row,col)

    def minimax(self, board: Board, maximazing: bool) -> tuple[int, Optional[tuple]]:

        """ AI is minimizing (player 2)"""

        # terminal cases
        case = board.final_state()
        # player 1 wins:
        if case == 1:
            return 1, None
        # AI (player 2) wins:
        elif case == 2:
            return -1, None

        elif board.is_full():
            return 0, None

        if maximazing:
            # initialization with any big number
            max_eval = -100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for row, col in empty_sqrs:
                # to create new board:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, 1)  # player 1
                eval = self.minimax(temp_board, False)[0]  # [0] we want return value of eval not move
                if eval > max_eval:
                    max_eval = eval
                    best_move = (row, col)

            return max_eval, best_move

        elif not maximazing:
            min_eval = 100
            best_move = None
            empty_sqrs = board.get_empty_sqrs()

            for row, col in empty_sqrs:
                temp_board = copy.deepcopy(board)
                temp_board.mark_square(row, col, self.player)
                eval = self.minimax(temp_board, True)[0]
                if eval < min_eval:
                    min_eval = eval
                    best_move = row, col

            return min_eval, best_move

    def evaluation(self, main_board) -> tuple:

        if self.level == 0:
            eval = "random"
            move = self.random_choice(main_board)
        else:
            # minimax algorithm choice
            eval, move = self.minimax(main_board, False)

        print(f"AI has chosen to marked the square in pos {move} with an eval of {eval}")

        return move


class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()
        self.player = 1
        self.game_mode = "ai"  # or pvp
        self.running = True
        self.draw_lines()

    def draw_lines(self):
        # bug fix for reset, paint the screen
        screen.fill(BG_COLOUR)

        # 1 horizontale line
        pygame.draw.line(screen, LINE_COLOUR, (0, 200), (600, 200), LINE_WIDTH)

        # 2 horizontale line
        pygame.draw.line(screen, LINE_COLOUR, (0, 400), (600, 400), LINE_WIDTH)

        # 1 vertical line
        pygame.draw.line(screen, LINE_COLOUR, (200, 0), (200, 600), LINE_WIDTH)

        # 2 vertical line
        pygame.draw.line(screen, LINE_COLOUR, (400, 0), (400, 600), LINE_WIDTH)

    def draw_figures(self, row, col):
        center = ((int(col * SQ_SIZE + SQ_SIZE / 2)), (int(row * SQ_SIZE + SQ_SIZE / 2)))
        if self.player == 1:
            pygame.draw.line(screen, CROSS_COLOUR, (col * SQ_SIZE + CROSS_SPACE, row * SQ_SIZE + SQ_SIZE - CROSS_SPACE),
                             (col * SQ_SIZE + SQ_SIZE - CROSS_SPACE, row * SQ_SIZE + CROSS_SPACE), CROSS_WIDTH)
            pygame.draw.line(screen, CROSS_COLOUR, (col * SQ_SIZE + CROSS_SPACE, row * SQ_SIZE + CROSS_SPACE),
                             (col * SQ_SIZE + SQ_SIZE - CROSS_SPACE, row * SQ_SIZE + SQ_SIZE - CROSS_SPACE),
                             CROSS_WIDTH)

        elif self.player == 2:
            pygame.draw.circle(screen, CIRCLE_COLOUR, center, CIRCLE_RAD, CIRCLE_WIDTH)

    def next_turn(self):
        self.player = (self.player % 2) + 1
        # if player 1 -- 1%2=1  1+1=2
        # if player 2 -- 2%2=0 0+1=1

    def make_move(self, row, col):
        self.board.mark_square(row, col, self.player)
        self.draw_figures(row, col)
        self.next_turn()

    def change_gamemode(self):
        self.game_mode = "ai" if self.game_mode == "pvp" else "pvp"

    def reset(self):
        # value reset
        self.__init__()

    def is_over(self):
        return self.board.final_state(show=True) != 0 or self.board.is_full()


def main():
    # OBJCET

    game = Game()
    board = game.board
    ai = game.ai

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                # reset fce
                if event.key == pygame.K_r:
                    game.reset()
                    board = game.board  # we create new clean board
                    ai = game.ai

                # change to play player vs player
                if event.key == pygame.K_g:
                    game.change_gamemode()

                # if level == 0 - play ai mode (basic setting)
                if event.key == pygame.K_0:
                    ai.level = 0

                # if level == 1 - play random mode
                if event.key == pygame.K_1:
                    ai.level = 1

            # FCE for checking if we click the screen
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_X = event.pos[0]  # X
                mouse_Y = event.pos[1]  # Y

                row = int(mouse_Y // SQ_SIZE)
                col = int(mouse_X // SQ_SIZE)

                if board.available_square(row, col):
                    game.make_move(row, col)
                    if game.is_over():
                        game.running = False

        if game.game_mode == "ai" and game.player == ai.player and game.running:
            # update the screen
            pygame.display.update()

            # ai methods
            row, col = ai.evaluation(board)
            game.make_move(row, col)

            if game.is_over():
                game.running = False

        pygame.display.update()


main()
