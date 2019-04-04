import os

# change this!
subreddit = 'dankmemes'
working_dir = f'/beegfs/work/smapp/reddit_/{subreddit}/'

image_lookup_file = os.path.join(working_dir, 'media.json.gz')

# these files don't exist yet
logits_file = os.path.join(working_dir, 'image_features_copy.csv.gz')
knn_file = os.path.join(working_dir, 'knn.pkl')

# This is where local images are stored
media_dir = os.path.join(working_dir, 'media')

for _dir in [working_dir, media_dir]:
    os.makedirs(_dir, exist_ok=True)