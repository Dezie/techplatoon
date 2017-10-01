from task import  Task


class BoardList:
    def __init__(self, name):
        pass
    
    def add_task(self):
        pass

    def delete_board_list(self):
        pass

    def view_tasks(self):
        pass
class card(object):
    """Class that matches a dict with card details from json api response."""

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, dict):
            return other.get("name", None) == self.name
        return NotImplemented

    def __repr__(self):
        return "{}({!r}, {!r})".format(
            self.__class__.__name__, self.key, self.value)


if __name__ == '__main__':
    pass
