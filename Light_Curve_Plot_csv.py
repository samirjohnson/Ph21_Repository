import csv
import urllib.request
import matplotlib.pyplot as plt

# URL for data
url = 'https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves?ID=686103400034440%20BANDNAME=g%20FORMAT=CSV'

# Fetch data from url in CSV format
url_obj = urllib.request.urlopen(url)
csv_reader = csv.reader(url_obj.read().decode('utf-8').splitlines())

# Construct data list from CSV
data_list = []
for d in csv_reader:
  data_list.append(d[0].replace(' ','').replace('<TD>','').replace('</TD>',''))

# Reduce data list to only include relevant entries
index1 = data_list.index('<TABLEDATA>') + 1
index2 = data_list.index('</TABLEDATA>')
data_list_new = data_list[index1:index2]
print(data_list_new[:100])

# Construct lists for Modified Julian date and magnitude from complete data
# list and convert lists from string entries to float entries
dates_list_str = data_list_new[4::26]
mags_list_str = data_list_new[5::26]
dates_list = [float(d) for d in dates_list_str]
mags_list = [float(m) for m in mags_list_str]

# Construct and show lightcurve plot
plt.scatter(dates_list, mags_list, s=1)
plt.xlabel('Modified Julian Date')
plt.ylabel('Magnitude')
plt.show()
