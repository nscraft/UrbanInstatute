import pandas as pd

import api_CCD
import api_EDFACTS

CCD = api_CCD.results_df
EDFACTS = api_EDFACTS.results_df

CCD['teacher_student_ratio'] = CCD['teachers_fte'] / CCD['enrollment']

merge_df = pd.merge(CCD, EDFACTS, on='ncessch', how='left')
merge_df_filter = merge_df[merge_df['teacher_student_ratio'].notna() & merge_df['read_test_pct_prof_midpt'].notna()]

print(merge_df_filter[['teacher_student_ratio', 'read_test_pct_prof_midpt']])
