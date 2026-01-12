import pandas as pd

# Read CSV file
df = pd.read_csv("student_data.csv")

print("Original Student Data:")
print(df)

# Add new columns
df["total_marks"] = df["maths"] + df["science"] + df["english"]
df["average_marks"] = df["total_marks"] / 3

# Pass or Fail logic
df["result"] = df["average_marks"].apply(
    lambda x: "Pass" if x >= 40 else "Fail"
)

# Save new CSV file
df.to_csv("student_result_data.csv", index=False)

print("\nProcessed data saved as student_result_data.csv")
