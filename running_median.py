# Running Median Problem


def median(arr):
	"""Finds the median of a list

    Args:
        arr: A list to find median of.

    Returns:
        Median of the list.
    """
    # length of the list
	elements = float(len(arr))
	# half the length of the list
	mid = elements/2
	# if length of list is even
	if(int(mid) == mid):
		# sets the index of the mid value in the list
		mid = int(mid)-1
		# returns the calculated median
		return float((arr[mid] + arr[mid+1]))/2
	# if length of list is odd
	else:
		# returns the median
		return arr[int(mid)]

# input the total number of elements in the list
total_elements = int(input())
# a list to store the input elements
elements = []
# a list to store the median of the list after each input element
medians = []
# loop to input elements
for x in range(total_elements):
	# stores the input element in the elements list
	elements.append(input())
	# calculates the median of the list
	medians.append(median(elements))

# prints the median list
for median in medians:
	print(median)
