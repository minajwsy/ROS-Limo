#import datetime

def main():
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    
    print(list_a + list_b)
    print(list_a * 3)
    list_a.append("추가원소")
    list_a.insert(1, "insert 추가원소")
    print(list_a)
    del list_a[2]
    print(list_a)
    list_a.pop(1)  # [1, 3, "추가원소"]
    print(list_a)
    list_a.remove(3)
    print(list_a)

    if 5 in list_b:
        print("5는 리스트b에 있어")
    else:
        print("5는 리스트b에 없어")

    for j, i in enumerate(list_b):
        print(f"{j+1} 번째 원소는 {i}입니다")

if __name__ == "__main__":
    main()