# Calculate the sum of diagonal elements in a graph/2D List
# Example:
# [[1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]] --> 15
def sumDiagonal(a):
    total = 0
    j = 0
    for i in range(len(a)):
        total += a[i][j]
        j += 1
    return total

# Write a function that returns a tuple containing the first and second largest values in a list


def firstSecond(givenList):
    first = max(givenList)
    second_max = min(givenList)
    for i in givenList:
        if i > second_max and i < first:
            second_max = i
    return (first, second_max)


# Write a function that returns the missing value in a contigeous sequenc of numbers
def missingNumber(myList, totalCount):
    nums_sum = (totalCount*(totalCount+1))/2
    current_sum = sum(myList)
    return nums_sum-current_sum

# Write a function that returns a list cotnaining only unique values from a given list


def removeDuplicates(myList):
    temp = []
    solution = []
    for i in myList:
        if i in temp:
            solution.append(i)
        else:
            temp.append(i)
    return temp


# Write a function that returns a list of containing the pairs of integers that add up to a given total
def pairSum(myList, total):
    solution = []
    # Save values in a dictionary
    for i in range(len(myList)):
        if total-myList[i] in myList[i+1:]:
            solution.append((myList[i], total-myList[i]))
    return solution
