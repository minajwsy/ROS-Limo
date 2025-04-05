def main():
    abc = 4
    print(abc, type(abc))   # abc: class of int
    abc = 4.5
    print(abc, type(abc))   # abc : float
    abc = "this is python"  # abc: str
    print(abc, type(abc))

    # format -- f-string
    abc = "fstring"
    number = 3.1415
    print(f"string string {abc} pi : {number: .3}")
    input_var = input("input num")
    print(f"input number is {input_var}")
    print(f"plus 30 is : {int(input_var) * 30}")

if __name__ == "__main__":
    main()