"""
# Convert Temperature

Drill: drill-01
Challenge: m1-w1-d2-c1

## Goal

Write a function called `solution` that converts a Celsius temperature to Fahrenheit.

The function receives one value, `celsius`, and must return the Fahrenheit value rounded to 2 decimal places.

Formula:

fahrenheit = (celsius * 9 / 5) + 32

Rules:
- Convert the input to a number using `float()`.
- Return the converted value.
- Round the answer to 2 decimal places.
- Do not print.
- Do not ask for input.

## Files to submit

- `solution.py`

## Allowed functions

- `return`
- `float`
- `round`
"""

# solution

def solution(celsius):
    celsius = float(celsius)
    fahrenheit = (celsius * 9/5) + 32
    ans = round(fahrenheit, 2)
    return ans

def main():
   number = input("give me a number to be converted:", )
   result = solution(number)
   print(result)

main()