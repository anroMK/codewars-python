def like_or_dislike(lst):
    status = 'Nothing'
    for i in lst:
        if i != status:
            status = i
        else:
            status = 'Nothing'
    return status


print(like_or_dislike(['Dislike']))
print(like_or_dislike(['Dislike', 'Like']))


