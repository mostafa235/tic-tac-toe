import random
the_border={'1':" ",'2':" ",'3':" ",'4':" ",'5':" ",'6':" ",'7':" ",'8':" ",'9':" "}
border_key=[]
for key in the_border:
	border_key.append(key)
def print_border(border):
	print(border['1']+" |"+border['2']+' |'+border['3'])
	print("--+--+--")
	print(border['4']+" |"+border['5']+' |'+border['6'])
	print("--+--+--")
	print(border['7']+" |"+border['8']+' |'+border['9'])
def chose_turn(choise):
	if choise=="1":
		move=str(input())
		return move
	else:
		move=str(random.randrange(1,10))
		return move
def game():
	player="x"
	count=0
	print("Do you want to be player 1  (click 1 )or player 2 (click 2)")
	choice=input()
	for i in range(100):
		print_border(the_border)
		print(f"player {player} its your turn")
		move = chose_turn(choice)
		if the_border[move]==" ":
			the_border[move] = player
			count+=1
		else:
			print("the place is aiready filled")
			continue
		if count>=5:

			if the_border["1"]==the_border['2']==the_border["3"]!=" ":
				print_border(the_border)
				print("player "+player+" won")
				print("game over")
				break
			elif the_border["4"]==the_border["5"]==the_border['6']!=" ":
				print_border(the_border)
				print("player "+player+" won")
				print("game over")
				break
			elif the_border['7']==the_border['8']==the_border['9']!=" ":
				print_border(the_border)
				print("player "+player+" won")
				print("game over")
				break
			elif the_border['1']==the_border['5']==the_border['9']!=" ":
				print_border(the_border)
				print("player "+player+" won")
				print("game over")
				break
			elif the_border['3']==the_border['5']==the_border['7']!=" ":
				print_border(the_border)
				print("player "+player+" won")
				print("game over")
				break
			elif the_border['3']==the_border['6']==the_border['9']!=" ":
				print_border(the_border)
				print("player "+player+" won")
				print("game over")
				break
			elif the_border['1']==the_border['4']==the_border['7']!=" ":
				print_border(the_border)
				print("player "+player+" won")
				print("game over")
				break
			elif the_border['2']==the_border['5']==the_border['8']!=" ":
				print_border(the_border)
				print("player "+player+" won")
				print("game over")
				break


		if count==9:
			print("Game over")
			print("its a tie")
			break
		if player=="x" or player=="X":
			player="o"
		else:
			player="x"
		if choice=="1":
			choice="2"
		else:
			choice="1"
	restart_play=input("do you want play again")
	if restart_play=="yes" or restart_play=="Yes":
			for play in border_key:
				the_border[play]=" "
			game()




