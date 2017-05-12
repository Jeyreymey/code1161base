# -*- coding: UTF-8 -*-
"""Refactoring.

This excercise is very similar to week 2, exercise 2. It contains a complete
and working example, but it's very poorly written.

Your job is to go through it and make it as good as you can.

That means making it self-documenting wherever possible, adding comments where
it isn't. Take repeated code and make it into a function. Also use functions
to encapsulate concepts. If something is done many times, maybe a map or a loop
is called for. Etc.

The resulting file should feel as close to english as possible.
It must also pass the linter.

This is the first file that will be run against the pydocstyle checker. If
you've run the week5_system_prep.sh file you should be getting blue linter dots
that show you where lintere errors are. If they aren't working, you should be
getting the errors in the test output.

Some functions will have directions as external comments, once you think you
are on top of it, take these comments out. Others won't have comments and
you'll need to figure out for yourself what to do.
"""

from __future__ import division
from __future__ import print_function


# This is a terrible function. The rest of the functions in this file do a
# much better job of what it's trying to do. Once you've has a little look,
# move on, and eventually delete this function. (And this comment!)
def do_bunch_of_bad_things():
    """Get rid of this line.

    The line is completely useless
    """
    # print("Getting ready to start in 9")
    # print("Getting ready to start in 8")
    # print("Getting ready to start in 7")
    # print("Getting ready to start in 6")
    # print("Getting ready to start in 5")
    # print("Getting ready to start in 4")
    # print("Getting ready to start in 3")
    # print("Getting ready to start in 2")
    # print("Getting ready to start in 1")
    # print("Let's go!")
    #
    # print("area = " + str((triangle["base"] * triangle["height"])/2))
    # print("side lengths are:")
    # print("base: {}".format(triangle["base"]))
    # print("height: {}".format(triangle["height"]))
    # print("hypotenuse: {}".format(triangle["hypotenuse"]))
    #
    # another_hyp = 5**2 + 6**2
    # print(another_hyp)
    #
    # yet_another_hyp = 40**2 + 30**2
    # print(yet_another_hyp)


# return a list of countdown messages, much like in the bad function above.
# It should say something different in the last message.
def countdown(message, start, stop, completion_message):
    """Return a list of countdown messages, much like in the bad function above.

    It should say something different in the last message.
    """
    count_down = start
    if count_down > stop:
        print(message, count_down)
        while count_down > stop:
            count_down = count_down - 1
            print(message, count_down)
    elif countdown < stop:
        print(message, count_down)
        while count_down < stop:
            count_down = count_down + 1
            print(message, count_down)
    if count_down == stop:
        print(completion_message)


# TRIANGLES

# This should be a series of functions that are ultimatly used by
# triangle_master
# It should eventually return a dictionary of triangle facts. It should
# optionally print information as a nicely formatted string. Make printing
# turned off by default but turned on with an optional argument.
# The stub functions are made for you, and each one is tested, so this should
# hand hold quite nicely.
def calculate_hypotenuse(base, height):
    """Return the hypotenuse of a triangle.

    use Pythagorus' theorem to help you
    """
    a = base
    b = height
    c = a**2 + b**2
    d = round(c**0.5, 2)
    print(d)
    return d


def calculate_area(base, height):
    """Return a line that calculates the area of a triangle.

    Use the calculate_area function to help you.
    """
    a = base * height
    b = a/2
    print(b)
    return b


def calculate_perimeter(base, height):
    """Return a line that calculates the perimeter of a triangle.

    Use the calculate_perimeter function to help you.
    """
    if True:
        a = base + height
        print(a)
    triangle = base**2 + height**2
    if triangle == int():
        triangle_hyp = int(triangle**0.5, 2)
        print(triangle_hyp + a)
        return(triangle_hyp + a)


def calculate_aspect(base, height):
    """Return a line that calculates the area of a triangle.

    Use the calculate_area function to help you.
    """


# Make sure you reuse the functions you've already got
# Don't reinvent the wheel
def get_triangle_facts(base, height, units="mm"):
    """Return a line that calculates the area of a triangle.

    Use the calculate_area function to help you.
    """
    return {"area": None,
            "perimeter": None,
            "height": None,
            "base": None,
            "hypotenuse": None,
            "aspect": None,
            "units": None}


# this should return a multi line string that looks a bit like this:
#
# 15
# |
# |     |\
# |____>| \  17.0
#       |  \
#       |   \
#       ------
#       8
# This triangle is 60.0mm²
# It has a perimeter of 40.0mm
# This is a tall triangle.
#
# but with the values and shape that relate to the specific
# triangle we care about.
def tell_me_about_this_right_triangle(facts_dictionary):
    """Return some facts about the triangle below.

    Describe how tall and wide it is while also elaborating on other facts.
    """
    tall = """
            {height}
            |
            |     |\\
            |____>| \\  {hypotenuse}
                  |  \\
                  |   \\
                  ------
                  {base}"""
    wide = """
            {hypotenuse}
             ↓         ∕ |
                   ∕     | <-{height}
               ∕         |
            ∕------------|
              {base}"""
    equal = """
            {height}
            |
            |     |⋱
            |____>|  ⋱ <-{hypotenuse}
                  |____⋱
                  {base}"""

    pattern = ("This triangle is {area}{units}²\n"
               "It has a perimeter of {perimeter}{units}\n"
               "This is a {aspect} triangle.\n")

    facts = pattern.format(**facts_dictionary)


def triangle_master(base,
                    height,
                    return_diagram=False,
                    return_dictionary=False):
    """Return a working triangle master.

    It should do everything that you have already done when describing
    the triangle.
    """
    if return_diagram and return_dictionary:
        return None
    elif return_diagram:
        return None
    elif return_dictionary:
        return None
    else:
        print("You're an odd one, you don't want anything!")


def wordy_pyramid():
    """Return a word pyramid.

    This pyramid should have a max of 21 and a min of 3 letter words.
    These words should go up by 2 untill the max and down by 2 untill the min.
    """
    import requests
    baseURL = "http://www.setgetgo.com/randomword/get.php?len="
    pyramid_list = []
    for i in range(3, 21, 2):
        url = baseURL + str(i)
        r = requests.get(url)
        message = r.text
        pyramid_list.append(message)
    for i in range(20, 3, -2):
        url = baseURL + str(i)
        r = requests.get(url)
        message = r.text
        pyramid_list.append(message)
    return pyramid_list


def get_a_word_of_length_n(length):
    """Generate a word with a length of n.

    make use of the pyramid script above.
    """
    import requests
    baseURL = "http://www.setgetgo.com/randomword/get.php?len="
    word_gen = []
    for i in range(input()):
        url = baseURL + str(i)
        r = requests.get(url)
        message = r.text
        word_gen.append(message)
    print(word_gen)
    return word_gen


def list_of_words_with_lengths(list_of_lengths):
    """Create a list of words with a generaive number of letters.

    from the last line of code extend it to form a list of these words.
    """


if __name__ == "__main__":
    do_bunch_of_bad_things()
    print(countdown("Countdown starts in", 9, 0, "yey"))
