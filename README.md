# Tableau Video Game Sales Dashboard

Interactive Tableau dashboard comparing the number of video game copies sold between publishers, games, platforms, genres and regions. Includes the best selling games from the years 1977 to 2016.

### [Link to dashboard.](https://public.tableau.com/app/profile/aidan.casselman/viz/VideoGameSales_16892091832450/Global)

[<img align="left" alt="Dashboard" width="800px" style="padding-right:10px;" src="https://github.com/Aidan-Casselman/tableau-video-game-sales-dashboard/blob/main/dashboard.png" />](https://public.tableau.com/app/profile/aidan.casselman/viz/VideoGameSales_16892091832450/Global)
<br clear="left"/>
---
This repo showcases the steps I took to clean and prepare the dataset for use in the Tableau dashboard.

## Original Data Cleaning & Preparation Steps
Originally I prepared the data for use in Tableau using Excel. Here are the steps I took:
1. Download video game sales dataset .csv from: https://data.world/sumitrock/video-games-sales Dataset published by: Sumit Kumar Shukla
2. Remove columns K-P (Critic_Score, Critic_Count, User_Score, User_Count, Developer, Rating) from 1st dataset as they are irrelevant to our dashboard.
3. Remove rows 661 and 14248 as the name and genre are blank.
4. Sort by Year_of_Release, descending
5. 269 rows do not have a Year_of_Release. 
6. MobyGames Release Date Extractor found 208 of the missing dates
7. Modified 29 game names to match name in MobyGames.com database
8. MobyGames Release Date Extractor found 26 more missing dates
9. Remaining 35 dates were found by manual Google search
10. Remove row 264 (Brothers in Arms: Furious 4) as it is a canceled game
11. 53 Games do not have a Publisher
12. Changed “Bentley’s Hackpack” Year_Of_Release to 2013, and changed platform to PlayStation Vita as it appears that this is the first ever release of the game and a 2005 GBA release is impossible.
13. Changed “Thomas the Tank Engine & Friends” Year_Of_Release to 1993, and changed platform to Genesis as this is the most likely game that the original dataset is referring to. No 2004 GBA releases of the game were found.
14. Changed “Brothers Conflict: Precious Baby” Year_Of_Release to 2016
15. Changed “Imagine: Makeup Artist” Year_Of_Release to 2009
16. Changed both instances of “Phantasy Star Online 2 Episode 4: Deluxe Package” Year_Of_Release to 2016
17. The 53 missing publishers were found by manual Google search
18. Replaced all instances of “Platform” genre with “Platformer” as it is more widely used

## Jupyter Notebook
I have included a jupyter notebook (.ipynb) file that performs all the operations outlined in the [Data Cleaning & Preparation Steps](original-data-cleaning-&-preparation-steps) section.

## main.py
I have also included a simple python file that completes all of the [Data Cleaning & Preparation Steps](original-data-cleaning-&-preparation-steps) and saves the modified .csv file as "Video_Games_Modified.csv". Start by downloading the data from [this](https://data.world/sumitrock/video-games-sales) link. Then simply run the python file to reach the state the dataset was in when I imported it to Tableau.