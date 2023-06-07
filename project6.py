import math
import streamlit as st

def calculate_stats(tab, value):
    try:
        float_value = int(value)
        if float_value < 0:
            return 84
        stock = (tab[3] * tab[3] + tab[1] * tab[1]) * tab[0]
        calc = (tab[3] * tab[3] + tab[1] * tab[1]) * tab[0]
        a_n = tab[1] * tab[0]
        tab[0] += 1
        tab[1] = (a_n + float_value) / tab[0]
        tab[3] = math.sqrt(((calc + pow(float_value, 2)) / tab[0]) - pow(tab[1], 2))
        tab[2] = tab[0] / ((1 / float_value) + ((tab[0] - 1) / tab[2]))
        root = math.sqrt((stock + pow(float_value, 2)) / tab[0])
        st.write(f"   Number of values:   {tab[0]}")
        st.write(f"   Standard deviation: {tab[3]:.2f}")
        st.write(f"   Arithmetic mean:    {tab[1]:.2f}")
        st.write(f"   Root mean square:   {root:.2f}")
        st.write(f"   Harmonic mean:      {tab[2]:.2f}\n")
    except ValueError:
        return 84
