'''
 Created by jenny at 11/23/19

Feature:

'''
COST = 10

class Cart:
    def __init__(self, title=None, time=None, seats=None):
        self._title = title
        self._time = time
        self._seats = seats

    def clear(self):
        '''
        clear variables to None
        :return:
        '''
        self._title = None
        self._time = None
        self._seats = None

    def set_title(self,title):
        if self._title is None:
            self._title = list()

        self._title.append(title)

    def set_time(self,time):
        if self._time is None:
            self._time = list()

        self._time.append(time)

    def set_seats(self,seats):
        if self._seats is None:
            self._seats = list()

        self._seats.append(seats)

    def get_title(self):
        return self._title

    def get_time(self):
        return self._time

    def get_each_quantity(self):
        '''
        get quantity of ticket of each movie
        :return:
        '''
        quantity_list = list()

        if self._title is None:
            return None

        for i in range(len(self._seats)):
            # append number of seats
            quantity_list.append(len(self._seats[i]))
        return quantity_list

    def get_quantity(self):
        '''
        get total quantity use picked
        :return:
        '''
        quantity = 0
        # total quantity user chose
        for i in range(len(self._seats)):
            quantity += len(self._seats[i])

        return quantity

    def get_total(self):
        '''
        get total with constant variable cost
        :return:
        '''
        return self.get_quantity()*COST

    def receipt(self):
        '''
        send data to the file
        :return:
        '''
        if self._title is not None:

            file_name = "receipt.txt"

            # save attributes into the text file
            outfile = open(file_name , "w")
            for i in range(len(self._title)):
                if len(self._seats[i]) > 0:
                    print(f"{self._title[i]:<20}  {self._time[i]}  X{len(self._seats[i])} = ${len(self._seats[i])*COST}",
                          file = outfile)
            print("*"*20,file = outfile)
            print("total: $ ",self.get_total(),file = outfile)
            outfile.close()

