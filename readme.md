#Language Practice

A work-in-progress command-line app for practicing a new language through text-to-speech and written translation. Currently only supports Spanish to English translations. `spanish_english.json` contains a base dictionary of random vocabulary that can be modified.

###Required dependencies

* Python 2.x (Python 3 untested)
* Mac OSX Terminal (untested in Linux terminal)
* Mac `say` program with English-US voice Alex and Spanish voice Carlos installed (http://apple.stackexchange.com/questions/3454/say-in-different-language)

###Usage 

`python practice.py` - starts the program
`add` - add a word or phrase and its translation to your vocabulary list
`q` - quits the program

Pressing Enter randomly chooses a method to deliver the word or phrase. The program will either:

* Speak the word/phrase and the user has to translate
* Display the word/phrase in one language and the user has to translate

This allows for varied forms of exposure to words and phrases.

###To Do

* Normalize JSON structure:
    * Support for synonyms
    * Words with multiple meanings
* Abstract to allow any language (only supports Spanish-English right now)
* Bundle into downloadable app with Platypus, Electron or similar
