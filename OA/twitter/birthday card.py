# Python3 program for the
# above approach
 
# Function to return nearest
# lower character
def nextAvailableChar(charset,
                      start):
 
    # Traverse charset from start-1
    for i in range(start - 1,
                   -1, -1):
        if (charset[i] > 0):
            charset[i] -= 1
            return chr(i + ord('a'))
           
    # If no character can be
    # appended
    return '\0'
 
# Function to find largest
# string
def newString(originalLabel,
              limit):
 
    n = len(originalLabel)
 
    # Stores the frequency of
    # characters
    charset = [0] * (26)
 
    newStrings = ""
 
    for i in originalLabel:
        charset[ord(i) -
                ord('a')] += 1
 
    # Traverse the string
    for i in range(25, -1, -1):
        count = 0
 
        # Append larger character
        while (charset[i] > 0):
            newStrings += chr(i + ord('a'))
 
            # Decrease count in
            # charset
            charset[i] -= 1
 
            # Increase count
            count += 1
 
            # Check if count reached
            # to charLimit
            if (charset[i] > 0 and
                count == limit):
 
                # Find nearest lower char
                next = nextAvailableChar(charset, i)
 
                # If no character can be
                # appended
                if (next == '\0'):
                    return newStrings
 
                # Append nearest lower
                # character
                newStrings += next
 
                # Reset count for next
                # calculation
                count = 0
 
    # Return new largest string
    return newStrings


if __name__ == '__main__':
    test = 'zzazcz'
    print(newString(test,2))
    