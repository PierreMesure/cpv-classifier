import pandas as pd
from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen

URL_CPV_CODES = "https://simap.ted.europa.eu/documents/10184/36234/cpv_2008_xls.zip"

def get_cpv_codes_from_simap(language):
    zipfile = ZipFile(BytesIO(urlopen(URL_CPV_CODES).read()))
    data = pd.read_excel(zipfile.open(zipfile.namelist()[0]))
    data.rename(columns = {language:'name'}, inplace = True)
    return data[['CODE', 'name']]
