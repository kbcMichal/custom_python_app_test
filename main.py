from keboola.component import CommonInterface
import os
import csv

ci = CommonInterface()
# access user parameters
print(ci.configuration.parameters)

# Create directory structure if it doesn't exist
os.makedirs('data/out/tables', exist_ok=True)

# Create empty CSV with one column
with open('data/out/tables/test.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['whatever'])  # Header row with one column named "whatever"

