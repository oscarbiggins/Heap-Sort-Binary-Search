import random
import numpy as np
class Heapify:
    @staticmethod
    def Run(data_list):
        i = len(data_list)//2 -1 
        Final_End = len(data_list) - 1
        while Final_End >= 0:
            Heapify.Heap_Logic(data_list, i, Final_End)
            if i == 0:
                data_list[0], data_list[Final_End] = data_list[Final_End], data_list[0]
                Final_End -= 1
                i = len(data_list)//2 - 1
            else:
                i -= 1   
    def LeftChild(i, Length_List):
        if 2*i + 1 <= Length_List: 
            return 2*i + 1
        else:
            return -1
    def RightChild(i, Length_List):
        if 2*i + 2 <= Length_List: 
            return 2*i + 2
        else:
            return -1
    def Heap_Logic(data_list, i, Final_End):
        while True:
            Left = Heapify.LeftChild(i, Final_End)
            Right = Heapify.RightChild(i, Final_End)
            if Left == -1 and Right == -1:
                break
            Temp = data_list[i]
            Largest = i
            if Left != -1 and data_list[Left] > data_list[Largest]:
                Largest = Left 
            if Right != -1 and data_list[Right] > data_list[Largest]:
                Largest = Right
            if Largest == i:
                break
            data_list[i], data_list[Largest] = data_list[Largest], data_list[i]
            i = Largest
        return i
    
def Binary_Search(data_list, Response):
    Upper, Lower = len(data_list) -1, 0
    while Lower <= Upper:
        Index = (Lower + Upper) // 2
        if data_list[Index] == Response:
            return Index
        if Response > data_list[Index]:
            Lower = Index + 1
        else:
            Upper = Index - 1
        Index = (Lower + Upper)//2
    return -1



### Initial Set Up
if __name__ == "__main__":
    
    data_list = np.array(random.sample(range(1, 100), random.randint(10,100)))
    data_list = data_list.astype(int)
    print(f"Unsorted List: {data_list}")
    Heapify.Run(data_list)
    print(f"Sorted List: {data_list}")
    ### Heap Sort


    ### Binary Search
    try:
        Response = int(input("Enter number to find: "))
        pos = Binary_Search(data_list, Response)
        if pos != -1:
            print(f"The Numbers Position is index {pos} (Element {pos + 1})")
        else:
            print("Number not found.")
    except ValueError:
        print("Please enter a valid integer.")
        
