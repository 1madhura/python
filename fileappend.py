#appending

try:
    file1=open("writing_to_file.txt","a")
    file1.write("this information recently got appended")
finally:
    print("in finally block")
    file1.close()
