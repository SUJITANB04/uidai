import pandas as pd
import matplotlib.pyplot as plt

files = [
    "data/api_data_aadhar_biometric_0_500000.csv",
    "data/api_data_aadhar_biometric_500000_1000000.csv",
    "data/api_data_aadhar_biometric_1000000_1500000.csv",
    "data/api_data_aadhar_biometric_1500000_1861108.csv"
]

df = pd.concat([pd.read_csv(f) for f in files])

df['total_bio'] = df[['bio_age_5_17','bio_age_17_']].sum(axis=1)

# Graph 1: State-wise volume
state_data = df.groupby('state')['total_bio'].sum().sort_values(ascending=False).head(10)
plt.figure()
state_data.plot(kind='bar')
plt.title("Top 10 States by Aadhaar Biometric Authentication Volume")
plt.xlabel("State")
plt.ylabel("Transactions")
plt.tight_layout()
plt.savefig("graphs/state_biometric_volume.png")
plt.close()

# Graph 2: Age group usage
age_data = df[['bio_age_5_17','bio_age_17_']].sum()
plt.figure()
age_data.plot(kind='bar')
plt.title("Biometric Usage by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Transactions")
plt.tight_layout()
plt.savefig("graphs/age_group_biometric.png")
plt.close()
