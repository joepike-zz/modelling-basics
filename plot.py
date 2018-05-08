from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [234.5, 256.7, 300.4, 319.0, 317.2, 330.5, 343.7]

plt.plot(years, gdp)

plt.title("Nominal GDP")

plt.ylabel("Billions of $")

plt.show()
