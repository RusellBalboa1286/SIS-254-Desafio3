import math

def taylor_sin(x, n):
    """Calcula la aproximación de Taylor de la función seno para un número de términos n."""
    taylor_approx = 0
    for i in range(n):
        # Los términos impares de la serie de Taylor para el seno
        coef = (-1)**i
        term = coef * (x**(2*i + 1)) / math.factorial(2*i + 1)
        taylor_approx += term
    return taylor_approx

# Valores de x en radianes (tomados de la tabla)
x_values = [0.523598776, 0.785398163, 1.047197551, 1.570796327, 3.141592654,
            4.71238898, 6.283185307, 0.392699082, 0.261799388, 0.314159265]

# Número de términos (n) en la serie de Taylor (también tomados de la tabla)
n_terms = [3, 4, 5, 6, 7, 8, 9, 2, 2, 3]

# Crear la tabla de resultados
print(f"{'x (radianes)':>15} {'n':>5} {'Aprox Taylor':>15} {'Valor Exacto':>15} {'Error Absoluto':>15}")
for x, n in zip(x_values, n_terms):
    approx_taylor = taylor_sin(x, n)
    valor_exacto = math.sin(x)
    error_absoluto = abs(valor_exacto - approx_taylor)
    
    print(f"{x:>15.9f} {n:>5} {approx_taylor:>15.9f} {valor_exacto:>15.9f} {error_absoluto:>15.9f}")
