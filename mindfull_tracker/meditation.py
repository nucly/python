import datetime, time


class Meditation:
    def __init__(self, m_type, comment):
        self.m_type = m_type
        self.date = datetime.datetime.now().date().strftime("%d/%m/%Y")
        self.time = datetime.datetime.now().time().strftime("%H:%M")
        self.comment = comment

    def __str__(self):
        return f'{self.m_type} meditation: {self.date} {self.time}'

    def __eq__(self, other):
        if (self.m_type == other.m_type and self.date == other.date
                and self.time == other.time and self.comment == other.comment):
            return True

    # It's approriate to give something for __hash__ when you override __eq__
    # #This is the recommended way if mutable (like it is here):
    __hash__ = None

    def __repr__(self):  # added to make list of items invoke str
        return self.__str__()
