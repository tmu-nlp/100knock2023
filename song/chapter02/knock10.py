#Listing and making lines elements in list
def lines(file):
    lines = file.readlines()
    return lines

#Count the number of elements in list
def count_lines(lines):
    count_lines = len(lines)
    return count_lines

#Count the total number of the lines of file
def total_lines(filename):
    with open(filename) as file:
        total_lines = count_lines(lines(file))
        return total_lines
