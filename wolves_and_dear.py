def wolves_and_dear(deer, wolves, deer_growth, deer_predation, wolves_predation, wolves_decay, dt, n):
    max_wolves = 0
    for i in range(n):
        wolves = wolves + dt * (wolves_predation * wolves * deer - wolves_decay * wolves)
        deer = deer + dt * (deer_growth * deer - deer_predation * wolves * deer)
        max_wolves = max(max_wolves, wolves)
    return max_wolves


if __name__ == '__main__':
    print(wolves_and_dear(1.5, 1.5, 0.6666666666666666, 1.3333333333333333, 1, 1, 0.01, 500))
