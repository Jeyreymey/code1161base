# -*- coding: UTF-8 -*-
"""
I'm in UR exam.
This is the same as the weekly exercises, fill in the functions,
and test them to see if they work.
You've got an hour.
"""
from __future__ import division
from __future__ import print_function
import time


def greet(name="Towering Timmy"):
    """Return a greeting.

    return a string of "Hello" and the name argument.
    E.g. if given as "Towering Timmy" it should return "Hello Towering Timmy"
    """
    print ("Hello " + name)
    return "Hello " + name


def three_counter(input_list=[1, 4, 3, 5, 7, 1, 3, 2, 3, 3, 5, 3, 7]):
    """Count the number of 3s in the input_list.

    Return an integer.
    TIP: the test will use a different input_list, so don't just return 5
    """
    counter = input_list.count(3)
    return int(counter)


def fizz_buzz():
    """Do the fizzBuzz.

        This is the most famous basic programming test of all time!
       "Write a program that prints the numbers from 1 to 100. But for
        multiples of three print "Fizz" instead of the number and for
        the multiples of five print "Buzz". For numbers which are
        multiples of both three and five print "FizzBuzz"."
            from https://blog.codinghorror.com/why-cant-programmers-program/
    Return a list that has an integer if the number isn't special, and a string
    if it is. E.g. [1, 2, "Fizz", 4, "Buzz", 6, 7, ...]
    """
    fizzBuzzList = []
    for i in range(1, 101):
        if i % 15 == 0:
            fizzBuzzList.append("FizzBuzz")
        elif i % 5 == 0:
            fizzBuzzList.append("Buzz")
        elif i % 3 == 0:
            fizzBuzzList.append("Fizz")
        else:
            fizzBuzzList.append(i)

    return (fizzBuzzList)


def put_behind_bars(input_string="very naughty boy"):
    """Interleave the input_string with pipes.

    Given any string, interleave it with pipes (| this character)
    e.g. "very naughty boy" should return "|v|e|r|y| |n|a|u|g|h|t|y| |b|o|y|"
    TIP: make sure that you have a pipe on both ends of the string.
    """
    name = input_string
    interleave = "|"
    behind_bars = "".join(i for j in zip(name, interleave)for i in j)
    return (behind_bars)


def pet_filter(letter="a"):
    """Return a list of animals with `letter` in their name."""
    pets = ["dog", "goat", "pig", "sheep", "cattle", "zebu", "cat", "chicken",
            "guinea pig", "donkey", "duck", "water buffalo",
            "western honey bee", "dromedary camel", "horse", "silkmoth",
            "pigeon", "goose", "yak", "bactrian camel", "llama", "alpaca",
            "guineafowl", "ferret", "muscovy duck", "barbary dove",
            "bali cattle", "gayal", "turkey", "goldfish", "rabbit", "koi",
            "canary", "society finch", "fancy mouse", "siamese fighting fish",
            "fancy rat and lab rat", "mink", "red fox", "hedgehog", "guppy"]
    new_list = []
    for pet_name in pets:
        for pet_name_index in range(len(pet_name)):
            if pet_name[pet_name_index] == letter:
                new_list.append(pet_name)
    return new_list


def best_letter_for_pets():
    """Return the letter that is present at least once in the most pet names.

    Reusing the pet_filter, find the letter that gives the longest list of pets
    TIP: return just a letter, not the list of animals.
    """
    import string
    the_alphabet = string.lowercase
    print(the_alphabet)
    list_of_names_with_letter = pet_filter(a_letter)
    for the_letter in the_alphabet
        list_name = pet_filter(the_letter)
        #now check the length of the list as see if its the biggest


def make_filler_text_dictionary():
    """Make a dictionary of random words filler text.

    There is a random word generator here: http://www.setgetgo.com/randomword/
    The only argument that the generator takes is the length of the word.
    Return a dictionary where the keys are numbers, and the values are lists of
    words. e.g. {3: ['cat','pop','cow'], ...}
    Use the API to get the 3 words.
    The dictionary should have the numbers between 3 and 7 inclusive.
    (i.e. 3, 4, 5, 6, 7 and 3 words for each)
    TIP: to add an argument to a URL, use: ?argName=argVal e.g. ?len=
    TIP: you'll need the requests library
    """
    import requests
    pass


def random_filler_text(number_of_words=200):
    """Make a paragraph of random filler text.

    Using the dictionary returned by make_filler_text_dictionary, make a
    paragraph of text using randomly picked words. Each word should be a random
    length, and a random one of the 3 words.
    Make the paragraph have number_of_words words in it.
    Return it as a string
    TIP: you'll need the random library
    Bonus: extra mark if you get the paragraph to start with a
           capital letter and end with a full stop.
    """
    import random
    pass


def fast_filler(number_of_words=200):
    """Reimplement random filler text.

    This time, the first time the code runs, save the dictionary to a file.
    On the second run,if the file already exists use it instead of going to
    the internet.
    Use the filename "dict_racey.words"
    TIP: you'll need the os library
    TIP: you'll probably want to use json dumps and loads to get the dictionary
    into and out of the file. Be careful when you read it back in, it'll
    convert integer keys to strings.
    """
    pass


if __name__ == '__main__':
    print(greet())
    print(three_counter())
    print(fizz_buzz())
    print(put_behind_bars())
    print(pet_filter())
    print(best_letter_for_pets())
    print(make_filler_text_dictionary())
    print(random_filler_text())
    print(fast_filler())
    for i in range(10):
        print(i, fast_filler())
