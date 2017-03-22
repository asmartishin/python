#!/usr/bin/env python


def reverse(number):
    i = 0
    j = len(number) - 1
    while (i < j):
        tmp = number[i]
        number[i] = number[j]
        number[j] = tmp
        i += 1
        j -= 1
    return number


def convert_to_binary(number):
    result =[]
    while number > 0:
        result.append(number % 2)
        number /= 2
    return reverse(result)


def check_command(pattern, command):
    result = True
    number = convert_to_binary(pattern)
    if len(command) >= len(number):
        number = [0 for x in range(len(command) - len(number))] + number
        for i in range(len(number)):
            if (command[i].isdigit() and number[i] == 1) or (not command[i].isdigit() and number[i] == 0):
                result = False
    else:
        result = False
    return result


if __name__ == '__main__':
    pattern = int(input())
    command = input()
    print(check_command(pattern, command))
