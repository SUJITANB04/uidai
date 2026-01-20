import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

df = pd.read_csv("data/api_data_aadhar_biometric_0_500000.csv")
df['date'] = pd.to_datetime(df['date'])
df['total_bio'] = df[['bio_age_5_17','bio_age_17_']].sum(axis=1)

monthly = df.resample('M', on='date')['total_bio'].sum()

model = ARIMA(monthly, order=(1,1,1))
model_fit = model.fit()

forecast = model_fit.forecast(steps=6)

plt.figure()
monthly.plot(label="Actual")
forecast.plot(label="Forecast")
plt.legend()
plt.title("Forecasted Aadhaar Biometric Demand")
plt.xlabel("Month")
plt.ylabel("Transactions")
plt.tight_layout()
plt.savefig("graphs/forecast_biometric.png")
plt.close()
