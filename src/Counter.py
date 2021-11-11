'''
 Created by jenny at 11/23/19

Feature: counter class

'''
COST = 10
class Counter:
    def __init__(self, file_name, total, tickets_sold):
        self._file_name = file_name
        self._total = total
        self._tickets_sold = tickets_sold
        # title - num of total sold
        self._movies = dict()

    def add(self,title,tickets_sold):
        '''
        create _movies : append values
        :param title: movie's title
        :param tickets_sold: num of tickets sold
        :return:
        '''

        if title in self._movies:
            self._movies[title] += tickets_sold

        else:
            self._movies[title] = tickets_sold

        # calculate total money earned
        self._total += tickets_sold * COST

    def get_movies(self):
        return self._movies

    def get_total(self):
        return self._total

    def update(self):
        '''
        write out datas into file
        :return:
        :return:
        '''
        outfile = open(self._file_name , "w")
        print("-"*20, file = outfile)
        for key, value in self._movies.items():
            print(f"{key} : {value}\n", file=outfile)

        print("-"*20, file = outfile)
        print(f"total money earned: ${self._total}", file=outfile)
        outfile.close()
