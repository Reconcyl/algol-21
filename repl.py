print("""ALGOL 21 REPL

"If we all need to putatively agree, guess what we're going to have? We're
going to have elections. We're going to have a democracy. And if you are having
elections with your open-source project, you have failed. You have failed.
Nobody should be casting a vote for the leadership of an open source project.

And the reason elections are so corrosive, the reason they are so divisive, is
that there are two side effects you cannot avoid from elections. One's politics,
the other's losers. Who wants to be in a community of politics and losers?"
""")

while True:
    try:
        line = input("> ")
    except EOFError:
        break
    print("\x1b[31mError\x1b[m: <stdin>, line 1")
    print(line)
    print("^")
    print("Invalid syntax")
