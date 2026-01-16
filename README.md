# reddit-data-collector-v2

Uses a downloaded file from ArcticShift and filters the comments by keyword.

## File structure

### get_and_filter_posts_from_reddit.ipynb
Takes the jsonl outputted by the filtering and collects the right data from it. It will:
1. (Optionally) beautify jsonl for human interpretation.
2. Import posts from the jsonl file into a dataframe for the script
3. Check each comment for any mention of PowerSchool in the title or post body
It will output as a csv file.

This process is repeated for every month, as each month has their own file in the scratch folder

### get_comments_from_posts.ipynb
Given a list of posts, collect all comments relating to the posts.
It will:
1. Take a list of breach posts from the previous Jupyter notebook and gets the post ids. This is formatted as a list to be exported.
2. (Not in this notebook, but) decompress zst files and find all comments that come from the post
3. Import and consolidate the list of comments from the previous step.
4. Collect relevant data for the comment.
5. Format it nicely for review.

### archive/filtered_posts/ and archive/processed_posts/
Data from Arcticshift. This is stored in case the methodology changes so the longest and most resource-consuming part will not have to be repeated.

### archive/breach_post_comments.csv
Output from step 4 of get_comments_from_posts.ipynb.

### archive/breach_post_ids.csv
Output from step 1 of get_comments_from_posts.ipynb.

### archive/comment_tree.csv and archive/comment_tree.txt
Output of get_comments_from_posts.ipynb.

### archive/final_breach_posts.csv
Input of get_comments_from_posts.ipynb.

### arcticshift-processing/aria.sh
File that is ran from the Sol supercomputer job creator. Downloads all posts and comments from the torrent files.

### arcticshift-processing/*.py
Files that are ran from the Sol supercomputer job creator. Decompresses the zst files downloaded from the torrent files.

### arcticshift-processing/torrent-files/*.torrent
Files that hold information about the torrent download. Provided by the Arcticshift repository.