import numpy as np
from scipy import stats

# Przykładowe dane: sprzedaż w PLN na sklep w okresie testowym
sales_control = np.array(
    [1200, 1350, 1100, 1400, 1250, 1300, 1150, 1380, 1220, 1290]
)
sales_test = np.array(
    [1450, 1500, 1380, 1600, 1420, 1550, 1390, 1480, 1510, 1460]
)

# Test t-Welcha (equal_var=False odpowiada za wariant Welcha)
t_stat, p_value = stats.ttest_ind(sales_test, sales_control, equal_var=False)

print(f"Statystyka t: {t_stat:.4f}")
print(f"p-value: {p_value:.6f}")

if p_value < 0.05:
    print(
        "Wynik jest istotny statystycznie (odrzucamy H0). Zmiana na półce wpłynęła na sprzedaż."
    )
else:
    print(
        "Brak podstaw do odrzucenia H0. Różnica w sprzedaży może być dziełem przypadku."
    )