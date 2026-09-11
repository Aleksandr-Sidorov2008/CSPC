from time import perf_counter
from decay import simulate_loop, simulate

N0 = 20000

t0 = perf_counter()
simulate_loop(N0,0.4)
t_loop = perf_counter() - t0

t0 = perf_counter()
simulate(N0,0.4)
t_numpy = perf_counter() - t0

speedup = t_loop / t_numpy

print(f"Pure Python loop time: {t_loop:.4f} s")
print(f"NumPy simulate time:   {t_numpy:.4f} s")
print(f"Speed-up factor:       {speedup:.2f}x faster")