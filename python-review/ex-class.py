class Student:
    def __init__(self, name, kor, math, eng, sci, *i, **kwarg):
        self.name = name  # a.name  self -> a를 가리킴   
        self.kor = kor
        self.math = math
        self.eng = eng
        self.sci = sci
                        ## C언어의 (*this) = self
        return
        
    def get_sum(self):
        self.sum = self.kor + self.math + self.eng + self.sci
        return self.sum

    def get_cal_sum(self):
        return self.sum

    def get_ave(self):
        return self.get_sum() / 4


def main():
    a = Student("choi", 10, 20, 15, 17)
    b = Student("park", 20, 20, 18, 17)
    print(a, b)
    print(a.name)
    print(a.kor)
    print(a.math)
    print(b.name)
    print(b.kor)
    print(b.math)
    print(a.get_sum())
    print(a.get_ave())


if __name__ == "__main__":
    main()