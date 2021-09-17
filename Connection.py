import pandas as pd


def update(database, newPath):
    database.to_csv(newPath, index=False)


class Connection:

    def __init__(self, path):
        self.path = path
        self.db = pd.DataFrame(pd.read_excel(path))
