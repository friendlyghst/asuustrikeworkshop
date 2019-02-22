from QUESTION import question

class evaluate:
    """ Contains evaluate_response(response,answer) 
    the function takes in two arguments: response, answer and compares the two to calculae a score.
    """

    def evaluate_response(self, response, answer):
        # checking answer for a match with the default response to question
        # and returns the score based on comparisons
        if response.upper() == answer:
            score = 10
        else:
            score = 0
            
        return score

evaluate = evaluate()
