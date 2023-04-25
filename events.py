class Event:
  def __init__(self, year, title, description, article_link, image_link):
    self.year = year # Int: year of the event (negative if BC)
    self.title = title # String: title of the page with the event
    self.description = description # String: description of event
    self.article_link = article_link # String: link to the Wikipedia article
    self.image_link = image_link # String: link to the image
