from urllib.request import urlopen
from json import loads
import pandas as pd

# Endpoint URLs have the following format:
# /api/v1/schools/edfacts/assessments/{year}/{grade_edfacts}/
# results are limited to 10000 rows
url = "https://educationdata.urban.org/api/v1/schools/edfacts/assessments/2014/grade-8/"
response = urlopen(url)
data = loads(response.read())

jsonData = dict(data)
results_data = jsonData['results']
results_df = pd.DataFrame.from_records(results_data)

print(results_df)