from class_student import Student

class Grad_Student(Student):
    def get_gra_sum():
        return self.get_sum() * 10


def main():
    park = Student("choi", 43, 63, 64, 34)
    choi = Grad_Student("choi", 43, 63, 64, 34)
    print(choi.get_ave())
    studs = [park, choi]
    for stud in studs:
         
    print(choi.get_sum())
    print(park.get_sum())
   # print(choi.get_grad_sum())


if __name__ == "__main__":
    main()