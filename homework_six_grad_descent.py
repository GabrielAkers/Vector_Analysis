# note that I did this at 6 in the morning the day this was due and only implemented it for the specific function given
# in the homework assignment. maybe ill update it later if i feel like it to be more general i.e. work with an arbitrary
# smooth function. also there's no error handling at all so probably easy to break idk.


def f(x, y):
    return (x-2)^2+2*(y-1)^2


def grad_f(x, y):
    return [2*(x-2), 4*(y-1)]


# i'm pretty sure in normal gradient descent you're supposed to have the step size be a paramater of the model but like
# i said it's 6am; I'm just doing a constant
step = 0.1

# lol
close_enough = 0.0001


def grad_desc(x, y, n=0):
    # without importing some packages python doesn't have a good way to multiply a list by a scalar to get the negative
    # of the gradient so i just used a list comprehension. again: 6am
    direction = [i * -1 for i in grad_f(x, y)]

    # print(direction)

    # stop when the gradient is "almost" zero. i.e. the curve flattens out. note this is prone to getting stuck if the
    # surface isn't convex everywhere, but w/e it works here since the surface is a paraboloid
    if abs(direction[0]) <= close_enough and abs(direction[1]) <= close_enough:
        return [x, y, "iterations: {0}".format(n)]

    x1 = x + step * direction[0]
    y1 = y + step * direction[1]

    # just some stupid indexing stuff since i chose to implement this recursively and I want to see how many
    # iterations it takes to converge
    m = n + 1

    return grad_desc(x1, y1, m)




