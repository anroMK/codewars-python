def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    root = sq ** 0.5
    return int((root+1) ** 2) if root.is_integer() else -1

print(find_next_square(121))
