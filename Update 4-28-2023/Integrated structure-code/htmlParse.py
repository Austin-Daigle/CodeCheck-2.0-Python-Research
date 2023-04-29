def print_slices(pattern,input):
    
    max_value = len(input)
    
    result = ""

    last_right = 0
    for i in range(len(a)):
        left, right = a[i]

        if last_right != left:
            #print(f"{last_right} ~ {left}", end=" *")

            if last_right > left:
                print(f"|*!| {last_right} ~ {left} |")
            else:
                print(f"|* | {last_right} ~ {left} | \"{input[last_right:left]}\"")
                result += input[last_right:left]


        if i < len(a) - 1 and right > a[i + 1][0]:
            right = a[i + 1][0]
            print(f"| !| {left} ~ {right} | <mark>\"{input[left:right]}\"</mark>")
            result += f"<mark>{input[left:right]}</mark>"
        else:
            print(f"|  | {left} ~ {right} | <mark>\"{input[left:right]}\"</mark>")
            result += f"<mark>{input[left:right]}</mark>"

        last_right = right

    if last_right != max_value:
        print(f"|* | {last_right} ~ {max_value} | \"{input[last_right:max_value]}\"")
        result += input[last_right:max_value]
    return result

a = [[0, 4], [9, 20], [23, 35]]
input = "The quick brown fox jumps over the lazy dog."
print("input length: ",len(input))
print(print_slices(a, input))
