import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import joblib
import os


class DataHandler:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.countries = sorted(self.df["country"].unique())

    def list_countries(self):
        return self.countries

    def get_country_data(self, country):
        return self.df[self.df["country"].str.lower() == country.lower()]


class PopulationModel:
    def __init__(self, country):
        self.country = country
        self.model_filename = (
            f"{country.replace(' ', '_').lower()}_population_model.pkl"
        )
        self.model = None

    def train(self, X, y):
        self.model = LinearRegression()
        self.model.fit(X, y)
        joblib.dump(self.model, self.model_filename)

    def load_or_train(self, X, y):
        if os.path.exists(self.model_filename):
            print("\nLoading existing model...")
            self.model = joblib.load(self.model_filename)
        else:
            print("\nTraining new model...")
            self.train(X, y)
            print(f"Model saved as {self.model_filename}")

    def predict(self, X):
        return self.model.predict(X)


class Evaluator:
    @staticmethod
    def evaluate(y_true, y_pred):
        mse = mean_squared_error(y_true, y_pred)
        mae = mean_absolute_error(y_true, y_pred)
        r2 = r2_score(y_true, y_pred)
        mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
        rmspe = np.sqrt(np.mean(np.square((y_true - y_pred) / y_true))) * 100
        return mse, mae, mape, rmspe, r2


class PopulationForecaster:
    def __init__(self, csv_path, forecast_horizon=3):
        self.data_handler = DataHandler(csv_path)
        self.forecast_horizon = forecast_horizon

    def run(self):
        countries = self.data_handler.list_countries()
        print("Available countries:")
        for country in countries:
            print(f"- {country}")

        try:
            country = input(
                "\nEnter the name of the country to forecast population: "
            ).strip()
            if country.lower() not in [c.lower() for c in countries]:
                raise ValueError("Invalid country name.")
        except ValueError as e:
            print(f"Error: {e}")
            return

        data = self.data_handler.get_country_data(country)
        if data.empty:
            print(f"No data found for country: {country}")
            return

        X = data[["year"]]
        y = data["population"]

        model = PopulationModel(country)
        model.load_or_train(X, y)
        y_pred = model.predict(X)

        # Evaluation
        mse, mae, mape, rmspe, r2 = Evaluator.evaluate(y, y_pred)
        print("\nModel Evaluation on Historical Data:")
        print(f"Mean Squared Error (MSE): {mse:,.2f}")
        print(f"Mean Absolute Error (MAE): {mae:,.2f}")
        print(f"Mean Absolute Percentage Error (MAPE): {mape:.2f}%")
        print(f"Root Mean Squared Percentage Error (RMSPE): {rmspe:.2f}%")
        print(f"R² Score: {r2:.4f}")

        # Forecast future
        last_year = data["year"].max()
        future_years = pd.DataFrame(
            {"year": [last_year + 10 * i for i in range(1, self.forecast_horizon + 1)]}
        )
        forecast = model.predict(future_years)

        print(f"\nPopulation Forecast for {country}:")
        for year, pop in zip(future_years["year"], forecast):
            print(f"{year}: {int(pop):,}")

        # Plot
        plt.scatter(X, y, color="blue", label="Actual")
        plt.plot(X, y_pred, color="green", label="Fitted Line")
        plt.scatter(future_years, forecast, color="red", label="Forecast")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.title(f"Population Forecast for {country}")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()


# Run the forecaster
if __name__ == "__main__":
    csv_path = r"C:\Users\Kline (OJT)\Desktop\workshop\world_population\ml_model\csv\AI_world_population.csv"
    forecaster = PopulationForecaster(csv_path)
    forecaster.run()
