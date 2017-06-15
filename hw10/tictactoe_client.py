import Tkinter as tk
import sys
import socket

PLAYER1 = "PLAYER1"
PLAYER2 = "PLAYER2"
O = "O"
X = "X"
BLANK = ""

class TicTacToeFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.turn = PLAYER1
        self.board = []
        for i in range(3):
            l = []
            line = tk.Frame(self)
            line.pack()
            for j in range(3):
                button_text = tk.StringVar(line, BLANK)
                button = tk.Button(line, textvariable = button_text, width = 1, command = self.press(i, j))
                button.pack(side = tk.LEFT)
                l.append(["", button_text, button])
            self.board.append(l)

    def press(self, i, j):
        def real_press():
            #local change
            self.board[i][j][1].set(O)
            self.board[i][j][0] = O
            self.board[i][j][2].config(state = 'disabled')
            #send
            z = str(i) + " " + str(j)
            z = str.encode(z)
            s.send(z)
            if self.check_status():
                for m in range(3):
                    for n in range(3):
                        self.board[m][n][2].config(state = 'disabled')
            #Receive
            z = str.decode(s.recv(1024))
            x, y = int(z[0]), int(z[2])
            self.board[x][y][1].set(X)
            self.board[x][y][0] = X
            self.board[x][y][2].config(state = 'disabled')
            if self.check_status():
                for m in range(3):
                    for n in range(3):
                        self.board[m][n][2].config(state = 'disabled')
        return real_press

    def check_status(self):
        if self.board[0][0][0] == self.board[0][1][0] == self.board[0][2][0] and self.board[0][0][0] != BLANK and self.board[0][1][0] != BLANK and self.board[0][2][0] != BLANK:
            self.board[0][0][2].config(disabledforeground = 'red')
            self.board[0][1][2].config(disabledforeground = 'red')
            self.board[0][2][2].config(disabledforeground = 'red')
            return True
        elif self.board[1][0][0] == self.board[1][1][0] == self.board[1][2][0] and self.board[1][0][0] != BLANK and self.board[1][1][0] != BLANK and self.board[1][2][0] != BLANK:
            self.board[1][0][2].config(disabledforeground = 'red')
            self.board[1][1][2].config(disabledforeground = 'red')
            self.board[1][2][2].config(disabledforeground = 'red')
            return True
        elif self.board[2][0][0] == self.board[2][1][0] == self.board[2][2][0] and self.board[2][0][0] != BLANK and self.board[2][1][0] != BLANK and self.board[2][2][0] != BLANK:
            self.board[2][0][2].config(disabledforeground = 'red')
            self.board[2][1][2].config(disabledforeground = 'red')
            self.board[2][2][2].config(disabledforeground = 'red')
            return True
        elif self.board[0][0][0] == self.board[1][0][0] == self.board[2][0][0] and self.board[0][0][0] != BLANK and self.board[1][0][0] != BLANK and self.board[2][0][0] != BLANK:
            self.board[0][0][2].config(disabledforeground = 'red')
            self.board[1][0][2].config(disabledforeground = 'red')
            self.board[2][0][2].config(disabledforeground = 'red')
            return True
        elif self.board[0][1][0] == self.board[1][1][0] == self.board[2][1][0] and self.board[0][1][0] != BLANK and self.board[1][1][0] != BLANK and self.board[2][1][0] != BLANK:
            self.board[0][1][2].config(disabledforeground = 'red')
            self.board[1][1][2].config(disabledforeground = 'red')
            self.board[2][1][2].config(disabledforeground = 'red')
            return True
        elif self.board[0][2][0] == self.board[1][2][0] == self.board[2][2][0] and self.board[0][2][0] != BLANK and self.board[1][2][0] != BLANK and self.board[2][2][0] != BLANK:
            self.board[0][2][2].config(disabledforeground = 'red')
            self.board[1][2][2].config(disabledforeground = 'red')
            self.board[2][2][2].config(disabledforeground = 'red')
            return True
        elif self.board[0][0][0] == self.board[1][1][0] == self.board[2][2][0] and self.board[0][0][0] != BLANK and self.board[1][1][0] != BLANK and self.board[2][2][0] != BLANK:
            self.board[0][0][2].config(disabledforeground = 'red')
            self.board[1][1][2].config(disabledforeground = 'red')
            self.board[2][2][2].config(disabledforeground = 'red')
            return True
        elif self.board[0][2][0] == self.board[1][1][0] == self.board[2][0][0] and self.board[0][2][0] != BLANK and self.board[1][1][0] != BLANK and self.board[2][0][0] != BLANK:
            self.board[0][2][2].config(disabledforeground = 'red')
            self.board[1][1][2].config(disabledforeground = 'red')
            self.board[2][0][2].config(disabledforeground = 'red')
            return True
        else:
            return False

if __name__ == "__main__":
    HOST = '127.0.0.1' # The remote host
    PORT = 50008 # The same port as used by the server
    s = None
    for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except OSError as msg:
            s = None
            continue
        try:
            s.connect(sa)
        except OSError as msg:
            s.close()
            s = None
            continue
        break
    if s is None:
        print('could not open socket')
        sys.exit(1)

    window = tk.Tk()
    app = TicTacToeFrame(window)
    app.pack()
    window.mainloop()
