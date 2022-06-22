#file read2

try:
    file1=open("LICENSE.txt")
    text=file1.read(9)
    print("the first 9characters are\n",text)
    next_text=file1.read(20)
    print("the next set of 20 characters are\n",next_text)
finally:
    print("in finally block")
    file1.close()
