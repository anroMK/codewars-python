def bouncing_ball(h, bounce, window):
    if h <= window or window < 0 or h < 0:
        return -1
    if bounce <= 0 or bounce >= 1: 
        return -1
    ball_pass = -1
    while h > window:
        h *= bounce
        ball_pass += 2
    return ball_pass

# print(bouncing_ball(10, 0.6, 10))
# print(bouncing_ball(2, 0.5, 1))
# print(bouncing_ball(3, 0.66, 1.5))
# print(bouncing_ball(30, 0.75, 1.5))

print(bouncing_ball(-5, 0.66,  1.5))
print(bouncing_ball(5, -1,  1.5))
