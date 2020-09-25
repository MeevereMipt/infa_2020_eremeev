import turtle as t
t.shape("turtle")

n = 12
for i in range(1,n+1):
    t.forward(50)
    t.stamp()
    t.left(180)
    t.forward(50)
    t.left(360/n)

t.exitonclick()

