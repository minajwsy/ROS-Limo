import datetime

def main():
    now = datetime.datetime.now()

    if now.hour < 12:
        print("현재 시각은 {now.hour}시로 오전이야")

    if now.hour > 12:
        print("현재 시각은 {now.hour}시로 오후야")

    if 2 < now.month <6:
        print(f"이번 달은 {now.month}월이므로 봄이야")
    elif 5 < now.month < 9:
        print(f"이번 달은 {now.month}월이므로 여름이야")
    elif 8 < now.month < 12:
        print(f"이번 달은 {now.month}월이므로 가을이야")
    else:
        print(f"이번 달은 {now.month}월이므로 겨울이야")
    
if __name__ == "__main__":
    main()