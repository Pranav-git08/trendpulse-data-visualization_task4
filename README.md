## TrendPulse - Task 4: Data Visualization ## 

### Project Overview
This is the final step of the pipeline. I used *Matplotlib* to create visual reports based on the data we collected and analyzed in the previous tasks.

### Visualizations Created:
1. **Top 10 Stories**: A horizontal bar chart showing which stories got the highest scores. I made sure to shorten the titles so the graph stays readable.
2. **Category Count**: A bar chart with different colors showing how many stories we found in each category (Tech, Science, etc.).
3. **Score vs Comments**: A scatter plot that shows the relationship between upvotes and discussion. I colored the dots based on whether the story was "popular" (above average score).
4. **Dashboard (Bonus)**: A combined figure that shows all three charts together in one image.

### Folder Structure:
task4_visualization.py`: The main script.
outputs : All the generated graphs are saved here as PNG files.
data : Contains the `trends_analysed.csv` file used for the plots.

### How to run:
Make sure you have matplotlib and pandas installed, then run:
python task4_visualization.py 
