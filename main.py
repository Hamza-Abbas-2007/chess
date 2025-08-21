import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Chess- Hamza Abbas")

# Create labels to place in grid

x = 0
y = 0


board = [
    ["br","bn","bb","bq","bk","bb","bn","br"],  # row 0
    ["bp","bp","bp","bp","bp","bp","bp","bp"],  # row 1
    ["we","be","we","be","we","be","we","be"],                  # row 2
    ["be","we","be","we","be","we","be","we"],                  # row 3
    ["we","be","we","be","we","be","we","be"],                  # row 4
    ["be","we","be","we","be","we","be","we"],                  # row 5
    ["wp","wp","wp","wp","wp","wp","wp","wp"],  # row 6
    ["wr","wn","wb","wq","wk","wb","wn","wr"]   # row 7
]

pieces = {
    "wp": "P",  # if "P" in your font is a white pawn
    "wr": "R",
    "wn": "N",
    "wb": "B",
    "wq": "Q",
    "wk": "K",
    "bp": "p",
    "br": "r",
    "bn": "n",
    "bb": "b",
    "bq": "q",
    "bk": "k",
    "we": " ",  # empty square
    "be": "+"  # empty square
    }

selected_piece = None
selected_coords = None
def on_click(event, x, y):
    global selected_piece, selected_coords

    if selected_piece is None:
        selected_piece = board[x][y]
        selected_coords = (x, y)
        event.widget.config(bg="yellow")

        if selected_piece == "we" or selected_piece == "be":
            print("You cannot select an empty square.")
            selected_piece = None
            selected_coords = None
            return
        
    else:
        from_x, from_y = selected_coords
        if (x,y) in get_valid_moves(selected_piece, from_x, from_y):
            board[x][y] = selected_piece
            board[from_x][from_y] = "we" if (from_x+from_y) % 2 == 0 else "be"
            selected_piece = None
            selected_coords = None
            draw_board()
        else:
            print("Invalid move.")
            event.widget.config(bg="red")
            selected_piece = None
            selected_coords = None
            draw_board()
            return
    print(f"You clicked square ({x}, {y}) → {board[x][y]}")


def draw_board():
    # clear old widgets
    for widget in root.winfo_children():
        widget.destroy()

    for x in range(8):
        for y in range(8):
            label = tk.Label(root, text=pieces[board[x][y]],
                             bd=1, relief="solid", 
                             font=("CHESS CASES", 32)) 
                             
            label.grid(row=x, column=y, padx=0, pady=0)
            label.bind("<Button-1>", lambda e, x=x, y=y: on_click(e, x, y))

def get_valid_moves(piece, x, y):
    moves = []

    # White pawn
    if piece == "wp":
        # one step forward
        if x > 0 and board[x-1][y] in ("we", "be"):
            moves.append((x-1, y))
        # two steps forward from starting row
        if x == 6 and board[x-1][y] in ("we", "be") and board[x-2][y] in ("we", "be"):
            moves.append((x-2, y))
    return moves


draw_board()
# Run the window
root.mainloop()
