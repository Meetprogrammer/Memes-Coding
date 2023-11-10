def aayein():
    name = input("Jis class me padte ho, naam batao: ")
    print(f"Aayein aayein, {name}, std 6") #name aditya
    subject = input("Yeh batao konsa subject acha lagta hai: ")
    print(f"Aayein, aayein your favorite subject is {subject}")
    if subject.lower() =='baingain':
        print("arre, 'baingain' konsa subject hai...?")
    else:
        print(f"nice, {subject} is a great subject")

    poem = input("koi poem yaad hai english mai..? (yes/ha): ")
    if poem.lower() in['yes','ha']:
        poem_name = input("konasa poem yaad hai: ")
        if poem_name == '55':
            print("arre, 55 ka spelling yaad hai....?")

        else:
            print(f"nice, {poem_name} is a great poem")

    pm_name = input("acha desh ke pradhan mantri ji ka naam bataye: ")

    if pm_name.lower() == 'niteshishkumar' or pm_name.lower() == 'laluyadav':
        print("laluyadav..? pradhanmantri? no, its modi")
    elif pm_name.lower() == 'modi':
        print("ji ha modi sarkar")

aayein()