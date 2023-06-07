import streamlit as st
import math
import time

def compute_binomial_coefficient(n, k):
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)

def binomial_distribution(appel, people, hour, phones=25):
    stock = appel / (60 * 60 * hour)
    Overload = 0
    timer = time.time()
    result_text = ""
    for i in range(0, 51):
        result = math.factorial(people) // (math.factorial(i) * math.factorial(people - i)) * (stock ** i) * ((1 - stock) ** (people - i))
        if i > 0 and i % 5 == 0:
            result_text += "\n"
        if (i + 1 > 0 and (i + 1) % 5 == 0) or i == 50:
            result_text += "%d -> %.3f" % (i, result)
        else:
            result_text += "%d -> %.3f" % (i, result) + "\t"
        if i > phones:
            Overload += result
    Overload = 1 if appel > 320 else Overload
    result_text += "\nOverload: %.1f%%" % (Overload * 100)
    end = time.time()
    result_text += "\ncomputation time: %.2f ms\n" % ((end - timer) * 1000)
    st.write(result_text)

def poisson_distribution(appel, people, hour, phones=25):
    stock = people * (appel / (60 * 60 * hour))
    final_proba = [math.exp(-stock) * (stock ** i) / math.factorial(i) for i in range(51)]
    timer = time.time()
    result_text = ""
    for i, p in enumerate(final_proba):
        if i > 0 and i % 5 == 0:
            result_text += "\n"
        if (i + 1 > 0 and (i + 1) % 5 == 0) or i == 50:
            result_text += "%d -> %.3f" % (i, p)
        else:
            result_text += "%d -> %.3f" % (i, p) + "\t"
    Overload = sum(final_proba[phones + 1:])
    Overload = 1 if appel > 320 else Overload
    result_text += "\nOverload: %.1f%%\n" % (Overload * 100)
    end = time.time()
    result_text += "\ncomputation time: %.2f ms" % ((end - timer) * 1000)
    st.write(result_text)
