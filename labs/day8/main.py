import labs.day8.lsystem as lsys
import labs.day8.draw as draw

# lsys_rule = {
#     "1": "11",
#     "0": "1[0]0"
# }
#
# draw_rule = {
#     "1": draw.one_rule,
#     "0": draw.zero_rule,
#     "[": draw.left_bracket_rule,
#     "]": draw.right_bracket_rule,
# }

lsys_rule = {
    "F": "F-G+F+G-F",
    "G": "GG"
}

draw_rule = {
    "F": draw.one_rule,
    "G": draw.one_rule,
    "-": draw.left_bracket_rule,
    "+": draw.right_bracket_rule,
}

draw.tl.penup()
draw.tl.goto(-200,-200)
draw.tl.pendown()

sys = lsys.LSystem("FG-+", "F-G-G", lsys_rule)
sys.revolveN(8)
draw.draw(sys.getSequence(), draw_rule)

draw.t.exitonclick()
