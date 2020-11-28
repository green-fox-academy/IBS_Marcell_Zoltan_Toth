class BlogPost():

    author_name = ""
    title = ""
    text = ""
    publication_date = ""

    def __init__(self, author, title, text, date):
        self.author_name = author
        self.title = title
        self.text = text
        self.publication_date = date

    def print(self):
        print("author_name = " + self.author_name)
        print("title = " + self.title)
        print("text = " + self.text)
        print("publication_date = " + self.publication_date)



