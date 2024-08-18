def save_or_add_grade(file_name, first_name, last_name, grade):
    students = []
    updated = False

    # Dosyada bulunan mevcut öğrencileri oku
    try:
        with open(file_name, 'r') as file:
            for line in file:
                stored_first_name, stored_last_name, stored_grades = line.strip().split(',', 2)
                stored_first_name, stored_last_name = stored_first_name.strip(), stored_last_name.strip()
                if stored_first_name == first_name.strip() and stored_last_name == last_name.strip():
                    # Yeni notu mevcut notlara ekle
                    stored_grades += f", {grade}"
                    students.append((stored_first_name, stored_last_name, stored_grades))
                    updated = True
                else:
                    students.append((stored_first_name, stored_last_name, stored_grades))
    except FileNotFoundError:
        pass

    # Öğrenci dosyada mevcut değilse yeni ekle
    if not updated:
        students.append((first_name, last_name, str(grade)))

    # Dosyayı güncelle
    with open(file_name, 'w') as file:
        for stored_first_name, stored_last_name, stored_grades in students:
            file.write(f"{stored_first_name}, {stored_last_name}, {stored_grades}\n")
    print(f"{first_name} {last_name} için not başarıyla kaydedildi veya eklendi.")

def read_grades(file_name):
    students = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                first_name, last_name, grades = line.strip().split(',', 2)
                # Notları virgülle ayır
                grades_list = [int(grade.strip()) for grade in grades.split(',')]
                # Notları 0 ile 100 arasında sınırla
                grades_list = [max(0, min(100, grade)) for grade in grades_list]
                students.append((first_name.strip(), last_name.strip(), grades_list))
    except FileNotFoundError:
        print(f"{file_name} dosyası bulunamadı.")
    return students

def calculate_average(grades_list):
    # iki not da yoksa her iki notu da 0 kabul et
    if len(grades_list) == 0:
        return 0
    elif len(grades_list) == 1:
        return grades_list[0] * 0.4
    else:
        first_grade = grades_list[0] if len(grades_list) > 0 else 0
        second_grade = grades_list[1] if len(grades_list) > 1 else 0
        return first_grade * 0.4 + second_grade * 0.6

def get_letter_grade(average):
    if average >= 90:
        return "AA"
    elif average >= 85:
        return "BA"
    elif average >= 80:
        return "BB"
    elif average >= 75:
        return "CB"
    elif average >= 70:
        return "CC"
    elif average >= 65:
        return "DC"
    elif average >= 60:
        return "DD"
    elif average >= 50:
        return "FD"
    else:
        return "FF"
    
def printStudentAverage(file_name):
    students = read_grades(file_name)
    for student in students:
        first_name, last_name, grades_list = student
        average = calculate_average(grades_list)
        letter_grade = get_letter_grade(average)
        print(f"{first_name} {last_name}: Ortalama: {average:.2f} Harf Notu: {letter_grade}")

def main_program():
    file_name = "students_grades.txt"

    while True:
        print("\n1. Not Gir")
        print("2. Notları Göster")
        print("3. Not Ortalamalarını Göster")
        print("4. Çıkış")
        choice = input("Seçimin (1/2/3/4): ")

        if choice == '1':
            first_name = input("Öğrencinin adı: ")
            last_name = input("Öğrencinin soyadı: ")
            grade = int(input(f"{first_name} {last_name} ismili öğrencinin notu: "))
            save_or_add_grade(file_name, first_name, last_name, grade)

        elif choice == '2':
            students = read_grades(file_name)
            if students:
                for first_name, last_name, grades_list in students:
                    grades = ", ".join(map(str, grades_list))
                    print(f"{first_name} {last_name}: {grades}")
            else:
                print("Not bulunamadı.")
        
        elif choice == '3':
            printStudentAverage(file_name)
        elif choice == '4':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar dene")

main_program()