"""
i mod 10 = <strong>
i mod 3 = <em>
if is_prime(i) is true = <u>
"""

# Initialize lists to store their corresponding numbers
tenth_numbers = []
third_numbers = []
prime_numbers = []

# Initialize number strings for html file
tenth_string = ""
third_string = ""
prime_num_string = ""


def is_prime(num):
    check = 0
    for i in range(2, num):
        if not num % i:
            check += 1
    if not check:
        return True
    else:
        return False
        

for i in range(1, 500 + 1):
    if i % 10 == 0:
        tenth_numbers.append(i)
    if i % 3 == 0:
        third_numbers.append(i)
    elif is_prime(i):
        prime_numbers.append(i)

# Generate 10th numbers string for html file
for num in tenth_numbers:
    if tenth_numbers.index(num) != len(tenth_numbers) - 1:
        tenth_string += f"<strong>{num}</strong>, "
    else:
        tenth_string += f"<strong>{num}</strong>"

# Generate 3rd numbers string for html file
for num in third_numbers:
    if third_numbers.index(num) != len(third_numbers) - 1:
        third_string += f"<em>{num}</em>, "
    else:
        third_string += f"<em>{num}</em>"

# Generate prime-numbers string for html file
for num in prime_numbers:
    if prime_numbers.index(num) != len(prime_numbers) - 1:
        prime_num_string += f"<u>{num}</u>, "
    else:
        prime_num_string += f"<u>{num}</u>"

        
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Interview Solution</title>
</head>
<body>
    <h1>My Solution</h1>
    <p>10th numbers in the series: {}</p> <br>
    <p>3rd numbers in the series: {}</p> <br>
    <p>Prime numbers in the series: {}</p>
</body>
</html>
""".format(tenth_string, third_string, prime_num_string)
        
        
with open("interview_solution.html", "w") as html_file:
    print(html_content, file=html_file)
