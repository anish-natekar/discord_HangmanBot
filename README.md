# discord_HangmanBot
Hangman Game
---------------


Triple-A: Anish Natekar


Project files:
1. Triple_A_main.py - Contains the main function and has some initial user inputs to select categories (main file)
2. Triple_A_func - Folder containing all other files and scripts required for the game to run
1. Triple_A_bollywoodtext.txt - Contains about 300 bollywood movie names, date of release, genre, actor names and director name in Hash separated format.
2. Triple_A_IMDBtext.txt - Contains about 1000 movies rated 7.4 or more on IMDB along with date of release and genre of movie in Hash separated format.
3. Triple_A_MALtext.txt - Contains about 400 Anime rated 8.0 or more on MyAnimeList.net and which come under the top 400 most popular anime on MyAnimeList.net along with the date of release and genre in Hash separated format.
4. Triple_A_display_script.py - this script has a function that will display the ASCII hangman character according to how many tries are left.
5. Triple_A_file_script.py - this script has functions to read, write and append certain files which are required for the game.
6. Triple_A_backend_script.py - this script has the main game loop and function to get a random movie name of a specific category. This is the backend part of the game which the user can’t see so that is why the script is also named backend_script.
7. Triple_A_hint_script.py - this script contains a function that will define the order of hints for each category and return the specific hint index for a specific input.
To asks for hints in the game user has to type out “hint” instead of an alphabet 


Sample inputs: 
First when you run Triple_A_main.py it will present to you a menu.
You have to select either 1, 2 or 3 according to the respective option.


Now enter your name it can be any string we would recommend not having # in you name
It will not cause any exceptions but it will cause a logical error.


Instead of mentioning sample inputs i will explain the game
So the game start by selecting some category from which data will be taken
There are 3 options bollywood movie, IMDB movie or Anime to choose from to pick any one enter either 1, 2 or 3 respectively.


Now the game has begun
The user has to enter only one ALPHABET from the keyboard
The aim is to guess an alphabet that may lie in the name of the movie/anime title.
User can also gues the whole title name in one go by writing the whole title with correct spelling and format.


User can also ask for hints by typing the word ‘hint’ instead of any alphabet and it will display a hint before the hangman character.
There are limited hints 4 for bollywood and 2 for IMDB and anime
Using hint again and again will just print the ending hint.


Here after you guess a word or not guess it you can choose to play another round or stop by choosing y or n respectively.


If you choose n your score and datetime will be printed and recorded in logs.txt
