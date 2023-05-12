def sqrt(x):
  """
  This function calculates the square root of x to a precision of 2e-16.

  Args:
    x: The number whose square root is to be calculated.

  Returns:
    The square root of x.
  """
  # Check that x is a positive number.
  if x < 0:
    raise ValueError("x must be positive")
  # Modify if you want to make the initial guess more efficient
  y = x/2
  # Iterate until the estimate converges to within a specified tolerance.
  while True:
    # Calculate the next estimate of the square root.
    z = (y + x / y) / 2.0
    # Check if the estimate has converged.
    if abs(y - z) < 2e-16:
      break
    # Update the estimate of the square root.
    y = z
  # Return the square root of x.
  return y
# Find the Square root
print(sqrt(1123))
# >> 33.511192160232085
