from random import choice
from time import sleep
import tkinter as tk
from tkinter import font

def grid(widget, column, row, pady=10, padx=10, columnspan=1, rowspan=1): widget.grid(column=column, row=row, pady=pady, padx=padx, columnspan=columnspan, rowspan=rowspan)
def Frame(master): return tk.Frame(master=master)
def Label(master, text, text_font=None, text_colour='white'):
    if text_font is None: font.nametofont('TkDefaultFont')
    return tk.Label(master=master, text=text, fg=text_colour, font=text_font)
def Button(master, command, text, text_colour='black'): return tk.Button(master=master, text=text, fg=text_colour, command=command)

canvas = [
    ['', '', ''],
    ['', '', ''],
    ['', '', '']
]

symbol_font = 'Terminal 25 bold'
computer_symbol_gui = 'Ｏ'; computer_symbol_color = 'red'
player_symbol_gui = 'Ｘ'; player_symbol_color = 'SlateBlue2'

computer_symbol_text = 'o'
player_symbol_text = 'x'

window = tk.Tk() ; window.title('Tic Tac Toe (v2-GUI)')

master_frame = Frame(window); grid(master_frame, 0, 0, 20, 20)
tile_frame = Frame(master_frame); grid(tile_frame, 0, 0)

computer_symbol_label = Label(tile_frame, computer_symbol_gui, symbol_font, computer_symbol_color)
player_symbol_label = Label(tile_frame, player_symbol_gui, symbol_font, player_symbol_color)

button_pressed = False
buttons = []

# tile## first number is x coordinate, second is y coordinate - these correspond to tiles on the tkinter grid system
# 00 is top left, 22 is bottom right
# tile##[0] is x, tile##[1] is y
tile00 = (0, 0); tile10 = (2, 0); tile20 = (4, 0)
tile01 = (0, 2); tile11 = (2, 2); tile21 = (4, 2)
tile02 = (0, 4); tile12 = (2, 4); tile22 = (4, 4)

def set_canvas(tile, x, y): canvas[int(tile[x]/2)][int(tile[y]/2)] = 'x'

def set_tile(tile, contents): grid(contents, tile[0], tile[1], 0, 0)

def check_symbol(x, y, symbol):
    if canvas[x][y] == symbol: return True
    else: return False

def check_for_win():
    while True:
        winner = ''

        # computer
        if check_symbol(0, 0, computer_symbol_text) and check_symbol(0, 1, computer_symbol_text) and check_symbol(0, 2, computer_symbol_text): winner = 'Computer'; break # top row
        if check_symbol(1, 0, computer_symbol_text) and check_symbol(1, 1, computer_symbol_text) and check_symbol(1, 2, computer_symbol_text): winner = 'Computer'; break # middle row
        if check_symbol(2, 0, computer_symbol_text) and check_symbol(2, 1, computer_symbol_text) and check_symbol(2, 2, computer_symbol_text): winner = 'Computer'; break # bottom row

        if check_symbol(0, 0, computer_symbol_text) and check_symbol(1, 0, computer_symbol_text) and check_symbol(2, 0, computer_symbol_text): winner = 'Computer'; break # left column
        if check_symbol(0, 1, computer_symbol_text) and check_symbol(1, 1, computer_symbol_text) and check_symbol(2, 1, computer_symbol_text): winner = 'Computer'; break # middle column
        if check_symbol(0, 2, computer_symbol_text) and check_symbol(1, 2, computer_symbol_text) and check_symbol(2, 2, computer_symbol_text): winner = 'Computer'; break # right column

        if check_symbol(0, 0, computer_symbol_text) and check_symbol(1, 1, computer_symbol_text) and check_symbol(2, 2, computer_symbol_text): winner = 'Computer'; break # diagonal top-left to bottom-right
        if check_symbol(0, 2, computer_symbol_text) and check_symbol(1, 1, computer_symbol_text) and check_symbol(2, 0, computer_symbol_text): winner = 'Computer'; break # diagonal bottom-left to top-right

        # player
        if check_symbol(0, 0, player_symbol_text) and check_symbol(0, 1, player_symbol_text) and check_symbol(0, 2, player_symbol_text): winner = 'Player'; break # top row
        if check_symbol(1, 0, player_symbol_text) and check_symbol(1, 1, player_symbol_text) and check_symbol(1, 2, player_symbol_text): winner = 'Player'; break # middle row
        if check_symbol(2, 0, player_symbol_text) and check_symbol(2, 1, player_symbol_text) and check_symbol(2, 2, player_symbol_text): winner = 'Player'; break # bottom row

        if check_symbol(0, 0, player_symbol_text) and check_symbol(1, 0, player_symbol_text) and check_symbol(2, 0, player_symbol_text): winner = 'Player'; break # left column
        if check_symbol(0, 1, player_symbol_text) and check_symbol(1, 1, player_symbol_text) and check_symbol(2, 1, player_symbol_text): winner = 'Player'; break # middle column
        if check_symbol(0, 2, player_symbol_text) and check_symbol(1, 2, player_symbol_text) and check_symbol(2, 2, player_symbol_text): winner = 'Player'; break # right column

        if check_symbol(0, 0, player_symbol_text) and check_symbol(1, 1, player_symbol_text) and check_symbol(2, 2, player_symbol_text): winner = 'Player'; break # diagonal top-left to bottom-right
        if check_symbol(0, 2, player_symbol_text) and check_symbol(1, 1, player_symbol_text) and check_symbol(2, 0, player_symbol_text): winner = 'Player'; break # diagonal bottom-left to top-right

        break

    if winner != '':
        grid(Label(master_frame, f'{winner} Wins!'), 0, 1)
        window.update()
        sleep(3)
        quit()

# return a list of empty tiles that can be used
def get_available_tiles():
    available_tiles = []
    x, y = 0, 0

    for row in canvas:
        for tile in row:
            if tile == '': available_tiles.append((x, y))
            x += 1
        y += 1; x = 0

    return available_tiles

def check_if_tiles_remaining():
    # if the list is empty, `bool(available_tiles())` will return False
    # use `not` to reverse it, so the game quits if there are no more available tiles
    if not bool(get_available_tiles()):
        grid(Label(master_frame, f'Game Over - No Tiles Left'), 0, 1)
        window.update()
        sleep(3)
        quit()

def set_button_pressed():
    global button_pressed
    button_pressed = True

def tile_button(tile):
    global buttons

    btn = Button(tile_frame, lambda:[
        grid(Label(tile_frame, player_symbol_gui, text_colour=player_symbol_color, text_font=symbol_font), tile[0], tile[1]),
        set_canvas(tile, 1, 0),
        btn.grid_remove(),
        window.update(),
        set_button_pressed()
    ], 'Place Here')

    buttons.append(btn)
    return btn

def remove_buttons():
    for button in buttons: button.grid_remove()

def place_dividers():
    divider_tiles_vertical = [(1, 0), (3, 0), (1, 2), (3, 2), (1, 4), (3, 4)]
    for divider in divider_tiles_vertical: grid(Label(tile_frame, '|\n|'), divider[0], divider[1])

    divider_tiles_horizontal = [(0, 1), (0, 3)]
    for divider in divider_tiles_horizontal: grid(Label(tile_frame, '- ' * 40), divider[0], divider[1], columnspan=5)

def players_turn():
    for tile in get_available_tiles(): exec(f'set_tile(tile{tile[0]}{tile[1]}, tile_button(tile{tile[0]}{tile[1]}))')
    window.update()

def computers_turn():
    for button in buttons: button.grid_remove()

    tile = choice(get_available_tiles())
    canvas[tile[1]][tile[0]] = computer_symbol_text

    x, y = 0, 0
    for row in canvas:
        for tile in row:
            if tile == 'o': grid(Label(tile_frame, computer_symbol_gui, symbol_font, computer_symbol_color), x*2, y*2)
            x += 1
        y += 1; x = 0

    window.update()

def main():
    global button_pressed
    while True:
        button_pressed = False
        players_turn()
        while True:
            if button_pressed: break
            window.update()
        remove_buttons()
        check_for_win()
        check_if_tiles_remaining()
        sleep(1)
        computers_turn()
        check_for_win()
        check_if_tiles_remaining()
        sleep(1)

place_dividers()
window.after(1000, main)
window.mainloop()