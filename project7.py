import sys
from math import sqrt
import streamlit as st

def feur(data):
    result = []
    for values in data.values():
        if len(result) < len(values):
            result.extend(values)
        else:
            for i in range(len(values)):
                result[i] += values[i]
    return result

def avg(dates, total):
    if len(dates) != len(total):
        sys.exit(84)
    return sum(total) / len(total) if len(total) > 0 else 0

def quoicoubeh(dates, total, elem):
    dateAvg = sum(dates) / len(dates) if len(dates) > 0 else 0
    dividend = 0
    divisor = 0
    for i in range(0, len(total)):
        dist = 0
        value = total[i]
        if elem == 1:
            dist = dates[i] - dateAvg
            dividend += (value - avg(dates, total)) * dist
        elif elem == 2:
            dist = value - avg(dates, total)
            dividend += (dates[i] - dateAvg) * dist
        divisor += pow(dist, 2)
    if divisor == 0:
        return [0, 0]
    first_elem = dividend / divisor
    if elem == 1:
        second_elem = avg(dates, total) - first_elem * dateAvg
        return [first_elem, second_elem]
    elif elem == 2:
        second_elem = dateAvg - first_elem * avg(dates, total)
        return [first_elem, second_elem]
    else:
        sys.exit(84)

def apanyan(dates, data, total):
    if len(dates) != len(data):
        sys.exit(84)
    return sqrt(sum(pow((total[0] * dates[i] + total[1]) - data[i], 2) for i in range(len(dates))) / len(dates)) if len(dates) > 0 else 0

def lescramptés(dates, data, total):
    if len(dates) != len(data):
        sys.exit(84)
    return sqrt(sum(pow(((dates[i] - total[1]) / total[0]) - data[i], 2) if total[0] != 0 else 0 for i in range(len(dates))) / len(dates)) if len(dates) > 0 else 0

def main(country_codes):
    if (any(not arg.isupper() for arg in country_codes) or len(country_codes) == 0 or any(any(char.isdigit() for char in arg) for arg in country_codes)):
        st.error("Invalid arguments")
        sys.exit(84)
    try:
        with open("207demography_data.csv", "r") as file:
            data = file.readlines()
        dates = [int(date) for date in data[0].split(";")[2:] if "Country Name" in data[0].split(";")]
        splitData = [line.split(";") for line in data[1:]]
        countries = {line[0]: [int(x) for x in line[2:]] for line in splitData if line[1] in country_codes}
        totalCountries = feur(countries)
        res = quoicoubeh(dates, totalCountries, 1)
        mean = apanyan(dates, totalCountries, res)
        baka = res[0] * 2050 + res[1]
        res2 = quoicoubeh(dates, totalCountries, 2)
        senpai = lescramptés(dates, totalCountries, res2)
        uwu = (2050 - res2[1]) / res2[0]
        cestcontrenatureuh = pow(10, 6)
        st.write("Country:", ", ".join(sorted(countries.keys())))
        st.write(f"Fit1\n    Y = {res[0]/cestcontrenatureuh:.2f} X - {abs(res[1]/cestcontrenatureuh):.2f}")
        st.write(f"    Root-mean-square deviation: {mean/cestcontrenatureuh:.2f}")
        st.write(f"    Population in 2050: {baka/cestcontrenatureuh:.2f}")
        st.write(f"Fit2\n    X = {res2[0]*cestcontrenatureuh:.2f} Y + {abs(res2[1]):.2f}")
        st.write(f"    Root-mean-square deviation: {senpai/cestcontrenatureuh:.2f}")
        try:
            st.write(f"Correlation: {mean / senpai:.4f}")
        except:
            st.write("Correlation: 0.0000")

    except Exception as e:
        st.error("Error", e)
        sys.exit(84)
