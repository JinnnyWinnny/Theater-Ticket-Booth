'''
 Created by jenny at 11/23/19

Feature: Movie class

'''
import copy
import math

class Movies:
    def __init__(self, title, times, length=None,num_of_seat=None):
        self._title = title
        # times - list
        self._time_seats = dict()
        self._length = length
        self._num_of_seats = num_of_seat
        rows, cols = (math.sqrt(self._num_of_seats),math.sqrt(self._num_of_seats))
        _seats = list()

        # just create three 2d lists and store it seperately
        # make a function that creates a list and call it
        for i in range(int(rows)):
            row = [0] * int(cols)
            _seats.append(row)

        for i in times:
            # to prevent the list shares the same address
            self._time_seats[i] = copy.deepcopy(_seats)

    def get_num_of_showtimes(self):
        '''
        counting the number of show times specific movie has
        :return:
        '''
        count = 0
        for i in self._time_seats.keys():
            count += 1
        return count

    def get_nst_time(self,n):
        '''
        return time related to the number n
        :param n:
        :return: time
        '''
        for i,k in enumerate(self._time_seats.keys()):
            if n == i:
                return k

    def get_show_times(self):
        '''
        create dictionary time : seats
        :return: times_seats
        '''
        times_seats = dict()
        for i, k in enumerate(self._time_seats.keys()):
            times_seats[k] = self.get_num_of_left_seats(k)
        return times_seats


    def int_to_char(self,n):
        '''
        convert int to character
        :param n:
        :return: char
        '''
        return chr(n+97)

    def char_to_int(self,char):
        '''
        conver character to int
        :param char:
        :return: int
        '''
        return ord(char)-97

    def get_col(self,time):
        '''
        get total column number
        :param time:
        :return:
        '''
        return len(self._time_seats[time][0])

    def get_row(self,time):
        '''
        get total row number
        :param time:
        :return:
        '''
        return len(self._time_seats[time])

    def show_seats(self, time):
        '''
        print seats
        :param time:
        '''
        # getting a number of columns of the seat
        col = self.get_col(time)
        # print columns numbers
        for c in range(col):
            print(f"{c+1:>4}",end = '')
        print()

        for i,k in enumerate(self._time_seats[time]):
            # convert number to the alphabet as rows
            print(f"{self.int_to_char(i)}  {k}")

    def get_title(self):
        '''
        getter: title
        :return: title
        '''
        return self._title

    def get_length(self):
        return self._length

    def update_seats(self,time,r,c):
        '''
        update the seat selected
        :param time:
        :param r: row
        :param c: column
        '''
        seat = self._time_seats[time]
        if seat[r][c] == 0:
            seat[r][c] = 1
        else:
            seat[r][c] = 0

    def check_seats(self,time,r,c):
        '''
        check its occupied or not
        :param time:
        :param r: row
        :param c: column
        :return:
        '''
        seat = self._time_seats[time]
        return seat[r][c]

    def get_num_of_left_seats(self, time):
        '''
        get number of remaining seats
        :param time:
        :return:
        '''
        # count num of 0 in the list
        # 0 - empty 1 - occupied
        count = 0
        for i in self._time_seats[time]:
            for j in i:
                if j == 0:
                    count += 1

        return count
