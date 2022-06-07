def banner_text(text: str = " ", screen_width: int = 80) -> None:

    if len(text) > screen_width -4:
        raise ValueError(f"String {text} is larger than the specified width {screen_width}")

    if text == "*":
        print("*" * screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = "**{0}**".format(centred_text)
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("Life goes on my jolly friend")
banner_text("What can we do")
banner_text("*")
#banner_text("Always look on the bright side of life...Always look on the bright side of life...Always look on the bright side of life...")
