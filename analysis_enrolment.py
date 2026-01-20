import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/aadhaar_enrolment.csv")

state_enrol = df.groupby('state')['enrolment_count'].sum().sort_values(ascending=False).head(10)

plt.figure()
state_enrol.plot(kind='bar')
plt.title("State-wise Aadhaar Enrolment Distribution")
plt.xlabel("State")
plt.ylabel("Enrolments")
plt.tight_layout()
plt.savefig("graphs/state_enrolment.png")
plt.close()
