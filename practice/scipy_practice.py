from matplotlib.pyplot import plot, savefig
from scipy import linspace
from scipy import optimize
from scipy import special

f = lambda x:-special.jv(3, x)
sol = optimize.minimize(f, 1.0)
x = linspace(0, 10, 5000)
plot(x, special.jv(3, x), '-', sol.x, -sol.fun, 'o')
savefig('plot.png', dpi=96)
