try:
    file1=open("LICENSE.txt")
    text=file1.read(5)
    print("the text is\n",text)
finally:
    print("In finally block")
    file1.close()
