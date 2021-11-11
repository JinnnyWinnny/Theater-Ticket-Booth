'''
 Created by jenny at 11/23/19

Feature: theater class

'''
import Movie


class Theater:
    def __init__(self,file_name):
        self._file_name = file_name
        # list of objects
        self._movies = self.movies_from_file(Movie.Movies)

    def movies_from_file(self, object):
        '''
        get data of the movie from text file : title,times,length,num of seat
        :param object:
        :return:
        '''
        # list of movies
        movies = list()
        # reading from the file
        infile = open(self._file_name, "r")
        # ignore the first line
        infile.readline()

        for i, line in enumerate(infile):
            # ignore \n
            curr_line = line.rstrip()
            # split by ,
            curr_line = curr_line.split(',')

            # split by / so that obtain show times
            times_split = curr_line[1].split('/')

            # get title, times, length
            title = curr_line[0]
            times = times_split
            length = int(curr_line[2])
            num_of_seat = int(curr_line[3])

            # create objects
            temp = object(title, times, length, num_of_seat)
            movies.append(temp)

        infile.close()
        return movies

    def get_num_of_movies(self):
        '''
        get number of movies from movie list
        :return:
        '''
        return len(self._movies)

    def get_titles(self):
        '''
        get a list of movies
        :return:
        '''
        movie_list = list()
        for movie in self._movies:
            movie_list.append(movie.get_title())

        return movie_list

    def get_length(self):
        '''
        get a length of movies
        :return:
        '''
        length_list = list()
        for movie in self._movies:
            length_list.append(movie.get_length())

        return length_list


    def get_movie_num_w_title(self):
        '''
        creat dictionary of number : titles
        :return:
        '''
        movie_num_title = dict()
        nums = self.get_num_of_movies()
        titles = self.get_titles()
        for i in range(nums):
            movie_num_title[i] = titles[i]
        return movie_num_title

    def get_show_times(self,selection):
        return self._movies[selection].get_show_times()

    def show_nst_time(self, selection, nst_show_time):
        return self._movies[selection].get_nst_time(nst_show_time)

    def get_col(self,title,time):
        return self._movies[title].get_col(time)

    def get_row(self,title,time):
        return self._movies[title].get_row(time)

    def check_seats(self,title,time,r,c):
        return self._movies[title].check_seats(time,r,c)

    def update_seat(self,selection,time,r,c):
        # error checking did he choose 0
        self._movies[selection].update_seats(time,r,c)

    def get_num_left_seat(self,selection,time):
        return self._movies[selection].get_num_of_left_seats(time)

    def get_title(self,title_selection):
        return self._movies[title_selection].get_title()

    def int_to_char(self,n):
        return chr(n+97)