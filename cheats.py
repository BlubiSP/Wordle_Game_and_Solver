import functions

valid_words = functions.read_list("list_of_valid_guesses.txt")
possible_answers = functions.read_list("answers.txt")

def disgusting(ck, f, mode = "inWord"):
    #ck = current_knowledge which is a list of classes or strings depending on mode
    #f is a possible answer
    #this basically checks every single possible answer and sees if it fits the current knowledge we have.
    #i used short names because i had to write them alot
    new = []
    # There is probably a way to do this way shorter/faster but i could not figure one out
    if mode == "inWord":
        try:
            if ck[0].letter in f and f[ck[0].position] != ck[0].letter and ck[1].letter in f and f[ck[1].position] != ck[1].letter and ck[2].letter in f and f[ck[2].position] != ck[2].letter  and ck[3].letter in f and f[ck[3].position] != ck[3].letter and ck[4].letter in f and f[ck[4].position] != ck[4].letter:
                new.append(f)
        except IndexError:
            try:
                if ck[0].letter in f and f[ck[0].position] != ck[0].letter and ck[1].letter in f and f[ck[1].position] != ck[1].letter and ck[2].letter in f and f[ck[2].position] != ck[2].letter  and ck[3].letter in f and f[ck[3].position] != ck[3].letter:
                    new.append(f)
            except IndexError:
                try:
                    if ck[0].letter in f and f[ck[0].position] != ck[0].letter and ck[1].letter in f and f[ck[1].position] != ck[1].letter and ck[2].letter in f and f[ck[2].position] != ck[2].letter:
                        new.append(f)
                except IndexError:
                    try:
                        if ck[0].letter in f and f[ck[0].position] != ck[0].letter and ck[1].letter in f and f[ck[1].position] != ck[1].letter:
                            new.append(f)
                    except IndexError:
                        if ck[0].letter in f and f[ck[0].position] != ck[0].letter:
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
    # this creates a new list of possible answers with the current knowledge we have
    #ck = current_knowledge as a dictionary with 
    ## Example: We know the letter in the second position is "a", there is no "w" or "r" and there is an "e" somewhere but not in position 3
    # {'inWord': [class with .letter e and .position3], 'correctPosition': [class with .letter a and .position 2], 'notinWord': ['w', "r"]}
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

    return new3