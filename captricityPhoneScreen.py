starting_string = "aaabbcdddabbcccdddd"
correct_answer =  "a3b2c1d3a1b2c3d4"
    
def compress(string):
    result = ""
    counter = 1

    for i in range(1, len(string)):

        if string[i] == string[i - 1]:
            counter += 1

        else:
            result += string[i - 1] + str(counter)
            counter = 1

    result += string[len(string) - 1] + str(counter)

    return result
