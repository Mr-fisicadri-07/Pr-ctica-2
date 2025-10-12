# this is a simple script to reverse the digits of a number
digit_input = str(input("Please insert your digits: "))

digit_list = digit_input.split(",")

print(digit_list)

inverted_list = reversed (digit_list)

print(inverted_list)

inverted_digits = " " .join(inverted_list)

print(inverted_digits)