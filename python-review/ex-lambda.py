def power(n: int) -> int:
    return n*n

def under200(n: int) -> bool:
    return n < 200

def main():
    li = [i+1 for i in range(20)]
    out_map=map(power, li)
    out_filter = filter(under200, li)
    print("map 결과", list(out_map))
    print("filter 결과", list(out_filter))

if __name__ == "__main__":
    main()