class Post_it:
    bg_color = ""
    text = ""
    text_color = ""

    def __init__(self, bg_color, text, text_color):
        self.bg_color = bg_color
        self.text = text
        self.text_color = text_color

    def print(self):
        print("bg_color = " + self.bg_color)
        print("text = " + self.text)
        print("text_color = " + self.text_color)
