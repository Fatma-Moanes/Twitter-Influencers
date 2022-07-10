import pandas as pd
import time

start_time = time.time()
df = pd.read_csv("twitter.csv", names=['Follower', 'ID'], header=None)
# Drop duplicates
df.drop_duplicates(inplace=True)
influencers_df = df.groupby('ID').count().sort_values(by='Follower', ascending=False).reset_index()[:10] # alternative: can be done using value_counts
influencers = influencers_df['ID'].to_list()

# Save results to a file
with open('top_10_influencers.txt', 'w') as f:
    for i in influencers:
        f.write(str(i))
        f.write('\n')

stop_time = time.time()
print('time in seconds: ', stop_time-start_time)
