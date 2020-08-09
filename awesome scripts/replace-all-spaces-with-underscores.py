import os

directory = '~/Documents/experiment'

# Replace all spaces with underscore and also replace the string '[some.random_string]' with nothing
[os.rename(os.path.join(directory, f), os.path.join(directory, f).replace(' ', '_').replace('[some.random_string]', '')) for f in os.listdir(directory)]