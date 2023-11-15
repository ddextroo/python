from pingouin import ancova
import pandas as pd
import numpy as np

data = pd.DataFrame({'methodology': np.repeat(['A', 'B', 'C'], 4),
					'current_grade': [67, 88, 75, 85,
									92, 77, 74, 88,
									91, 88, 82, 80],
					'test_score': [77, 89, 74, 69,
									88, 93, 94, 90,
									85, 81, 83, 79]})

ancova(data=data, dv='test_score', covar='current_grade', between='methodology')
