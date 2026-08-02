while True:
    choice = input("Выбери действие: 1-добавить, 2-посмотреть, 3-выйти: ")
    
    if choice == "1":
        task = input("Текст задачи: ")

        with open("todo.txt", "a") as file:
            file.write(task + "\n")
        

        
    elif choice == "2":

        with open("todo.txt", "r") as file:
            for line in file:
                print(line, end = "")

    elif choice == "3":
        break