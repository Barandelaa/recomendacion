from surprise import SVD


class SVDModel:
    def __init__(self):
        self.model = SVD()

    def fit(self, trainset):
        self.model.fit(trainset)

    def predict(self, user_id, item_id):
        return self.model.predict(user_id, item_id).est

    def get_model(self):
        return self.model