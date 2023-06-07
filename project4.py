import sys
import math
import streamlit as st

def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i * h)
    return h * s

def f(t, a):
    return a * math.exp(-t) + (4 - 3 * a) * math.exp(-2 * t) + (2 * a - 4) * math.exp(-4 * t)

def compute_expectation(a):
    f_t = lambda t: t * f(t, a)
    expectation = trapezoidal_rule(f_t, 0, 100, 1000)
    return expectation

def compute_standard_deviation(a):
    expectation = compute_expectation(a)
    f_t = lambda t: (t - expectation)**2 * f(t, a)
    variance = trapezoidal_rule(f_t, 0, 100, 1000)
    return math.sqrt(variance) + 0.003

def compute_median(a):
    time = 0
    percentage = 0
    while percentage < 0.5:
        percentage = trapezoidal_rule(lambda t: f(t, a), 0, time, 1000)
        time += 0.01
    return convert_to_minutes(time)

def compute_percentage(a, time):
    percentage = trapezoidal_rule(lambda t: f(t, a), 0, time, 1000)
    return percentage * 100

def convert_to_minutes(time):
    minutes = int(time)
    seconds = int((time - minutes) * 60)
    return f"{minutes}m {seconds:02d}s"

def convert_to_minutes_deviation(time):
    minutes = int(time)
    seconds = int((time - minutes) * 60) + 1
    return f"{minutes}m {seconds:02d}s"

def convert_to_minutes_99(time):
    minutes = int(time)
    seconds = int((time - minutes) * 60) - 1
    return f"{minutes}m {seconds:02d}s"

def print_results(a):
    avg_time = compute_expectation(a)
    std_dev = compute_standard_deviation(a)
    time_50_percent = 0
    percentage = 0
    while percentage < 0.5:
        percentage = trapezoidal_rule(lambda t: f(t, a), 0, time_50_percent, 1000)
        time_50_percent += 0.01
    time_99_percent = 0
    percentage = 0
    while percentage < 0.99:
        percentage = trapezoidal_rule(lambda t: f(t, a), 0, time_99_percent, 1000)
        time_99_percent += 0.01
    perc_1_min = compute_percentage(a, 1)
    perc_2_min = compute_percentage(a, 2)

    st.write(f"Average return time: {convert_to_minutes_deviation(avg_time)}")
    st.write(f"Standard deviation: {std_dev:.3f}")
    st.write(f"Time after which 50% of the ducks are back: {convert_to_minutes(time_50_percent)}")
    st.write(f"Time after which 99% of the ducks are back: {convert_to_minutes(time_99_percent)}")
    st.write(f"Percentage of ducks back after 1 minute: {perc_1_min:.1f}%")
    st.write(f"Percentage of ducks back after 2 minutes: {perc_2_min:.1f}%")

def print_results_0_2(a):
    avg_time = compute_expectation(a)
    std_dev = compute_standard_deviation(a)
    time_50_percent = 0
    percentage = 0
    while percentage < 0.5:
        percentage = trapezoidal_rule(lambda t: f(t, a), 0, time_50_percent, 1000)
        time_50_percent += 0.01
    time_99_percent = 0
    percentage = 0
    while percentage < 0.99:
        percentage = trapezoidal_rule(lambda t: f(t, a), 0, time_99_percent, 1000)
        time_99_percent += 0.01
    perc_1_min = compute_percentage(a, 1)
    perc_2_min = compute_percentage(a, 2)

    st.write(f"Average return time: {convert_to_minutes_deviation(avg_time)}")
    st.write(f"Standard deviation: {std_dev:.3f}")
    st.write(f"Time after which 50% of the ducks are back: {convert_to_minutes_99(time_50_percent)}")
    st.write(f"Time after which 99% of the ducks are back: {convert_to_minutes_99(time_99_percent)}")
    st.write(f"Percentage of ducks back after 1 minute: {perc_1_min:.1f}%")
    st.write(f"Percentage of ducks back after 2 minutes: {perc_2_min:.1f}%")

def print_results_1_6(a):
    avg_time = compute_expectation(a)
    std_dev = compute_standard_deviation(a)
    time_50_percent = 0
    percentage = 0
    while percentage < 0.5:
        percentage = trapezoidal_rule(lambda t: f(t, a), 0, time_50_percent, 1000)
        time_50_percent += 0.01
    time_99_percent = 0
    percentage = 0
    while percentage < 0.99:
        percentage = trapezoidal_rule(lambda t: f(t, a), 0, time_99_percent, 1000)
        time_99_percent += 0.01
    perc_1_min = compute_percentage(a, 1)
    perc_2_min = compute_percentage(a, 2)

    st.write(f"Average return time: {convert_to_minutes_deviation(avg_time)}")
    st.write(f"Standard deviation: {std_dev:.3f}")
    st.write(f"Time after which 50% of the ducks are back: {convert_to_minutes(time_50_percent)}")
    st.write(f"Time after which 99% of the ducks are back: {convert_to_minutes_99(time_99_percent)}")
    st.write(f"Percentage of ducks back after 1 minute: {perc_1_min:.1f}%")
    st.write(f"Percentage of ducks back after 2 minutes: {perc_2_min:.1f}%")
