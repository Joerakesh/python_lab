# Object Creation and Usage
# Course: Python for Data Science | Loyola College, Chennai
# Student: Joe Rakesh A | Department No.: 26-PDS-002

# Exercise 07 — Object Creation and Usage
class StandardScalerScratch:
    def __init__(self):
        self.mean_ = None
        self.std_ = None
        self.is_fitted = False

    def fit(self, data):
        if not data:
            raise ValueError("data must not be empty")
        self.mean_ = sum(data) / len(data)
        variance = sum((x - self.mean_) ** 2 for x in data) / len(data)
        self.std_ = variance ** 0.5
        if self.std_ == 0:
            self.std_ = 1.0
        self.is_fitted = True
        return self

    def transform(self, data):
        if not self.is_fitted:
            raise RuntimeError("Scaler must be fitted before calling transform()")
        return [(x - self.mean_) / self.std_ for x in data]

    def fit_transform(self, data):
        return self.fit(data).transform(data)

    def inverse_transform(self, scaled_data):
        if not self.is_fitted:
            raise RuntimeError("Scaler must be fitted before inverse_transform()")
        return [x * self.std_ + self.mean_ for x in scaled_data]

train_data = [50, 60, 55, 70, 65, 80, 45]
test_data = [58, 90]
scaler = StandardScalerScratch()
train_scaled = scaler.fit_transform(train_data)
test_scaled = scaler.transform(test_data)
print("Training data:", train_data)
print("Learned mean:", round(scaler.mean_, 2), " Learned std:", round(scaler.std_, 2))
print("Scaled training data:", [round(x, 3) for x in train_scaled])
print("Test data:", test_data)
print("Scaled test data (using train stats):", [round(x, 3) for x in test_scaled])
print("Inverse-transformed:", [round(x, 2) for x in scaler.inverse_transform(train_scaled)])
