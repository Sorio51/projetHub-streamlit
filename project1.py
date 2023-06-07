#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## 201yams
## File description:
## Yams Probability
##

import sys
import math
import streamlit as st

def open_file():
    file = open("log/help.txt", "r+")

    for i in range(11):
        print(file.readline(), end = "")
    file.close()

def try_int(number):
    try:
        int(number)
    except ValueError:
        sys.exit(84)
    if (int(number) < 1 or int(number) > 6):
        sys.exit(84)

def count_zero():
    cp = 0
    for i in range(len(sys.argv) -  2):
        if (sys.argv[i + 1] == 0):
            cp += 1
    return cp

def fact(nb):
    if nb == 1:
        return 1
    else:
        return nb * fact(nb-1)

def calc_binomial(a, b):
    result = (math.factorial(a) / (math.factorial(b) * math.factorial(a - b))) * pow((1 / 6), b) * pow((5 / 6), (a - b))
    return result

def get_spawn(nb):
    app = 0
    for i in range(len(sys.argv) - 2):
        if (sys.argv[i + 1] == nb):
            app += 1
    return app

def print_fast(number, nb, x):
    if (x == 2):
        st.write("Chances to get a", number, "pair: %.2f%%" % nb)
    if (x == 3):
        st.write("Chances to get a", number, "three-of-a-kind: %.2f%%" % nb)
    if (x == 4):
        st.write("Chances to get a", number, "four-of-a-kind: %.2f%%" % nb)
    if (x == 5):
        st.write("Chances to get a", number, "yams: %.2f%%" % nb)

def calc_number_easy(number, x):
    nb = 0
    app = get_spawn(number)

    if (x < app):
        nb = 0.1
    else:
        for i in range(x - app, 6 - app):
            nb += calc_binomial(5 - app, i)
    nb *= 100
    print_fast(number, nb, x)

def full(number1, number2):
    x = 1
    app1 = get_spawn(number1)
    app2 = get_spawn(number2)
    for n in range(5 - app1 - app2, 6 - app1 - app2):
        x *= calc_binomial(5 - app1 - app2, n)
    if x > 0.1:
        x = 0.1
    dec = math.ceil((x * 1000) * 100) / 100
    st.write("Chances to get a", number1, "full of", number2, end="")
    st.write(": %.2f%%" % dec)

def straight(number):
    tab = [sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]]

    result = math.factorial(int(number) - int(len(tab))) / pow(6, int(number) - int(len(tab)))
    dec = math.ceil((result * 100) * 100) / 100
    st.write("Chances to get a", number, "straight: %.2f%%" % dec)

def check_tab(parts):
    if (len(parts) > 2):
        sys.exit(84)

def match_keyword(word, number1, parts):
    if (word == "pair"):
        check_tab(parts)
        calc_number_easy(number1, 2)
        sys.exit(0)
    if (word == "three"):
        check_tab(parts)
        calc_number_easy(number1, 3)
        sys.exit(0)
    if (word == "four"):
        check_tab(parts)
        calc_number_easy(number1, 4)
        sys.exit(0)
    if (word == "full"):
        if (len(parts) < 3):
            sys.exit(84)
        number2 = parts[2]
        if (len(parts) > 3):
            sys.exit(84)
        try_int(number2)
        if (number1 == number2):
            sys.exit(84)
        full(number1, number2)
        sys.exit(0)
    if (word == "straight"):
        check_tab(parts)
        if (int(number1) < 5):
            sys.exit(84)
        straight(number1)
        sys.exit(0)
    if (word == "yams"):
        check_tab(parts)
        calc_number_easy(number1, 5)
        sys.exit(0)
    sys.exit(84)

def parse_prog(d1, d2, d3, d4, d5, c):
    parts = c.split('_')
    word = parts[0]
    if len(parts) < 2:
        st.exit(84)
    number1 = parts[1]

    try_int(number1)
    match_keyword(word, number1, parts)

if __name__ == "__main__":
    if (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        open_file()
        st.exit(0)
    if (len(sys.argv) != 7):
        st.exit(84)
    try:
        for i in range(len(sys.argv) -  2):
            int(sys.argv[i + 1])
    except ValueError:
        st.exit(84)
    for i in range(len(sys.argv) -  2):
        if (int(sys.argv[i + 1]) < 0 or int(sys.argv[i + 1]) > 6):
            st.exit(84)
    parse_prog()