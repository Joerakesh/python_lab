# Program Involving Inheritance
# Course: Python for Data Science | Loyola College, Chennai
# Student: Joe Rakesh A | Department No.: 26-PDS-002

# Exercise 08 — Program Involving Inheritance
from abc import ABC, abstractmethod

class Estimator(ABC):
    @abstractmethod
    def fit(self, X, y):
        pass

    @abstractmethod
    def predict(self, X):
        pass

    def score(self, X, y):
        predictions = self.predict(X)
        return sum((pred - actual) ** 2 for pred, actual in zip(predictions, y)) / len(y)

class MeanRegressor(Estimator):
    """Baseline model: always predicts the mean of the training target."""
    def fit(self, X, y):
        self.mean_ = sum(y) / len(y)
        return self

    def predict(self, X):
        return [self.mean_ for _ in X]

class LinearRegressor(Estimator):
    """Simple least-squares linear regression for a single feature."""
    def fit(self, X, y):
        if len(X) != len(y) or len(X) < 2:
            raise ValueError("X and y must have equal length >= 2")
        n = len(X)
        x_mean = sum(X) / n
        y_mean = sum(y) / n
        numerator = sum((X[i] - x_mean) * (y[i] - y_mean) for i in range(n))
        denominator = sum((x - x_mean) ** 2 for x in X)
        if denominator == 0:
            raise ValueError("X must contain at least two distinct values")
        self.slope_ = numerator / denominator
        self.intercept_ = y_mean - self.slope_ * x_mean
        return self

    def predict(self, X):
        return [self.slope_ * x + self.intercept_ for x in X]

X = [1, 2, 3, 4, 5]
y = [3, 4, 6, 7, 9]
for model in [MeanRegressor(), LinearRegressor()]:
    model.fit(X, y)
    print(f"{model.__class__.__name__}:")
    print(" Predictions:", [round(p, 2) for p in model.predict(X)])
    print(f" MSE: {model.score(X, y):.3f}\n")
