def main():
    dict_a = dict()
    dict_b = {}  # 딕셔너리
    dict_c = {0 : 0}  
    print(dict_a, dict_b, dict_c)    
    print(type(dict_a), type(dict_b), type(dict_c))    
    dict_a = {"name": "어벤저스 게임", "type": "히어로 무비"}
    print(dict_a["name"])    
    print(dict_a.get("name"))    
   #print(dict_a["등장인물"])    
    dict_a["등장인물"] = ["헐크", "스티브", "아이언맨"]
    print(dict_a)
    del dict_a["type"]     
    print(dict_a)

    if "name" in dict_a:
        print("'name'은 dict_a 키값에 있어")
    else:
        print("'name'은 dict_a 키값에 없어")

    for key in dict_a:
        print(key, dict_a[key])
    
    for key, value in dict_a.items():
        print(key, value)

if __name__ == "__main__":
    main()