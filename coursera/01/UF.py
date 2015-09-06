__author__ = 'Sergey'


class UF:
    def __init__(self, number):
        self.id = list(range(number))

    def union(self, p, q):
        qid = self.id[q]
        pid = self.id[p]
        for i in range(len(self.id)):
            if self.id[i] == pid:
                self.id[i] = qid

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def print(self):
        print(self.id)

