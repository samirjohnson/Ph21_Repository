from astropy.io.votable import parse
import matplotlib.pyplot as plt


"""
We download the VOTABLE file from the following URL for data on Her X-1
https://irsa.ipac.caltech.edu/cgi-bin/ZTF/nph_light_curves?ID=686103400034440%20BANDNAME=g%20FORMAT=VOTABLE ,
save it in the file herx1-votable.xml, and read it in using the astropy tool
for parsing VOTABLE files.
"""
votable = parse('herx1-votable.xml')
table = votable.get_first_table()
data = table.array

# Construct lists for Modified Julian Date and Magnitude
dates_list = []; mags_list = [];
for d in data:
    dates_list.append(d[3])
    mags_list.append(d[4])

# Produce lightcurve plot
plt.scatter(dates_list,mags_list,s=1)
plt.xlabel('Modified Julian Date')
plt.ylabel('Magnitude')
plt.show()

