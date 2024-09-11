#!/usr/bin/python3
import time
print('\nWelcome to the Personality Quiz!')
name = input("\nFirst, what's your name? ")
print(f'\nNice to meet you, {name}!')
time.sleep(1)
color = input(f"\n{name}, what's your favorite color? ")
time.sleep(1)
print(f'\n{color} is such a nice color')
time.sleep(1)
animal = input(f"\nAnd what's your favorite animal, {name}? ").strip().lower()
time.sleep(2)
if animal == 'cat':
	print('\nAh! The mysterious and independent cat!')
elif animal == 'dog':
	print('\nThe loyal and playful dog!')
else:
	print(f"\nWow, {animal.lower()}! That's a great and unexpected choice!")
time.sleep(1)
hobby = input(f'\nWhat do you like to do in your free time, {name}? ')
time.sleep(1)
print(f'\nLet me think for a second here, {name}...')
time.sleep(2)
print(f'\n{name.capitalize()}, you must be someone who loves {color.lower()} things, '
	f'hangs out with {animal}s,\n'
	f'and enjoys {hobby.lower()} in your free time!')
time.sleep(1)
print(f'\nThanks for playing, i hope you have learned a lot about yourself {name}, '
      	f'\nhave a wonderful day!')
