def count_photos(road):
    photos_count = 0
    for i in range(len(road)):
        if road[i]  == '>':
            photos_count += road[i:].count('.')
        if road[i] == '<':
            photos_count += road[:i].count('.')
    
    return photos_count

print(count_photos('>.>..<'))
