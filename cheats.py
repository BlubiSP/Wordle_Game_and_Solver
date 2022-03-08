import sys
sys.path.append('C:/Users/stefa/Desktop/test/wordle solver/')
import functions

valid_words = functions.read_list("list.txt")
possible_answers = functions.read_list("answers.txt")


def get_best_starter(valid_words = valid_words, possible_answers = possible_answers):
    for f in valid_words:
        for i in possible_answers:
            pass
def get_score(guess, answer):
    inWord, correctPosition, notinWord = functions.evaluate(guess, answer).values()

def disgusting(ck, f, mode = "inWord"):
    new = []
    if mode == "inWord":
        try:
            if ck[0].letter in f and ck[1].letter in f and ck[2].letter in f  and ck[3].letter in f and ck[4].letter in f:
                new.append(f)
        except IndexError:
            try:
                if ck[0].letter in f and ck[1].letter in f and ck[2].letter in f  and ck[3].letter in f:
                    new.append(f)
            except IndexError:
                try:
                    if ck[0].letter in f and ck[1].letter in f and ck[2].letter in f:
                        new.append(f)
                except IndexError:
                    try:
                        if ck[0].letter in f and ck[1].letter in f:
                            new.append(f)
                    except IndexError:
                        if ck[0].letter in f:
                            new.append(f)
    elif mode == "notinWord":
        try:
            if ck[0] not in f and ck[1] not in f and ck[2] not in f  and ck[3] not in f and ck[4] not in f and ck[5] not in f and ck[6] not in f and ck[7] not in f and ck[8] not in f and ck[9] not in f and ck[10] not in f:
                new.append(f)
        except IndexError:
            try:
                if ck[0] not in f and ck[1] not in f and ck[2] not in f  and ck[3] not in f and ck[4] not in f and ck[5] not in f and ck[6] not in f and ck[7] not in f and ck[8] not in f and ck[9] not in f:
                    new.append(f)
            except IndexError:
                try:
                    if ck[0] not in f and ck[1] not in f and ck[2] not in f  and ck[3] not in f and ck[4] not in f and ck[5] not in f and ck[6] not in f and ck[7] not in f and ck[8] not in f:
                        new.append(f)
                except IndexError:
                    try:
                        if ck[0] not in f and ck[1] not in f and ck[2] not in f  and ck[3] not in f and ck[4] not in f and ck[5] not in f and ck[6] not in f and ck[7] not in f:
                            new.append(f)
                    except IndexError:
                        try:
                            if ck[0] not in f and ck[1] not in f and ck[2] not in f  and ck[3] not in f and ck[4] not in f and ck[5] not in f and ck[6] not in f:
                                new.append(f)
                        except IndexError:
                            try:
                                if ck[0] not in f and ck[1] not in f and ck[2] not in f  and ck[3] not in f and ck[4] not in f and ck[5] not in f:
                                    new.append(f)
                            except IndexError:
                                try:
                                    if ck[0] not in f and ck[1] not in f and ck[2] not in f  and ck[3] not in f and ck[4] not in f:
                                        new.append(f)
                                except IndexError:
                                    try:
                                        if ck[0] not in f and ck[1] not in f and ck[2] not in f  and ck[3] not in f:
                                            new.append(f)
                                    except IndexError:
                                        try:
                                            if ck[0] not in f and ck[1] not in f and ck[2] not in f:
                                                new.append(f)
                                        except IndexError:
                                            try:
                                                if ck[0] not in f and ck[1] not in f:
                                                    new.append(f)
                                            except IndexError:
                                                if ck[0] not in f:
                                                    new.append(f)
    elif mode == "correctPosition":
        try:
            if ck[0].letter == f[ck[0].position] and ck[1].letter == f[ck[1].position] and ck[2].letter == f[ck[2].position]  and ck[3].letter == f[ck[3].position] and ck[4].letter == f[ck[4].position]:
                new.append(f)
        except IndexError:
            try:
                if ck[0].letter == f[ck[0].position] and ck[1].letter == f[ck[1].position] and ck[2].letter == f[ck[2].position]  and ck[3].letter == f[ck[4].position]:
                    new.append(f)
            except IndexError:
                try:
                    if ck[0].letter == f[ck[0].position] and ck[1].letter == f[ck[1].position] and ck[2].letter == f[ck[2].position]:
                        new.append(f)
                except IndexError:
                    try:
                        if ck[0].letter == f[ck[0].position] and ck[1].letter == f[ck[1].position]:
                            new.append(f)
                    except IndexError:
                        if ck[0].letter == f[ck[0].position]:
                            new.append(f)
    return new

def get_list_of_possible_answers(ck, possible_answers):
    new = []
    new2 = []
    new3 = []
    for f in possible_answers:
        if len(ck['correctPosition']) > 0:
            new += disgusting(ck["correctPosition"], f, "correctPosition")

    if new:    
        for f in new:
            if ck["notinWord"]:
                new2 += disgusting(ck["notinWord"], f, "notinWord")

            else:
                new2 = new

    else:
        for f in possible_answers:
            if ck["notinWord"]:
                new2 += disgusting(ck["notinWord"], f, "notinWord")

            else:
                new2 = possible_answers
            
    for f in new2:
        if ck["inWord"]:
            new3 += disgusting(ck["inWord"], f, "inWord")

        else:
            new3 = new2

    return "\n".join(new3)


def get_best_guess(in_, out, perfect):
    pass