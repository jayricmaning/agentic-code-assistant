from functions.get_files_info import get_files_info

def main():
    # Test 1: Current directory
    print('get_files_info("calculator", "."):')
    print("Result for current directory:")
    result1 = get_files_info("calculator", ".")
    print(result1)
    print()

    # Test 2: 'pkg' directory
    print('get_files_info("calculator", "pkg"):')
    print("Result for 'pkg' directory:")
    result2 = get_files_info("calculator", "pkg")
    print(result2)
    print()

    # Test 3: Outside directory (/bin)
    print('get_files_info("calculator", "/bin"):')
    print("Result for '/bin' directory:")
    result3 = get_files_info("calculator", "/bin")
    print(f"    {result3}")
    print()

    # Test 4: Parent directory (../)
    print('get_files_info("calculator", "../"):')
    print("Result for '../' directory:")
    result4 = get_files_info("calculator", "../")
    print(f"    {result4}")

if __name__ == "__main__":
    main()