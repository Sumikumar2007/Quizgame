# ======STOCK MARKET QUIZ GAME======
import pickle   #LIBRARY FOR ACCESSING BINARY FILE

fh=open("QuizGame.dat","wb+")   #OPENING FILE IN WRITING MODE

user={}


#====PRINTING ABOUT GAME====
def about():
     print("This is a text based stock market quiz game \n")
     print("This is for educational purpose only\n ")
     print(" — Here are some game rules : \n")
     print(" → Here you got a question and its four oprions\n")
     print(" → You have to give your answer from those four options by writing it \n")
     print(" → If you give right answer you will get +10 score points")


#-----READING BINARY FILE------

def read():
     fh=open("QuizGame.dat","rb+")
     try:
         data=pickle.load(fh)
         return data
     except EOFError:
          print("File not found")
          return {}

#------REGISTERING USER------

def register():
    print("----NEW USER REGISTER----\n\n")
    username=input("Enter your desired username")
    password=input("Enter your desired password")
    fh=open("user_data.dat","rb")
    print("Opened the file")
    try:
        user_list=pickle.load(fh)
        print("Loaded the file")
        # return -> no use
    except Exception as e:
          print("Error:",e)
          user_list=[]
    for user in user_list:
        if user["username"]==username:
            print("Username already exists.\n Please chose another")
    user_data={"username":username,"password":password,"score":0}
    user_list.append(user_data)
    fh.close()
    fh = open("user_data.dat","rb+")
    pickle.dump(user_list,fh)
    print("Registration Successfull !!")
    
 #----- MAKE USER LOGIN------

def login():
    ("----USER LOGIN----")
    username=input("Enter your registered Usernname: ")
    password=input("Enter your passsword: ")
    try:
         fh=open("user_data.dat","rb")
         user_list=pickle.load(fh)
         
    except EOFError:
          print("File not found")

    for user in user_list:
        if user["username"]==username and user["password"]==password:
            return user
    print("Invalid username or password")     

Quiz_questions = [
    {
        "question": "What does IPO stand for?",
        "options": [
            "(A) Internal Portfolio Option",
            "(B) Investment Portfolio Outlook",
            "(C) Initial Public Offering",
            "(D) Income Producing Organisation"
        ],
        "answer": "C"
    },
    {
        "question": "How many stock exchanges are there in India?",
        "options": [
            "(A) 3",
            "(B) 5",
            "(C) 1",
            "(D) 2"
        ],
        "answer": "D"
    },
    {
        "question": "Which is the first stock exchange of Asia?",
        "options": [
            "(A) Shanghai Stock Exchange (China)",
            "(B) Tokyo Stock Exchange (Japan)",
            "(C) Bombay Stock Exchange (India)",
            "(D) Saudi Exchange (Saudi Arabia)"
        ],
        "answer": "C"
    },
    {
        "question": "Which was the first Indian bank listed on the New York Stock Exchange (NYSE)?",
        "options": [
            "(A) SBI",
            "(B) ICICI",
            "(C) HDFC",
            "(D) RBI"
        ],
        "answer": "B"
    },
    {
        "question": "NASDAQ index belongs to which country?",
        "options": [
            "(A) USA",
            "(B) Africa",
            "(C) India",
            "(D) China"
        ],
        "answer": "A"
    },
    {
        "question": "Which of the following is India's first stock index?",
        "options": [
            "(A) Nifty",
            "(B) Sensex",
            "(C) Nasdaq",
            "(D) Mutual Funds"
        ],
        "answer": "B"
    },
    {
        "question": "Sensex is the stock index of which stock exchange?",
        "options": [
            "(A) Bombay Stock Exchange (BSE)",
            "(B) National Stock Exchange (NSE)",
            "(C) Shanghai Stock Exchange (SSE)",
            "(D) Tokyo Stock Exchange (TSE)"
        ],
        "answer": "A"
    },
    {
        "question": "What is the full form of SENSEX?",
        "options": [
            "(A) Sensitive Index of Bombay Stock Exchange",
            "(B) Sensitive Index of National Stock Exchange",
            "(C) Indian Sectorial Index",
            "(D) Government"
        ],
        "answer": "A"
    }
]

                
# -----RUNNING OF QUIZ-----
def run_quiz():
    print("----STOCK MARKET QUIZ----")
    score=0
    for q in Quiz_questions:
        print("\n"+q["question"])
        for opt in q["options"]:
            print(opt)
        user_ans=input("Enter your answer in (A/B/C/D)").upper()
        if user_ans==q["answer"]:
            print("Hurray !! Right answer")
            score+=10
        else:
            print("OOPS !! Wrong answer")
    print(f"\n Your score:{score}/{len(Quiz_questions)*10}")
    return score
                   # ---- MAIN----

about()
#print("====WELCOME TO STOCK MARKET QUIZ GAME====")
#print("MAIN MENU\n 1. REGISTER(If new user)\n 2. LOGIN & PLAY\n 3. EXIT ")
choice=int(input("Enter your choice between (1-3) : "))
while True:
    print("MAIN MENU\n 1. REGISTER(If new user)\n 2. LOGIN & PLAY\n 3. EXIT ")
    choice=int(input("Enter your choice between (1-3) : "))
    if choice==1:
        register()
    elif choice==2:
        username=login()
        if username:
            # user=pickle.load(fh)
            print(f"Welcome {username} to the Quiz Game")
        #---RUNNING QUIZ-----

        score=run_quiz()
            # ----UPDATING SCORE ----
        if score>username["score"]:
            username["score"]=score
            pickle.dump(username,fh)

            print(f"Your best score: {username['score']}")
            break
    elif choice==3:
        print("Thank you for your time")
        break
    else:
        print("LAADLE AUKAAT MEI")
