import math

while True:
    grade = int(input("What is the grade: "))
    if grade == int(4):
        total_words_read = int(input("Total Words Read ORF: "))
        total_errors = int(input("Total Errors ORF: "))

        total_words_correct = total_words_read - total_errors

        percentage_part_one = total_words_correct / total_words_read
        percentage_part_two = round(percentage_part_one * 100, 2)

        maze_question = int(input("Maze Correct: "))
        maze_question_2 = int(input("Maze Incorrect: "))

        maze = (maze_question_2 / 2 - maze_question) * -1

        orf_wrc = total_words_read * 36.42
        orf_acc = percentage_part_two * 0.06
        maze_total = maze * 6.29

        total = orf_wrc + orf_acc + maze_total

        step_3 = total - 4563
        step_4 = step_3 / 1771
        step_5 = step_4 * 40

        time = input("When was it done? (Beginning = B, Middle = M, End = E) ")

        if time == "B":
            step_5 += 360
        elif time == "M":
            step_5 += 400
        elif time == "E":
            step_5 += 440
        print(step_5)
        print("Next!")
        continue
    elif grade == int(5):
        total_words_read = int(input("Total Words Read ORF: "))
        total_errors = int(input("Total Errors ORF: "))

        total_words_correct = total_words_read - total_errors

        percentage_part_one = total_words_correct / total_words_read
        percentage_part_two = round(percentage_part_one * 100, 2)

        maze_question = int(input("Maze Correct: "))
        maze_question_2 = int(input("Maze Incorrect: "))

        maze = (maze_question_2 / 2 - maze_question) * -1

        orf_wrc = total_words_read * 31.12
        orf_acc = percentage_part_two * 0.03
        maze_total = maze * 4.58

        total = orf_wrc + orf_acc + maze_total

        step_3 = total - 4085
        step_4 = step_3 / 1299
        step_5 = step_4 * 40

        time = input("When was it done? (Beginning = B, Middle = M, End = E) ")

        if time == "B":
            step_5 += 360
        elif time == "M":
            step_5 += 400
        elif time == "E":
            step_5 += 440
        print(step_5)
        print("Next!")
        continue


