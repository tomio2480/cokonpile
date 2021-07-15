# coding: utf-8

class Othello:
    white = "●"
    black = "◯"

    def __init__(self):
        self.field = list("." * 10)
        self.player = Othello.white

    def show(self):
        print()
        print("".join([str(i) for i in range(10)]))
        print("".join(self.field))
        print()

    def play_turn(self):
        try:
            position = int(input(str(self.player) + " の手番ですー＞" ))
            if not 0 <= position <= 9:
                raise ValueError
            elif self.field[position] != ".":
                raise ValueError
        except Exception as e:
            print("不正な入力です．")
        else:
            self.put(self.player, position)
            self.player = self.enemy_color(self.player)
        
    def put(self, player, position):
        self.field[position] = player
        
        forward = self.field[:position]
        forward.reverse()
        rear = self.field[position+1:]

        try:
            fp = forward.index(self.player)
            fp = len(forward) - fp
            f_range_sl = list(set(self.field[fp:position]))
            if f_range_sl[0] == self.enemy_color(self.player) and len(f_range_sl) == 1:
                self.field[fp:position] = list(self.player * (position - fp))
        except Exception:
            # print("ない")
            pass
        else:
            # print(self.field[position - fp:position])
            pass
            
        try:
            bp = rear.index(self.player)
            b_range_sl = list(set(self.field[position + 1:position + bp + 1]))
            if b_range_sl[0] == self.enemy_color(self.player) and len(b_range_sl) == 1:
                self.field[position + 1:position + bp + 1] = list(self.player * bp)
        except Exception:
            # print("ない")
            pass
        else:
            # print(self.field[position:position + bp])
            pass

    def enemy_color(self, player):
        return Othello.black if player == Othello.white else Othello.white

def main():
    game = Othello()

    while "." in game.field:
        game.show()
        game.play_turn()
    
    game.show()
    
    w = game.field.count(Othello.white)
    b = game.field.count(Othello.black)

    print(Othello.white, w, "個")
    print(Othello.black, b, "個")

    if w == b:
        print("引き分け")
    else:
        print(Othello.white if w > b else Othello.black, "の勝ち")

if __name__ == "__main__":
    main()