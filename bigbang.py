import json

result = []
# Loop through numbers 1 to 100
for num in range(1, 101):
    # Check if number is divisible by 3, 5 or both
    if num % 3 == 0 and num % 5 == 0:
        result.append("BIGBANG")
    # Check if number is divisible by 3
    elif num % 3 == 0:
        result.append("BIG")
    # Check if number is divisible by 5
    elif num % 5 == 0:
        result.append("BANG")
    # If number is not divisible by 3 or 5, append the number
    else:
        result.append(str(num))

# Write the result to output.json
with open('output.json', 'w') as outfile:
    json.dump(result, outfile)

print("output.json file created successfully!")