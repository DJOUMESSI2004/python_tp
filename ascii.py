if __name__ == '__main__':
    pass



# decoder un message ascii

def decrypt(message: [int]) -> str:
    return ''.join(chr(num) for num in message)

if __name__ == '__main__':
    encrypted = [105, 115, 32, 97, 109]
    print(decrypt(encrypted)) 




# function de tri 

def my_sort(my_list: [int]) -> [int]:
    sorted_list = my_list[:]
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    return sorted_list

if __name__ == '__main__':
    print(my_sort([4, 2, 5, 1, 3]))
