def fib(n: int) -> int:
  if n == 1:
    return 0
  if 2 <= n <= 3:
    return 1
  return fib(n - 1) + fib(n - 2)

fib(42)
