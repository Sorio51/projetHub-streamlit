import sys
import streamlit as st

def open_file():
    file = open("log/help.txt", "r+")

    for i in range(11):
        print(file.readline())
    file.close()

def PrintLine():
    st.write("--------------------------------------------------------------------------------")

def CalculUnsold(a, b, x, y):
    top = (a - x) * (b - y)
    bot = (5 * a - 150) * (5 * b - 150)
    result = top / bot
    return float(result)

def CalculLawY(stock, j, tab):
    result = 0
    for i in range(5):
        result += stock[j][i]
    tab[0][j] = result
    st.write("%.3f" % result)
    return tab

def CalculLawX(stock, tabX):
    st.write("X law\t")
    final = 0
    for j in range(5):
        result = 0
        for i in range(5):
            result += stock[i][j]
        final += result
        tabX[1][j] = result
        st.write("%.3f\t" % result)
    st.write("%.3f" % final)
    return tabX

def CalcFirstPart(a, b):
    tabX = [[0.000, 0.000, 0.000, 0.000, 0.000],[0.000, 0.000, 0.000, 0.000, 0.000]]
    x = 10
    y = 10
    stock = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
    st.write("\tX=10\tX=20\tX=30\tX=40 \tX=50\tY law")
    for j in range(5):
        x = 10
        st.write("Y=%.i\t" % y)
        for i in range(5):
            stock[j][i] = CalculUnsold(a, b, x, y)
            st.write("%.3f\t" % stock[j][i])
            x += 10
        tabX = CalculLawY(stock, j, tabX)
        y += 10
    tabX = CalculLawX(stock, tabX)
    return tabX

def PrintFirstLine(z):
    st.write("z\t")
    while (z <= 100):
        if (z == 100):
            st.write(z)
        else:
            st.write(z)
        z += 10

def CalcSecondPart(a, b):
    z = 2
    PrintFirstLine(20)
    st.write("p(Z=z)")
    for z in range(2, 11):
        stock = 0.0
        result = 0.0
        for j in range(1, 6):
            for i in range(1, 6):
                result = CalculUnsold(a, b, i * 10, j * 10)
                if (i + j == z and j < 6):
                    stock += result
        if (z != 10):
            st.write("%0.3f\t" % stock)
        else:
            st.write("%0.3f" % stock)

def PrintLastPart(a, b, c, d):
    st.write("expected value of X:\t%0.1f" % a)
    st.write("variance of X:\t\t%0.1f" % b)
    st.write("expected value of Y:\t" + "%0.1f"    % c)
    st.write("variance of Y:\t\t%0.1f" % d)
    st.write("expected value of Z:\t%0.1f" % (a + c))
    st.write("variance of Z:\t\t%0.1f" % (b + d))

def CalcLastPart(a, b, tab):
    x = 0
    y = 0
    X = 0
    Y = 0
    for i in range(1, 6):
        x += (i * 10) * tab[1][i - 1]
    for j in range(1, 6):
        y += (j * 10) * tab[0][j - 1]

    for i in range(1, 6):
        X += ((i * 10) - x)**2 * tab[1][i - 1]
    for j in range(1, 6):
        Y += ((j * 10) - y)**2 * tab[0][j - 1]
    PrintLastPart(x, X, y, Y)

def MainUnsold(a, b):
    tab1 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    PrintLine()
    tab1 = CalcFirstPart(a, b)
    PrintLine()
    CalcSecondPart(a, b)
    PrintLine()
    CalcLastPart(a, b, tab1)
    PrintLine()
    sys.exit(0)

if __name__ == "__main__":
    if (len(sys.argv) == 2 and sys.argv[1] == "-h"):
        open_file()
        sys.exit(0)
    if (len(sys.argv) != 3):
        sys.exit(84)
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except ValueError:
        sys.exit(84)
    if (a < 50 or b < 50):
        sys.exit(84)
    MainUnsold(a, b)
    sys.exit(0)
