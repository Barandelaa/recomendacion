import surprise

class evaluator:
    def __init__(self, model):
        self.model = model

    def evaluate(self, testset):
        predictions = self.model.test(testset)
        return surprise.accuracy.rmse(predictions)