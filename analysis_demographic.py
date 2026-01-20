import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/aadhaar_demographic.csv")

# Gender-wise coverage
gender = df.groupby('gender')['aadhaar_count'].sum()
plt.figure()
gender.plot(kind='bar')
plt.title("Gender-wise Aadhaar Coverage")
plt.xlabel("Gender")
plt.ylabel("Aadhaar Count")
plt.tight_layout()
plt.savefig("graphs/gender_coverage.png")
plt.close()

# Age group coverage
age = df.groupby('age_group')['aadhaar_count'].sum()
plt.figure()
age.plot(kind='bar')
plt.title("Age Group-wise Aadhaar Coverage")
plt.xlabel("Age Group")
plt.ylabel("Aadhaar Count")
plt.tight_layout()
plt.savefig("graphs/age_coverage.png")
plt.close()
