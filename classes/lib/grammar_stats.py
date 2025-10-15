class GrammarStats:
    def __init__(self):
        self.total_texts = 0
        self.passed_texts = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        punc_marks = "?!."

        if isinstance(text, str):
            if len(text) > 2:
                if text[0].isupper() and text[-1] in punc_marks:
                    self.passed_texts += 1
                    self.total_texts += 1
                    return True
                self.total_texts += 1
                return False
            raise Exception("Text must be longer than 2 characters in order to be evaluated.")
        raise Exception("Text must be a string.")

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.total_texts > 0:
            return int(100 * (self.passed_texts / self.total_texts))
        return 0
