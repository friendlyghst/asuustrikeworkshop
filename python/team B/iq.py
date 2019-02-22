from QUESTION import question
from test import evaluate
from newfile import enoch

class Question:
    """ Contains quest(). A function that contains the list
    of questions to be asked
    """
    
    def quest(self):
        
        print("Pick an Option")
        
        # a list of questions
        list = [
        "Oliver Twist was published by who? (A)  Oliver Twist, (B) Charles Dickens: ",
        "What was the name of Alexander the great's horse? (A) Alonso, (B) Bucaphalus: ",
        "According to greek mythology, who is the god of thunder? (A) Ogun, (B) Thor: "
        ]
        
        # an empty list to store the results of each questions asked
        score = []
        
        # a loop that iterates through the elements in the list of questions
        for el in list:
            question1 = question.ask_question(el)   # calls the ask_question() function from the question class in QUESTION
            scoree = evaluate.evaluate_response(question1,"B")  # calls the evaluate_response() function from the evaluate class in test 
            score.append(scoree)   #append the result of the evaluate_response() function to score
        
        # prints the score of each question on the console
        print(score)
        # returns the sum of elements in score
        tiq = sum(score)
         
        # displays the iq score on the console
        print("Your IQ is:", tiq)        

        

Question = Question()

if __name__ == "__main__":
    enoch.welcome()

    
    Question.quest()

    enoch.goodbye()
