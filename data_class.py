class Data:
    def __init__(self, title, best_practice, priority, description, is_obsolete):
        self.title = title
        self.best_practice = best_practice
        self.priority = priority
        self.description = description
        self.is_obsolete = is_obsolete

    def get_title(self):
        return self.title

    def get_best_practice(self):
        return self.best_practice

    def get_priority(self):
        return self.priority

    def get_description(self):
        return self.description

    def get_is_obsolete(self):
        return self.is_obsolete

    def __str__(self):
        return f" Header: {self.title}\n Description: {self.description}\n Best practice: {self.best_practice}"
