from colorama import Fore, Back, Style
from emoji import emojize
from components.quizQuestions imports questions
from components import vars, quizTally 

answer1 = questions["q1"][input(questions["q1"]["questions"])]
print(fore.RED + 'answer1')

vars.quizTotal += answer1
print(fore.PINK + '~~*~~*~~*~Answer1~*~~*~~*~~')

answer2 = questions["q2"][input(questions["q2"]["questions"])]
print(fore.RED + 'answer2')

vars.quizTotal += answer2
print(fore.PINK + '~~*~~*~~*~Answer2~*~~*~~*~~')

answer3 = questions["q3"][input(questions["q3"]["questions"])]
print(fore.RED + 'answer3')

vars.quizTotal += answer3
print(fore.PINK + '~~*~~*~~*~Answer3~*~~*~~*~~')

answer4 = questions["q4"][input(questions["q4"]["questions"])]
print(fore.RED + 'answer4')

vars.quizTotal += answer4
print(fore.PINK + '~~*~~*~~*~Answer4~*~~*~~*~~')

answer5 = questions["q5"][input(questions["q5"]["questions"])]
print(fore.RED + 'answer5')

vars.quizTotal += answer5
print(fore.PINK + '~~*~~*~~*~Answer5~*~~*~~*~~')

answer6 = questions["q6"][input(questions["q6"]["questions"])]
print(fore.RED + 'answer6')

vars.quizTotal += answer6
print(fore.PINK + '~~*~~*~~*~Answer6~*~~*~~*~~')

answer7 = questions["q7"][input(questions["q7"]["questions"])]
print(fore.RED + 'answer7')

vars.quizTotal += answer7
print(fore.PINK + '~~*~~*~~*~Answer7~*~~*~~*~~')

answer8 = questions["q8"][input(questions["q8"]["questions"])]
print(fore.RED + 'answer8')

vars.quizTotal += answer8
print(fore.PINK + '~~*~~*~~*~Answer8~*~~*~~*~~')

answer9 = questions["q9"][input(questions["q9"]["questions"])]
print(fore.RED + 'answer9')

vars.quizTotal += answer9
print(fore.PINK + '~~*~~*~~*~Answer9~*~~*~~*~~')

answer10 = questions["q10"][input(questions["q10"]["questions"])]
print(fore.RED + 'answer10')

vars.quizTotal += answer10
print(fore.PINK + '~~*~~*~~*~Answer10~*~~*~~*~~')

answer11 = questions["q11"][input(questions["q11"]["questions"])]
print(fore.RED + 'answer11')

vars.quizTotal += answer11
print(fore.PINK + '~~*~~*~~*~Answer11~*~~*~~*~~')

answer12 = questions["q12"][input(questions["q12"]["questions"])]
print(fore.RED + 'answer12')

vars.quizTotal += answer12
print(fore.PINK + '~~*~~*~~*~Answer12~*~~*~~*~~')

print("total so far: " + str(vars.quizTotal) + "\n")

quizTally.total(vars.quizTotal)