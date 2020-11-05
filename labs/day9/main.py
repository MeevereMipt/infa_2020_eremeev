import labs.day9.lsystem as lsys
import labs.day9.draw as draw

lsys_rule = lsys.Rule({
    "1": [
        ["1",0.5],
        ["11",0.4],
        ["11111",0.05],
        ["",-1]
    ],
    "0": "1[0]0"
})
#
draw_rule = {
    "1": draw.one_rule,
    "0": draw.zero_rule,
    "[": draw.left_bracket_rule,
    "]": draw.right_bracket_rule,
}

# lsys_rule = lsys.Rule({
#     "F": [
#         ["F-G+F+G-F", 0.9],
#         ["F+G-G-G+F", -1]
#     ],
#     "G": [
#         ["GG", 0.999],
#         ["G", -1]
#     ]
# })

# draw_rule = {
#     "F": draw.one_rule,
#     "G": draw.one_rule,
#     "-": draw.minus_rule,
#     "+": draw.plus_rule,
# }

for i in range(-400, 400, 200):

    draw.tl.penup()
    draw.tl.goto(i,-200)
    draw.tl.pendown()
    draw.tl.setheading(90)

    # sys = lsys.LSystem("FG-+", "F-G-G", lsys_rule)
    sys = lsys.LSystem("10[]", "0", lsys_rule)
    sys.revolveN(11)

    draw.draw(sys.getSequence(), draw_rule)




draw.t.exitonclick()
