import streamlit as st
import math
import sys


def open_file():
    with open("log/help.txt", "r+") as file:
        for i in range(11):
            st.write(file.readline())


def pdf(x, mu, sigma):
    return math.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi))


def cdf(x, mu, sigma):
    if sigma == 0:
        sys.exit(84)
    else:
        return (1 + math.erf((x - mu) / (sigma * math.sqrt(2)))) / 2


def percentage_below(x, mu, sigma):
    return cdf(x, mu, sigma) * 100


def percentage_between(x1, x2, mu, sigma):
    return (cdf(x2, mu, sigma) - cdf(x1, mu, sigma)) * 100


def normal_pdf(x, mean, std_dev):
    if std_dev == 0:
        sys.exit(84)
    return (1 / (std_dev * math.sqrt(2 * math.pi))) * math.exp(-((x - mean) ** 2) / (2 * std_dev ** 2))


def iq_calculator(mean, std_dev, iq=None, iq1=None, iq2=None):
    if iq is None and iq1 is None and iq2 is None:
        iq_list = []
        for iq_value in range(0, 201):
            pdf_value = normal_pdf(iq_value, mean, std_dev)
            iq_list.append((iq_value, pdf_value))
        return iq_list

    elif iq is not None:
        if iq < 0 or iq > 200:
            sys.exit(84)
        percentage = percentage_below(iq, mean, std_dev)
        return f"{percentage:.1f}% of people have an IQ inferior to {iq}"

    elif iq1 is not None and iq2 is not None:
        if iq1 < 0 or iq1 > 200 or iq2 < 0 or iq2 > 200 or iq2 < iq1:
            sys.exit(84)
        percentage = percentage_between(iq1, iq2, mean, std_dev)
        return f"{percentage:.1f}% of people have an IQ between {iq1} and {iq2}"


def main():
    st.title("IQ Calculator")

    st.markdown("""
        **DESCRIPTION**

        This program calculates IQ probabilities and percentages using the normal distribution.

        Please enter the required parameters.
        """)

    mean = st.number_input("Mean IQ", value=100.0)
    std_dev = st.number_input("Standard Deviation", value=15.0)

    option = st.selectbox("Select Option", ("Calculate All PDFs", "Percentage Below IQ", "Percentage Between IQs"))

    if option == "Calculate All PDFs":
        iq_list = []
        for iq_value in range(0, 201):
            pdf_value = math.exp(-(iq_value - mean) ** 2 / (2 * std_dev ** 2)) / (std_dev * math.sqrt(2 * math.pi))
            iq_list.append((iq_value, pdf_value))

        st.write("IQ   PDF")
        for iq, pdf_value in iq_list:
            st.write(f"{iq}   {pdf_value:.5f}")

    elif option == "Percentage Below IQ":
        iq = st.number_input("IQ", min_value=0, max_value=200)
        if iq < 0 or iq > 200:
            st.error("Invalid IQ value. Please enter a value between 0 and 200.")
        else:
            cdf_value = (1 + math.erf((iq - mean) / (std_dev * math.sqrt(2)))) / 2
            percentage = cdf_value * 100
            st.write(f"{percentage:.1f}% of people have an IQ inferior to {iq}")

    elif option == "Percentage Between IQs":
        iq1 = st.number_input("IQ 1", min_value=0, max_value=200)
        iq2 = st.number_input("IQ 2", min_value=0, max_value=200)
        if iq1 < 0 or iq1 > 200 or iq2 < 0 or iq2 > 200 or iq2 < iq1:
            st.error("Invalid IQ values. Please enter valid values.")
        else:
            cdf_value1 = (1 + math.erf((iq1 - mean) / (std_dev * math.sqrt(2)))) / 2
            cdf_value2 = (1 + math.erf((iq2 - mean) / (std_dev * math.sqrt(2)))) / 2
            percentage = (cdf_value2 - cdf_value1) * 100
            st.write(f"{percentage:.1f}% of people have an IQ between {iq1} and {iq2}")

