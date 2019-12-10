from prettycli import green

class DataGroup:
    def __init__(self, title, data_list=[]):
        self.title = title
        self.data_list = list(data_list)

    def __str__(self):
        left_of_title = (38 - len(self.title)) // 2
        right_of_title = 38 - len(self.title) - left_of_title
        string = "┌" + "─" * left_of_title + self.title + "─" * right_of_title + "┐\n"
        for row in self.data_list:
            string = string + str(row) + "\n"
        string += "└" + "─" * 38 + "┘" + "\n"
        return string


class OutputData:
    def __init__(self, key, data, data_unit="", width=34, color=green().bold().copy()):  # TODO move width
        self.key = key
        self.data = data
        self.data_unit = data_unit
        self.width = width
        self.color = color

    def __str__(self):
        left = str(self.key)
        right = f"{self.data} {self.data_unit}"
        n_spaces = self.width - len(left) - len(right)
        left = self.color(left).to_str()
        right = self.color(right).to_str()
        spaces = "─" * n_spaces
        return f"│ {left} {spaces} {right} │"
