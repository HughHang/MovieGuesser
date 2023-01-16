#My two sub genres are Anime and Super-Hero

#Anime movies: 
#1.Your Name 
#2.Weathering With You
#3.I Wanna Eat Your Pancreas 
#4.A Silent Voice
#5.Howl's Moving Castle
#6.Spirited Away
#7.My Neighbor Totoro
#8.My Hero Academia
#9.Demon Slayer: Mugen Train
#10.Road to Ninja: Naruto the Movie

#Super-Hero movies:
#1.Justice League
#2.Super-Man: Man of Steel
#3.Shazam 
#4.Deadpool
#5.Venom
#6.Spider-Man: Into the Spider-Verse
#7.Sonic: The Hedgehog
#8.Avengers: Endgame
#9.The Incredible Hulk
#10.Black Widow



import sys

#Welcome to game
print("\nWelcome to Movie Guesser! \nI would like to invite you to choose a movie out of these twenty movies:")

print("___________________ \n")

#Give options
print("Your Name \nWeathering With You \nI Wanna Eat Your Pancreas \nA Silent Voice \nHowl's Moving Castle \nSpirited Away \nMy Neighbor Totoro \nMy Hero Academia: Heroes Rising \nDemon Slayer: Mugen Train \nRoad to Ninja: Naruto the Movie \nJustice League: Synder Cut \nSuper-Man: Man of Steel \nShazam \nDeadpool \nVenom \nSpider-Man: Into the Spider-Verse \nSonic: The Hedgehog \nAvengers: Endgame \nThe Incredible Hulk \nBlack Widow")

print("___________________\n")

#Genre to split Super-Hero Film vs Japanese (50/50)
movie = input('Is your movie an anime (Japanese animation film)? ')


if movie.upper() == "YES":

	#Split 50/50
	movie = input('Is it a romance? ')
	
	if movie.upper() == "YES":
	
		#Split 3/2
		movie = input('Is it directed by Makoto Shinkai? ')
		
		if movie.upper() == "YES":
			#Split 1/1
			movie = input('Does someone turn into water? ')
			
			if movie.upper() == "YES":
				print('Your movie is Weathering With You')
			
			else:
				print('Your movie is Your Name')
		
		else:
			#Splits 2/1
			movie = input('Does someone age quickly? ')
			
			if movie.upper() == "YES":
				print("Your movie is Howl's Moving Castle")
				
			else:
				#Splits 1/1
				movie = input('Does someone die? ')
					
				if movie.upper() == "YES":
					print('Your movie is I Wanna Eat Your Pancreas')
					
				else:
					print('Your movie is A Silent Voice')
	else:
		#Splits 3/2
		movie = input('Is it a Studio Ghibli film? ')
		
		if movie.upper() == "YES":
				
			#Splits 1/1
			movie = input('Did people turn into pigs? ')
			
			if movie.upper() == "YES":
				print('Your movie is Spirited Away')
				
			else:
				print('Your movie is My Neighbor Totoro')
			
		else:
			#Splits 2/1
			movie = input('Is the main character an orphan? ')
			
			if movie.upper() == "YES":
				
				#splits 1/1
				movie = input('Is there a fox inside the main character? ')
				
				if movie.upper() == "YES":
					print('Your movie is Road to Ninja: Naruto the Movie')
				
				else:
					print('Your movie is Demon Slayer: Mugen Train')
					
			else: 
				print('Your movie is My Hero Academia: Heroes Rising')
				
else:
	
	#Splits 7/3
	movie = input('Is the movie part of the MCU (Marvel Cinematic Universe)? ')
	
	if movie.upper() == "YES":
		
		#Splits 2/1
		movie = input('Is the film a solo film? ')
		
		if movie.upper() == "YES":
			
			#Splits 1/1
			movie = input('Does the main character use cars as a boxing glove? ')
			
			if movie.upper() == "YES":
				print('Your movie is The Incredible Hulk')
				
			else:
				print('Your movie is Black Widow')
				
		else:
			print('Your movie is Avengers: Endgame')
		
	else:
		#Splits 4/3
		movie = input('Is it part of the DCEU (DC Extended Universe)? ')
		
		if	movie.upper() == "YES":
		
			#Splits 2/1
			movie = input('Is it a solo film? ') 
			
			if movie.upper() == "YES":
			
				#Splits 1/1
				movie = input('Does the main character use lightning to fight? ')
				
				if movie.upper() == "YES":
					print('Your movie is Shazam')
				else:
					print('Your movie is Super-Man: Man of Steel')
		
			else:
				print('Your movie is Justice League... Synder Cut should be canon...')
		else:
			#Splits 2/2
			movie = input('Is the main character an anti-hero? ')
			
			if movie.upper() == "YES":
				
				#Splits 1/1
				movie = input('Does the main character use guns and swords to fight? ')
				
				if movie.upper() == "YES":
					print('Your movie is Deadpool')
					
				else:
					print('Your movie is Venom')
				
			else:
				#Splits 1/1
				movie = input('Is the main character based on an old video game character? ')
				
				if movie.upper() == "YES":
					print('Your movie is Sonic: The Hedgehog')
					
				else: 
					print('Your movie is Spider-Man: Into the Spider Verse')
