import tkinter as tk

root = tk.Tk()
root.title("Tic Tac Toe")

message = tk.Label(root, text="Select Player 1")
message.grid(row=0, column=0, columnspan=3)

def select_player(player):
    global current_player
    current_player = player
    message_label.config(text=f"Player {current_player}'s Turn")
    x_button.config(state="disabled")
    o_button.config(state="disabled")

x_button = tk.Button(root, text="X", command=lambda: select_player("X"))
x_button.grid(row=1, column=0)

o_button = tk.Button(root, text="O", command=lambda: select_player("O"))
o_button.grid(row=1, column=2)

message_label = tk.Label(root, text="Please select a player to start", font=('Times New Roman', 16))
message_label.grid(row=2, column=0, columnspan=3)

buttons = []
board = [["" for _ in range(3)] for _ in range(3)]

def on_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "" and not check_winner():
        buttons[row][col]["text"] = current_player
        board[row][col] = current_player

        if check_winner():
            message_label.config(text=f"(●'◡'●) Player {current_player} wins!")
            disable_buttons()
        elif is_draw():
            message_label.config(text="(⊙_⊙;)It's a draw!")
            disable_buttons()
        else:
            current_player = "O" if current_player == "X" else "X"
            message_label.config(text=f"Player {current_player}'s Turn")

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False

def is_draw():
    return all(board[row][col] != "" for row in range(3) for col in range(3))

def disable_buttons():
    for row in range(3):
        for col in range(3):
            buttons[row][col]["state"] = "disabled"

def reset_board():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = ""
            buttons[row][col]["state"] = "normal"
    message_label.config(text="Player X's Turn")
    x_button.config(state="normal")
    o_button.config(state="normal")

for row in range(3):
    button_row = []
    for col in range(3):
        btn = tk.Button(root, text="", font=('Helvetica', 20), width=5, height=2,
                        command=lambda r=row, c=col: on_click(r, c))
        btn.grid(row=row+3, column=col)
        button_row.append(btn)
    buttons.append(button_row)

reset_button = tk.Button(root, text="Reset Game", font=('Helvetica', 12), command=reset_board)
reset_button.grid(row=6, column=1, columnspan=1)

root.mainloop()
