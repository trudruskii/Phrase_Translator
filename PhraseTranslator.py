# SpencerP4.py
# Programmer: Andrew Spencer
# Email: aspencer22@cnm.edu
# Date: 09/05/2024
# Purpose: Translate common phrases from English to Spanish using a dictionary and user input.
# Python Version: 3.12.5

import time

# Create a dictionary with common phrases in langauge as the keys and the translations in another language as the values
lang_dict = {
    'How are you?': 'Como estas',
    'See you later': 'Hasta luego',
    'Please': 'Por favor',
    'Thank you very much!': 'Muchas gracias',
    'Where is the bathroom?': 'Donde esta el bano',
    'How much does this cost?': 'Cuanto cuesta esto',
}

# Convert the dictionary to a list for better output display
display_lang_dict = ' | '.join(list(lang_dict))

# Greeting
print('Welcome to the language translator!')
print('Please choose one of the following phrases to have it translated to Spanish:')

# Display the list of phrases to the user
print(display_lang_dict)

# Ask the user to enter a phrase to have translated
translate_user_value = input('\nPlease pick a phrase above and enter it to have it translated: ').strip()

# Fix the case of the user's input for case sensitivity errors
fix_case = translate_user_value.capitalize()

# Display the translation to the user
translated_value = lang_dict.get(fix_case, 'Phrase not found')
print(translated_value)

time.sleep(3.2)
print('\nThank you for using the language translator!')
print('Feel free to follow my progress by visiting my Github at:')
print('https://github.com/trudruskii')