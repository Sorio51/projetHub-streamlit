import streamlit as st
from math import pow, factorial

values = [[0.00, 0.02, 0.06, 0.15, 0.27, 0.45, 0.71, 1.07, 1.64, 2.71, 3.84, 5.41, 6.63],
            [0.02, 0.21, 0.45, 0.71, 1.02, 1.39, 1.83, 2.41, 3.22, 4.61, 5.99, 7.82, 9.21],
            [0.11, 0.58, 1.01, 1.42, 1.87, 2.37, 2.95, 3.66, 4.64, 6.25, 7.81, 9.84, 11.34],
            [0.301, 1.06, 1.65, 2.19, 2.75, 3.36, 4.04, 4.88, 5.99, 7.78, 9.49, 11.67, 13.28],
            [0.55, 1.61, 2.34, 3.00, 3.66, 4.35, 5.13, 6.06, 7.29, 9.24, 11.07, 13.39, 15.09],
            [0.87, 2.20, 3.07, 3.83, 4.57, 5.35, 6.21, 7.23, 8.56, 10.64, 12.59, 15.03, 16.81],
            [1.24, 2.83, 3.82, 4.67, 5.49, 6.35, 7.28, 8.38, 9.80, 12.02, 14.07, 16.62, 18.48],
            [1.65, 3.49, 4.59, 5.53, 6.42, 7.34, 8.35, 9.52, 11.03, 13.36, 15.51, 18.17, 20.09],
            [2.09, 4.17, 5.38, 6.39, 7.36, 8.34, 9.41, 10.66, 12.24, 14.68, 16.92, 19.68, 21.67],
            [2.56, 4.87, 6.18, 7.27, 8.30, 9.34, 10.47, 11.78, 13.44, 15.99, 18.31, 21.16, 23.21]]

def lethimcook(values, free_d, sum_sq):
    f_val = ""
    if values[free_d][0] > sum_sq:
        f_val = "P > 99%"
    else:
        for i in range(len(values)):
            if values[free_d][i] > sum_sq:
                if i == 0:
                    f_val = "99% > P > 90%"
                elif i > 0 and i <= 10:
                    f_val = str(100 - i * 10) + "% < P < " + str(100 - (i - 1 if i > 1 else i) * 10) + "%"
                else:
                    if i == 10:
                        f_val = "5% < P < 2%"
                    elif i == 11:
                        f_val = "2% < P < 1%"
                return f_val
        f_val = "P < 1%"
    return f_val

def main(values):
        quoicoubeh = [st.number_input(f"Value {i+1}", min_value=0, max_value=100, value=values[i]) for i in range(9)]
        if sum(quoicoubeh) != 100 or sum(1 for number in quoicoubeh if number < 0) > 0:
            st.error("Invalid input! The sum of values should be 100 and all values should be non-negative.")
            return

        off_l, off_r = 0, 0
        res, feur = [], []

        prob = sum([i * quoicoubeh[i] for i in range(len(quoicoubeh))]) / pow(10, 4)

        while quoicoubeh[0] < 10:
            quoicoubeh[0] = quoicoubeh[0] + quoicoubeh[1]
            quoicoubeh.remove(quoicoubeh[1])
            off_l += 1

        quoicoubeh.reverse()

        while quoicoubeh[0] < 10:
            quoicoubeh[0] = quoicoubeh[0] + quoicoubeh[1]
            quoicoubeh.remove(quoicoubeh[1])
            off_r += 1

        quoicoubeh.reverse()

        for i in range(8):
            feur.append((factorial(100) / (factorial(i) * factorial(100 - i))) * 100 * pow(1 - prob, 100 - i) * pow(prob, i))

        feur.append(100 - sum(i for i in feur))
        res.append(sum(feur[:off_l + 1]))
        res += (i for i in feur[off_l + 1:])
        res = res[:len(res) - 1 - off_r]
        res.append(sum(i for i in feur[(len(feur) - 1 - off_r):]))

        st.header("Output")
        st.write("Ox: ", end='')
        st.write("\t|\t".join(str(i) for i in quoicoubeh) + "\t|\t100")
        st.write("Tx: ", end='')
        st.write("\t|\t".join("%.1f" % i for i in res) + "\t|\t100")

        st.write("Distribution: B(100, %.4f)" % prob)
        st.write("Chi-squared: %.3f" % sum(pow(quoicoubeh[i] - res[i], 2) / res[i] for i in range(len(res))))
        st.write("Degrees of freedom: %d" % (len(res) - 2))
        st.write("Fit validity: %s" % lethimcook(values, len(res) - 2, sum(pow(quoicoubeh[i] - res[i], 2) / res[i] for i in range(len(res)))))