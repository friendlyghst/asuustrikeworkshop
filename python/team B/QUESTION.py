#question object
class question:
    """ Contains a function that takes in an input question as an argument
    and returns the question as a response"""
    
    def ask_question(self,question):
        response = input(question)
        return response

question = question()
