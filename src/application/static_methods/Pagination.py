
class Pagination:

    @staticmethod
    def paginateEnigmas(enigmas, maxPerPage):
        pagination = {}
        lastPage = (len(enigmas) / maxPerPage) + 1
        key = 1
        indexEnigmas = 0
        while key <= lastPage:
            tempArray = []
            i = 0
            while i < 5 and indexEnigmas < len(enigmas):
                tempArray.append(enigmas[indexEnigmas])
                indexEnigmas += 1
                i += 1
            pagination[key] = tempArray
            key += 1
        return pagination