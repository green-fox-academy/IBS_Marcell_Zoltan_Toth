class Blog:

    BlogPosts = []

    def add(self, blog):
        self.BlogPosts.append(blog)

    def delete(self, index):
        self.BlogPosts.pop(index)

    def update(self, index, blog):
        self.BlogPosts[index] = blog
