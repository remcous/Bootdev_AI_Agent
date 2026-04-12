from functions.get_file_content import get_file_content

def test():
    contents = get_file_content("calculator", "lorem.txt")
    if len(contents) > 10000:
        print(f"Content length: {len(contents)}")
        print(f"End of content: {contents[10000:]}")
    else:
        return f"Error: Content length is less than or equal to 10000 characters, got {len(contents)}"
    print()
        
    contents = get_file_content("calculator", "main.py")
    print(f"Main file content: {contents}")
    print()

    contents = get_file_content("calculator", "pkg/calculator.py")
    print(f"Calculator file content: {contents}")
    print()
    
    try:
        contents = get_file_content("calculator", "/bin/cat")
        print("Unexpectedly succeeded in reading /bin/cat, which should be outside the working directory.")
    except Exception as e:
        print(f"Expected error when trying to read /bin/cat: {e}")
        
    try:
        contents = get_file_content("calculator", "pkg/does_not_exist.py")
        print("Unexpectedly succeeded in reading pkg/does_not_exist.py, which should not exist.")
    except Exception as e:
        print(f"Expected error when trying to read pkg/does_not_exist.py: {e}")
        
    

if __name__ == "__main__":
    test()