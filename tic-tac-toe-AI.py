####	井字遊戲    ####

# 開始;

# 函數定義;

def default():
	# 預設要顯示的信息;
    print("\n歡迎！讓我們一起玩井字遊戲吧！\n")


def rules():
    print("棋盤看起來會像這樣！")
    print("這個 3 x 3 的棋盤位置同您鍵盤右側的數字排列。\n")
    print(" 7 | 8 | 9 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 1 | 2 | 3 ")
    print("\n您只需輸入位置號碼（1-9）。")


def play():
	# 詢問玩家是否準備好;
    return input("\n您準備好玩遊戲了嗎？輸入 [Y]es 或 [N]o。\t").upper().startswith('Y')


def names():
    # 玩家名稱輸入;
    
    p1_name=input("\n請輸入玩家 1 的名稱：\t").capitalize()
    p2_name=input("請輸入玩家 2 的名稱：\t").capitalize()
    return (p1_name, p2_name)


def choice():
    # 玩家選擇輸入;
    p1_choice = ' '
    p2_choice = ' '
    while p1_choice != 'X' or p1_choice != 'O':          # 當輸入的值不是 X 或 O 時;
        
        # WHILE 循環開始

        p1_choice = input(f"\n{p1_name}, 您想選擇 X 還是 O？\t")[0].upper()

        if p1_choice == 'X' or p1_choice == 'O':
            break
        print("無效輸入！請重試！") 

        # WHILE 循環結束

    if p1_choice == 'X':
        p2_choice = 'O'
    elif p1_choice == 'O':
        p2_choice = 'X'
    
    return (p1_choice, p2_choice)


def first_player():
    # 隨機決定誰先開始;
    import random
    return random.choice((0, 1))


def display_board(board, avail):
    print("    " + " {} | {} | {} ".format(board[7],board[8],board[9]) + "            " + " {} | {} | {} ".format(avail[7],avail[8],avail[9]))
    print("    " + "-----------" + "            " + "-----------")
    print("    " + " {} | {} | {} ".format(board[4],board[5],board[6]) + "            " + " {} | {} | {} ".format(avail[4],avail[5],avail[6]))
    print("    " + "-----------" + "            " + "-----------")
    print("    " + " {} | {} | {} ".format(board[1],board[2],board[3]) + "            " + " {} | {} | {} ".format(avail[1],avail[2],avail[3]))


def player_choice(board, name, choice):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input(f'\n{name} ({choice}), 請選擇您的下一個位置：(1-9) \t'))
        
        if position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position) or position == "":
            print(f"無效輸入。請重試！\n")   
    print("\n")        
    return position


# THIS IS THEFUNCTION WHERE AI IS ADDED:
def CompAI(board, name, choice):
    position = 0
    possibilities = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    
    # including both X and O, since if computer will win, he will place a choice there, but if the component will win --> we have to block that move
    for let in ['O', 'X']:
        for i in possibilities:
            # Creating a copy of the board everytime, placing the move and checking if it wins;
            # Creating a copy like this  and not this boardCopy = board, since changes to boardCopy changes the original board;
            boardCopy = board[:]
            boardCopy[i] = let
            if(win_check(boardCopy, let)):
                position = i
                return position

    openCorners = [x for x in possibilities if x in [1, 3, 7, 9]]
    
    if len(openCorners) > 0:
        position = selectRandom(openCorners)
        return position

    if 5 in possibilities:
        position = 5
        return position

    openEdges = [x for x in possibilities if x in [2, 4, 6, 8]]
    
    if len(openEdges) > 0:
        position = selectRandom(openEdges)
        return position



def selectRandom(board):
    import random
    ln = len(board)
    r = random.randrange(0,ln)
    return board[r]


def place_marker(board, avail, choice, position):
    #To mark/replace the position on the board list;
    board[position] = choice
    avail[position] = ' '


def space_check(board, position):
    #To check whether the given position is empty or occupied;
    return board[position] == ' '


def full_board_check(board):
    #To check if the board is full, then the game is a draw;
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def win_check(board, choice):
    #To check if one of the following patterns are true; then the respective player has won!;
    
    #HORIZONTAL CHECK;
    return ( 
       ( board[1] == choice and board[2] == choice and board[3] == choice )
    or ( board[4] == choice and board[5] == choice and board[6] == choice )
    or ( board[7] == choice and board[8] == choice and board[9] == choice )
    #VERTICAL CHECK;
    or ( board[1] == choice and board[4] == choice and board[7] == choice )
    or ( board[2] == choice and board[5] == choice and board[8] == choice )
    or ( board[3] == choice and board[6] == choice and board[9] == choice )
    #DIAGONAL CHECK;
    or ( board[1] == choice and board[5] == choice and board[9] == choice )
    or ( board[3] == choice and board[5] == choice and board[7] == choice )  )

def delay(mode):
    if mode == 2:
        import time
        time.sleep(2)

def replay():
    #If the users want to play the game again?
    return input('\nDo you want to play again? Enter [Y]es or [N]o: ').lower().startswith('y')





#MAIN PROGRAM STARTS;

print("\n\t\t NAMASTE! \n")
input("按 ENTER 鍵開始！")


default()
rules()



while True:
    ####################################################################################
    
    # 創建棋盤作為列表；用來不斷替換用戶輸入；
    theBoard = [' ']*10
    
    # 創建棋盤上可用的選項：
    available = [str(num) for num in range(0,10)] # 列表推導式

    print("\n[0]. 玩家對抗電腦")
    print("[1]. 玩家對抗玩家")
    print("[2]. 電腦對抗電腦")
    mode = int(input("\n選擇一個選項 [0]-[2]: "))
    if mode == 1:
        # 詢問名稱；
        p1_name, p2_name = names()
        # 詢問選擇；顯示選擇；X 或 O；
        p1_choice, p2_choice = choice()
        print(f"\n{p1_name}:", p1_choice)
        print(f"{p2_name}:", p2_choice)

    elif mode == 0:
        p1_name = input("\n輸入將與電腦對戰的玩家名稱：\t").capitalize()
        p2_name = "電腦"
        # 詢問選擇；顯示選擇；X 或 O；
        p1_choice, p2_choice = choice()
        print(f"\n{p1_name}:", p1_choice)
        print(f"{p2_name}:", p2_choice)
    
    else:
        p1_name = "電腦1"
        p2_name = "電腦2"
        p1_choice, p2_choice = "X", "O"
        print(f"\n{p1_name}:", p1_choice)
        print(f"\n{p2_name}:", p2_choice)

    # 隨機打印誰先開始；
    if first_player():
        turn = p2_name
    else:
        turn = p1_name

    print(f"\n{turn} 將先開始！")
    
    # 詢問用戶，是否準備好開始遊戲；輸出將是 True 或 False；
    if(mode == 2):
        ent = input("\n這將會很快！按 Enter 開始戰鬥！\n")
        play_game = 1
    else:
        play_game = play()   
    
    while play_game:
        
        ############################
        # 玩家 1
        if turn == p1_name:
            
            # 顯示棋盤；
            display_board(theBoard, available)

            # 輸入位置；
            if mode != 2:
                position = player_choice(theBoard, p1_name, p1_choice)
            else:
                position = CompAI(theBoard, p1_name, p1_choice)
                print(f'\n{p1_name} ({p1_choice}) 已放置在位置 {position}\n')
            
            # 將 *theBoard* 列表中 *position* 位置的 ' ' 替換為 *p1_choice*；
            place_marker(theBoard, available, p1_choice, position)
            
            # 檢查玩家 1 是否在當前輸入後贏得遊戲；
            if win_check(theBoard, p1_choice):
                display_board(theBoard, available)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                if(mode):
                    print(f'\n\n恭喜 {p1_name}！您贏得了遊戲！\n\n')
                else:
                    print('\n\n電腦贏得了遊戲！\n\n')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                play_game = False
                
            else:
                # 檢查棋盤是否已滿；如果是，則遊戲平局；
                if full_board_check(theBoard):
                    display_board(theBoard, available)
                    print("~~~~~~~~~~~~~~~~~~")
                    print('\n遊戲平局！\n')
                    print("~~~~~~~~~~~~~~~~~~")
                    break
                else:
                    turn = p2_name
                    
        ############################
        # 玩家 2          
        elif turn == p2_name:
            
            # 顯示棋盤；
            display_board(theBoard, available)

            # 輸入位置；
            if(mode == 1):
                position = player_choice(theBoard, p2_name, p2_choice)
            else:
                position = CompAI(theBoard, p2_name, p2_choice)
                print(f'\n{p2_name} ({p2_choice}) 已放置在位置 {position}\n')
            
            # 將 *theBoard* 列表中 *position* 位置的 ' ' 替換為 *p2_choice*；
            place_marker(theBoard, available, p2_choice, position)
            
            # 檢查玩家 2 是否在當前輸入後贏得遊戲；
            if win_check(theBoard, p2_choice):
                display_board(theBoard, available)
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                if(mode):
                    print(f'\n\n恭喜 {p2_name}！您贏得了遊戲！\n\n')
                else:
                    print('\n\n電腦贏得了遊戲！\n\n')
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                play_game = False
                
            else:
                # 檢查棋盤是否已滿；如果是，則遊戲平局；
                if full_board_check(theBoard):
                    display_board(theBoard, available)
                    print("~~~~~~~~~~~~~~~~~~")
                    print('\n遊戲平局！\n')
                    print("~~~~~~~~~~~~~~~~~~")
                    break
                else:
                    turn = p1_name
        
                    
    #If the users want to play the game again?                
    if replay():
        #if Yes;
        continue
    else:
        #if No;
        break
        
    ####################################################################################
    
print("\n\n\t\t\t遊戲結束！")



#END    