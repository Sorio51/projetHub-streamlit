#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## B-MAT-400-MPL-4-1-209poll-sacha.dessaint
## File description:
## 209poll
##

import math
import sys
import streamlit as st

def open_file():
    with open("log/help.txt", "r+") as file:
        for i in range(11):
            st.write(file.readline(), end="")

def compute_confidence_intervals(pSize, sSize, p):
    sample_proportion = p / 100
    variance = (sample_proportion * (1 - sample_proportion)) / sSize
    variance *= (pSize - sSize) / (pSize - 1)
    ci_95_amplitude = 1.96 * math.sqrt(variance)
    ci_99_amplitude = 2.58 * math.sqrt(variance)
    ci_95_lower_bound = sample_proportion - ci_95_amplitude
    ci_95_upper_bound = sample_proportion + ci_95_amplitude
    ci_99_lower_bound = sample_proportion - ci_99_amplitude
    ci_99_upper_bound = sample_proportion + ci_99_amplitude

    st.write(f"Population size:\t {pSize}")
    st.write(f"Sample size: \t\t {sSize}")
    st.write(f"Voting intentions:\t {p:.2f}%")
    st.write(f"Variance:\t\t {variance:.6f}")
    st.write(f"95% confidence interval: [{ci_95_lower_bound * 100:.2f}%; {ci_95_upper_bound * 100:.2f}%]")
    st.write(f"99% confidence interval: [{ci_99_lower_bound * 100:.2f}%; {ci_99_upper_bound * 100:.2f}%]")

if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        open_file()
        sys.exit(0)
    if len(sys.argv) != 4:
        sys.exit(84)
    try:
        pSize = int(sys.argv[1])
        if pSize <= 0:
            sys.exit(84)
        sSize = int(sys.argv[2])
        if sSize <= 0:
            sys.exit(84)
        p = float(sys.argv[3])
        if p < 0 or p > 100:
            sys.exit(84)
        compute_confidence_intervals(pSize, sSize, p)
    except ValueError as e:
        st.write(f"Error: {str(e)}")
        sys.exit(84)