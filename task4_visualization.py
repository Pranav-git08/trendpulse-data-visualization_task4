import pandas as pd
import matplotlib.pyplot as plt
import os

# 1 — Setup (2 marks)
print(" Starting Task 4: Visualizations ")

# Create the outputs folder if it doesn't exist
if not os.path.exists('outputs'):
    os.makedirs('outputs')
    print("Created 'outputs/' folder.")

# Load the analyzed data from Task 3
csv_path = "data/trends_analysed.csv"
if not os.path.exists(csv_path):
    print(f"Error: {csv_path} not found. Run Task 3 first!")
else:
    df = pd.read_csv(csv_path)
    print(f"Loaded {len(df)} stories for visualization.")

    # 2 — Chart 1: Top 10 Stories by Score (6 marks)
    plt.figure(figsize=(10, 6))
    top_10 = df.nlargest(10, 'score').copy()
    
    # Shorten titles longer than 50 characters for better display
    top_10['short_title'] = top_10['title'].apply(lambda x: x[:47] + '...' if len(x) > 50 else x)
    
    plt.barh(top_10['short_title'], top_10['score'], color='skyblue')
    plt.gca().invert_yaxis()  # Put the highest score at the top
    plt.title('Top 10 Stories by Score')
    plt.xlabel('Score')
    plt.ylabel('Story Title')
    plt.tight_layout()
    plt.savefig('outputs/chart1_top_stories.png')
    print("Saved Chart 1.")

    # 3 — Chart 2: Stories per Category (6 marks)
    plt.figure(figsize=(10, 6))
    cat_counts = df['category'].value_counts()
    # Using a list of colors to make each bar different
    colors = ['tomato', 'cornflowerblue', 'gold', 'mediumseagreen', 'orchid']
    
    cat_counts.plot(kind='bar', color=colors[:len(cat_counts)])
    plt.title('Number of Stories per Category')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('outputs/chart2_categories.png')
    print("Saved Chart 2.")

    # 4 — Chart 3: Score vs Comments (6 marks)
    plt.figure(figsize=(10, 6))
    # Filter popular vs non-popular for different colors
    popular = df[df['is_popular'] == True]
    not_popular = df[df['is_popular'] == False]
    
    plt.scatter(not_popular['score'], not_popular['num_comments'], color='gray', alpha=0.5, label='Regular')
    plt.scatter(popular['score'], popular['num_comments'], color='orange', edgecolors='red', label='Popular')
    
    plt.title('Score vs Number of Comments')
    plt.xlabel('Score')
    plt.ylabel('Number of Comments')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.savefig('outputs/chart3_scatter.png')
    print("Saved Chart 3.")

    # Bonus — Dashboard (+3 marks)
    # Creating a 2x2 layout (one slot will be empty or we can span across)
    fig, axs = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('TrendPulse Dashboard', fontsize=20, fontweight='bold')

    # Re-plot 1 in top-left
    axs[0, 0].barh(top_10['short_title'], top_10['score'], color='skyblue')
    axs[0, 0].invert_yaxis()
    axs[0, 0].set_title('Top 10 Stories')

    # Re-plot 2 in top-right
    cat_counts.plot(kind='bar', color=colors[:len(cat_counts)], ax=axs[0, 1])
    axs[0, 1].set_title('Category Distribution')

    # Re-plot 3 in bottom-left
    axs[1, 0].scatter(not_popular['score'], not_popular['num_comments'], color='gray', alpha=0.5)
    axs[1, 0].scatter(popular['score'], popular['num_comments'], color='orange')
    axs[1, 0].set_title('Score vs Comments')
    
    # Hide the empty 4th subplot
    axs[1, 1].axis('off')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig('outputs/dashboard.png')
    print("Saved Dashboard.")

    # Show the dashboard at the very end
    plt.show()

    print(" Task 4 Complete ")
    
    