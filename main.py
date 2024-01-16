import pandas as pd
df = pd.read_csv('Video_Games.csv')
columns_to_remove = ['Critic_Score', 'Critic_Count', 'User_Score', 'User_Count', 'Developer', 'Rating']
df.drop(columns=columns_to_remove, inplace=True)
df.drop([659, 14246], inplace=True)
df.reset_index(drop=True, inplace=True)
df = df.sort_values(by='Year_of_Release', ascending=False, na_position='first')
df.reset_index(drop=True, inplace=True)
release_years = [
    2003, 2003, 2008, 2005, 1980, 2007, 2001, 2008, 2006, 2008, 2010, 2007, 1998, 1980, 
    2008, 1977, 2011, 2002, 2002, 2007, 1999, 1997, 1977, 2002, 2011, 2003, 2010, 2011, 
    2002, 2011, 2011, 2006, 2002, 2011, 2008, 2008, 2004, 2010, 2011, 2005, 2011, 2006, 
    2002, 2011, 2008, 2007, 2005, 2002, 2001, 2004, 2003, 1980, 2009, 2011, 1982, 2007, 
    1980, 2004, 1980, 2008, 1981, 2008, 2010, 1999, 2002, 2011, 2001, 2008, 2008, 1978, 
    2007, 2002, 2002, 2006, 2012, 2013, 2011, 2000, 2002, 2010, 1980, 2004, 2002, 1979, 
    2000, 2011, 2002, 2007, 2006, 2002, 2005, 2005, 2002, 2004, 1977, 2011, 1978, 2009, 
    2008, 2011, 2005, 2011, 2006, 2010, 2010, 2010, 2002, 2006, 2002, 2010, 2011, 2004, 
    1992, 1978, 2002, 2012, 2011, 2011, 2010, 1997, 2013, 2011, 2011, 2006, 2011, 2001, 
    2011, 2002, 2005, 2010, 2011, 2002, 2002, 2011, 2001, 2009, 2011, 1978, 2002, 2004, 
    2011, 2009, 2000, 2011, 2005, 2001, 2009, 2003, 2009, 2011, 2012, 2012, 2006, 2002, 
    2010, 2003, 2010, 2006, 2007, 2003, 2011, 2006, 2006, 2009, 2011, 2008, 2011, 2005, 
    2010, 2005, 2009, 1999, 2003, 2009, 2011, 2008, 2014, 2010, 2008, 2011, 2009, 2002, 
    2012, 2011, 2013, 2011, 2008, 2004, 2003, 2010, 2002, 2012, 2011, 2006, 2006, 2008, 
    2005, 2010, 2008, 2006, 2012, 2011, 2007, 2005, 2011, 2006, 2011, 2010, 2007, 1999, 
    2011, 2011, 2016, 1998, 2004, 2003, 2008, 2006, 2009, 2006, 2008, 2004, 2011, 2012, 
    2007, 2009, 2009, 2005, 2005, 2014, 2011, 2003, 2003, 2005, 2012, 2003, 2011, 2006, 
    2009, 2009, 2009, 2009, 2013, 2010, 2009, 2006, 2008, 2004, 2007, 2005, 2008, 2003, 
    2007, 2009, 2011, 2006, 2012, 2003, 2010, 2015, 2009, 2011, 'Cancelled!', 2007, 2008, 
    2003, 2012, 2010, 2004
]
release_years = [year if year != 'Cancelled!' else None for year in release_years]
df.loc[0:268, 'Year_of_Release'] = release_years
df.drop([262], inplace=True)
df.reset_index(inplace=True, drop=True)
publishers = [
    "THQ", "Electronic Arts", "Sega", "Atari", "Nintendo", "Atari", "Banpresto",
    "Konami Digital Entertainment", "Hasbro Interactive", "Nintendo",
    "Nippon Ichi Software", "Capcom", "Hudson Soft Company", "Nintendo", 
    "3 O'Clock", "Microsoft Game Studios", "Alchemist", "Nintendo", 
    "Zoo Publishing", "Gearbox Software", "Namco Bandai Games", "Rejet", "Rejet",
    "7Sixty", "GIANTS Software", "Excalibur Publishing", "Astragon",
    "Excalibur Publishing", "Majesco Entertainment", "Sony Computer Entertainment",
    "Majesco Entertainment", "Majesco Entertainment", "Majesco Entertainment",
    "Majesco Entertainment", "Majesco Entertainment", "Majesco Entertainment",
    "Majesco Entertainment", "Majesco Entertainment", "Majesco Entertainment",
    "Majesco Entertainment", "Majesco Entertainment", "Majesco Entertainment",
    "Majesco Entertainment", "Majesco Entertainment", "Majesco Entertainment",
    "THQ", "Majesco Entertainment", "Majesco Entertainment", "Majesco Entertainment",
    "Majesco Entertainment", "Majesco Entertainment", "Majesco Entertainment",
    "Majesco Entertainment"
]
missing_publisher_indices = df[df['Publisher'].isna()].index
df.loc[missing_publisher_indices, 'Publisher'] = publishers
df.loc[df['Name'] == "Bentley's Hackpack", 'Year_of_Release'] = 2013
df.loc[df['Name'] == "Bentley's Hackpack", 'Platform'] = 'PlayStation Vita'
df.loc[df['Name'] == "Thomas the Tank Engine & Friends", 'Year_of_Release'] = 1993
df.loc[df['Name'] == "Thomas the Tank Engine & Friends", 'Platform'] = 'Genesis'
df.loc[df['Name'] == "Brothers Conflict: Precious Baby", 'Year_of_Release'] = 2016
df.loc[df['Name'] == "Imagine: Makeup Artist", 'Year_of_Release'] = 2009
df.loc[df['Name'] == "Phantasy Star Online 2 Episode 4: Deluxe Package", 'Year_of_Release'] = 2016
df['Genre'] = df['Genre'].replace('Platform', 'Platformer')
df.to_csv('Video_Games_Modified.csv', index=False)