import pandas as pd
import cpv.download_data as download_data
import cpv.clean_data as clean_data
from services.writer import Writer

df = download_data.get_cpv_codes_from_simap("EN")
df = clean_data.remove_check_digits(df)

#df.to_csv('cpv.csv')
#df = pd.read_csv('cpv.csv', dtype={'CODE': object})

Writer.write_json(clean_data.build_tree(df, df), 'cpv_en.json')

