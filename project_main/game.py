import random


def check_winner(board):
    # 檢查直線
    for x in range(4):
        if board[0][x] == board[1][x] == board[2][x] == board[3][x] != ' ': 
            return True
    # 檢查橫線
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True
    # 檢查對角線
    if board[0][0] == board[1][1] == board[2][2] == board[3][3] != ' ':
        return True
    if board[0][3] == board[1][2] == board[2][1] == board[3][0] != ' ':
        return True

    return False



# 玩家選擇數字
def select_number(player, board):
    while True:
        try:
            print(f"玩家 {player} 的回合:")
            row = int(input("請輸入行數 (1-4): ")) - 1
            col = int(input("請輸入列數 (1-4): ")) - 1
            if board[row][col] == ' ':
                return row, col
            else:
                print("此位置已被選取，請選擇其他位置。")
        except (ValueError, IndexError):
            print("請輸入有效的行列數 (1-4)。")

# 主函數
def main():
    board=[[' ' for _ in range(4)] for _ in range(4)]
    for row in board:
        print('| ' + ' | '.join(row) + ' |')

    player = 1
    while True:
        row, col = select_number(player, board)
        if player == 1:
            board[row][col] = 'X'
        else:
            board[row][col] = 'O'

        for row in board:
            print('| ' + ' | '.join(row) + ' |')

        if check_winner(board) == True:
            print(f"恭喜玩家 {player} 獲勝！")
            break

        if player == 1:
            player = 2
        else:
            player = 1

if __name__ == "__main__":
    main()

