class NewsModel:
    def __init__(self, source, author, title, description, url, urlToImage, publishedAt, content):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

    def __str__(self):
        return f"""
        Source: {self.source}
        Author: {self.author}
        Title: {self.title}
        Description: {self.description}
        Url: {self.url}
        Url To Image: {self.urlToImage}
        Published At: {self.publishedAt}
        Content: {self.content}
        """