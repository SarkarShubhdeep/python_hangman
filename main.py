import os
import random
import word_art
import movies_list

print(word_art.hangman)

movie = random.choice(movies_list.all_movies).upper()


len_movie = len(movie)
result_list = ['_' for i in movie]

# print(result)

lives = 6
print(word_art.stages[lives])
result = " ".join(result_list)
print(result)

while '_' in result_list:
    guess = input("Guess a letter: ").upper()

    if guess not in movie:
        print(f"Letter '{guess}' is not present in chosen movie name.")
        lives -= 1
    else:
        for i in range(len_movie):
            if movie[i] == guess:
                result_list[i] = guess
    result = " ".join(result_list)
    print(word_art.stages[lives])
    if lives == 0:
        print("You loose.")
        print(f"Movie was {movie}")
        break
    print(f"Lives left - {lives}")
    print(result)
    print()


if '_' not in result_list:
    print('Congratulations! You win.')






