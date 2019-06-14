import matplotlib.pyplot as plt

def pridobi_tocke(velikost):
    x = []
    y = []
    with open(f"..\\cleni\\{velikost}.IGS") as dat:
        a = dat.readlines()
        for line in a:
            if line[-9] == 'P' and line.count(',') == 4:
                line = line.split(',')
                if line[3] == '0.':
                    x.append(float(line[1]))
                    y.append(float(line[2]))

    # Da je zvezno dodaj prvo točko še na koncu
    x.append(x[0])
    y.append(y[0])

    plt.plot(x, y)
    plt.show()
    
    return x, y