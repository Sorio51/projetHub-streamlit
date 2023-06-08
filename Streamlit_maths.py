import streamlit as st
import subprocess
from pathlib import Path
import sys
import subprocess
import project1
import project2
import project3
import project4
import project5
import project6
import project7
import project8
import project9
import subprocess

def main():
    st.sidebar.title("Math Projects Tek2")
    project_selection = st.sidebar.radio("Select Project", ("201yams", "202unsold","203hotline","204ducks","205IQ","206neutrinos",'207demography',"208dowels","209poll"))

    if project_selection == "201yams":
        project1_page()
    elif project_selection == "202unsold":
        project2_page()
    elif project_selection == "203hotline":
        project3_page()
    elif project_selection == "204ducks":
        project4_page()
    elif project_selection == "205IQ":
        project5_page()
    elif project_selection == "206neutrinos":
        project6_page()
    elif project_selection == "207demography":
        project7_page()
    elif project_selection == "208dowels":
        project8_page()
    elif project_selection == "209poll":
        project9_page()

def parse_prog(d1, d2, d3, d4, d5, c):
    args = [str(d1), str(d2), str(d3), str(d4), str(d5), c]
    subprocess.run(["python3", "project1.py"] + args, check=True)

def project1_page():
    st.title("201yams")

    st.markdown("""
    \n**DESCRIPTION**\n
    d1  value of the first die (0 if not thrown)
    d2  value of the second die (0 if not thrown)
    d3  value of the third die (0 if not thrown)
    d4  value of the fourth die (0 if not thrown)
    d5  value of the fifth die (0 if not thrown)
    c   expected combination
    """)

    d1 = st.number_input("D1", value=1)
    d2 = st.number_input("D2", value=2)
    d3 = st.number_input("D3", value=3)
    d4 = st.number_input("D4", value=4)
    d5 = st.number_input("D5", value=5)
    c = st.text_input("Expected combination", value="four_4")

    if st.button("Compute"):
        project1.parse_prog(int(d1), int(d2), int(d3), int(d4), int(d5), c)

def project2_page():
    st.title("202Unsold")

    st.markdown("""
    \n**DESCRIPTION**\n
    DESCRIPTION
    a constant computed from past results
    b constant computed from past results
    """)

    a = st.number_input("Parameter A", value=60)
    b = st.number_input("Parameter B", value=70)

    if st.button("Compute"):
        project2.MainUnsold(int(a), int(b))

def project3_page():
    st.title("203 Hotline")

    st.markdown("""
    \n**DESCRIPTION**\n
    n       n value for the computation of C(n, k)
    k       k value for the computation of C(n, k)
    d       average duration of calls (in seconds)
    """)

    appel = st.number_input("Number of calls:", value=180, min_value=1)
    people = 3500
    hour = 8

    if st.button("Compute Binomial Distribution"):
        project3.binomial_distribution(appel, people, hour)

    if st.button("Compute Poisson Distribution"):
        project3.poisson_distribution(appel, people, hour)

def project4_page():
    st.title("204ducks")

    st.markdown("""
    \n**DESCRIPTION**\n
    a constant (between 0 and 2.5)
    """)

    a = st.number_input("Parameter A", value=1.60)

    if st.button("Compute"):
        project4.print_results(a)

def project5_page():
    st.title("205IQ")

    st.markdown("""
    \n**DESCRIPTION**\n
    u      mean
    s      standard deviation
    IQ1    minimum IQ
    IQ2    maximum IQ
    """)

    if st.button("Compute Percentage Below"):
        project5.main()

def project6_page():
    st.title("206neutrinos")

    st.markdown("""
    \n**DESCRIPTION**\n
    n       number of values
    a       arithmetic mean
    h       harmonic mean
    sd      standard deviation
    """)

    tab = [12000, 297514, 297912, 4363]

    st.write(f"   Number of values:   {tab[0]}")
    st.write(f"   Standard deviation: {tab[3]:.2f}")
    st.write(f"   Arithmetic mean:    {tab[1]:.2f}")
    st.write(f"   Root mean square:   {tab[3]:.2f}")
    st.write(f"   Harmonic mean:      {tab[2]:.2f}\n")

    value = st.number_input("Value", value = 299042)
    result = project6.calculate_stats(tab, value)
    if result is not None:
        st.error("Invalid input. Please enter a numeric value.")

def project7_page():
    st.title("207demography")

    st.markdown("""
    \n**DESCRIPTION**\n
    code    country code
    """)

    user_input = st.text_input("Enter country code(s) separated by space")
    country_codes = user_input.split()

    if st.button("Compute Percentage Below"):
        project7.main(country_codes)

def project8_page():
    st.title("208dowels")

    st.markdown("""
    \n**DESCRIPTION**\n
    Oi  size of the observed class
    """)

    values = [0 for _ in range(9)]

    if st.button("Compute Percentage Below"):
        try:
            st.sidebar.title("Input Values")

            values = [st.number_input(f"Value {i+1}", min_value=0, max_value=100, value=values[i]) for i in range(9)]
            if sum(values) != 100 or sum(1 for number in values if number < 0) > 0:
                st.error("Invalid input! The sum of values should be 100 and all values should be non-negative.")
                return

            main(values)

        except:
            st.error("An error occurred during the calculation.")

def project9_page():
    st.title("209poll")

    st.markdown("""
    \n**DESCRIPTION**\n
    pSize   size of the population
    sSize   size of the sample (supposed to be representative)
    p       percentage of voting intentions for a specific candidate
    """)

    pSize = st.number_input("Population size", value=10000)
    sSize = st.number_input("Sample size", value=500)
    p = st.number_input("Voting intentions (%)", value=42.24)

    if st.button("Compute"):
        project9.compute_confidence_intervals(pSize, sSize, p)

if __name__ == "__main__":
    main()
