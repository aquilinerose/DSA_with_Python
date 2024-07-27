def reverse(arr):
    reversed_arr = arr[::-1]
    print("The reversed arr is:", end = " ")
    for i in reversed_arr:
        print(i,end =  " ")
    
arr = [4,2,9,7,5,4]
reverse(arr)