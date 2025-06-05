# forth.py

import sys
import operator as op


# Types
Word = str
Number = (int, float)


std_dict = {
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
    "/": op.truediv,
}

stack = []


def tokenize(inpt: str):
    "Break input string into tokens"
    return inpt.upper().split(" ")


def typer(token: str):
    "Numbers become numbers, everything else becomes a word"
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Word(token)


def main() -> int:
    "A basic Forth calculator"

    while True:
        user_input = input(">")

        if user_input.upper() == "QUIT":
            break

        tokens = tokenize(user_input)

        status = "err"

        for token in tokens:
            typed_token = typer(token)

            if typed_token in std_dict:
                a = stack.pop()
                b = stack.pop()
                stack.append(std_dict[typed_token](b, a))
                status = "ok"
            elif isinstance(typed_token, Number):
                stack.append(typed_token)
                status = "ok"
            else:
                break

        sys.stdout.write(f"\033[F")  # Move cursor up
        sys.stdout.write(f"\033[{len('>' + user_input)}C")  # Move to EOL

        if status == "ok":
            sys.stdout.write(" ok\n")
            print(stack)
        else:
            sys.stdout.write("?\n")

        sys.stdout.flush()

    return 0


if __name__ == "__main__":
    sys.exit(main())
