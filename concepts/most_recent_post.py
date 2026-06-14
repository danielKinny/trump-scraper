#check if the most recent post is not pinned and also not in the latest.txt document
#logic behind checking if its a new post
def new_post(post):
    with open('latest.txt', 'r') as f:
        latest_posts = f.read().splitlines()
    
    if post['pinned'] == False and post['id'] not in latest_posts:
        return True
    else:
        return False