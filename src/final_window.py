'''
 Created by jenny at 12/11/19

Feature:

'''
import Counter
import Theater
import Cart
import tkinter as tk
import tkinter.ttk as ttk   # for buttons
import copy

class App:

    def __init__(self,master):
        # creating classes in the beginning
        self._theater = Theater.Theater("movie.txt")
        self._counter = Counter.Counter("counter.txt", 0, 0)
        self._cart = Cart.Cart()

        # list of seat selected
        self._seat = list()

        # key: title - value: time
        self._movie_w_time_in_cart = dict()
        self._movies = self._theater.get_movie_num_w_title()
        self._movie_length = self._theater.get_length()


        ###### Create component #######
        self._frame1 = tk.Frame(root, relief="solid", bd=2)
        self._frame1.pack(side="left", fill="both", expand=True)

        self._frame2 = tk.Frame(root, relief="solid", bd=2)
        self._frame2.pack(side="right", fill="both", expand=True)
        self._image_list = list()

        # list of buttons of time
        self._time_btn_list = list()

        # screen label in the new window
        self._screen_lbl = ttk.Label()

        # 2 dimensional list in new window
        self._seat_buttons = []


        ########################CART##########################
        self._cart_label = ttk.Label(self._frame2, text="CART")
        self._cart_label.config(foreground="gray")
        self._cart_label.config(font=('Tahoma', 13, 'bold'))
        self._cart_label.place(x=screen_width / 6, y=0)

        self._cart_text = tk.Text(self._frame2, width=screen_width//30, height=screen_height//50)
        self._cart_text.config(font=('Consolas', 15))
        self._cart_text.config(bg="lightgray")
        self._cart_text.config(state='disabled')
        self._cart_text.place(x=screen_width / 30, y=30)

        self._total_lbl = tk.Label(self._frame2, text="Total: $ ")
        self._total_lbl.place(x=screen_width / 8, y=screen_height / 1.95)

        self._total_text = tk.Text(self._frame2, width=6, height=1)
        self._total_text.config(bg="lightgray")
        self._total_text.config(state='disabled')
        self._total_text.place(x=screen_width / 5, y=screen_height / 1.95)

        self._receipt_btn = tk.Button(self._frame2, text="RECEIPT")
        self._receipt_btn.config(foreground="gray")
        self._receipt_btn.config(font=('Tahoma', 10, 'bold'))
        self._receipt_btn.place(x=screen_width / 8, y=screen_height / 1.8)
        self._receipt_btn.config(command=self.make_receipt)

        self._no_receipt_btn = tk.Button(self._frame2, text="NO RECEIPT")
        self._no_receipt_btn.config(foreground="gray")
        self._no_receipt_btn.config(font=('Tahoma', 10, 'bold'))
        self._no_receipt_btn.place(x=screen_width / 4.5, y=screen_height / 1.8)
        self._no_receipt_btn.config(command= self.pass_to_counter)

        ########################COUNTER##########################
        self._counter_label = ttk.Label(self._frame2, text="COUNTER")
        self._counter_label.config(foreground="gray")
        self._counter_label.config(font=('Tahoma', 13, 'bold'))
        self._counter_label.place(x=screen_width / 6, y=screen_height / 1.6)

        self._counter_text = tk.Text(self._frame2, width=screen_width//30, height=screen_height//80)
        self._counter_text.config(font=('Consolas', 15))
        self._counter_text.config(bg="lightgray")
        self._counter_text.config(state='disabled')
        self._counter_text.place(x=screen_width / 30, y=screen_height / 1.5)

        self._cnt_total_lbl = tk.Label(self._frame2, text="Counter Total: $ ")
        self._cnt_total_lbl.place(x=screen_width / 60, y=screen_height / 1.05)

        self._cnt_total_text = tk.Text(self._frame2, width=8, height=1)
        self._cnt_total_text.config(bg="lightgray")
        self._cnt_total_text.config(state='disabled')
        self._cnt_total_text.place(x=screen_width / 7, y=screen_height / 1.05)

        self._save_btn = tk.Button(self._frame2, text="SAVE TO FILE")
        self._save_btn.config(foreground="gray")
        self._save_btn.config(font=('Tahoma', 10, 'bold'))
        self._save_btn.place(x=screen_width / 4, y=screen_height / 1.06)
        self._save_btn.config(command=self._counter.update)

        self.create_movie_components()

        num_of_bts = len(self._image_list)

        for n in range(num_of_bts):
            button = ttk.Button(self._frame1,image=self._image_list[n])
            button.grid(row=n, column=0)

        root.mainloop()

    def create_movie_components(self):
        '''
        create compnents in the movie section
        :return:
        '''
        # create each movie's function
        for n, title in self._movies.items():
            # creating 2d list
            self._time_btn_list.append([])

            ttl = title + ".png"
            self._image_list.append(tk.PhotoImage(file=ttl))

            # title
            title_length = title + " ("+str(self._movie_length[n])+"min)"
            title_lbl = ttk.Label(self._frame1, text=title_length, borderwidth=5, relief="flat")
            title_lbl.config(font=('Consolas', 15))
            title_lbl.place(x=screen_width / 4.5, y=(n + 0.10) * 150)

            time_w_seats_num = self._theater.get_show_times(n)
            nst = 0
            for time, num_seat in time_w_seats_num.items():
                btn_text = f"{time}({num_seat}left)"
                time_btns = ttk.Button(self._frame1, text=btn_text, command=lambda
                    nst=nst, n=n: self.new_window(n, self._theater.show_nst_time(n, nst), nst), width=15)
                self._time_btn_list[n].append(time_btns)
                time_btns.place(x=130 + (nst * 120), y=(n + 0.3) * 151)
                nst += 1

                # if number of left seat is 0
                if num_seat <= 0:
                    time_btns.config(state="disabled")

    def update(self, i, j, movie, time):
        '''
        change the color of the seat and
        update that the seat is occupied
        :param i: row
        :param j: column
        :param movie: selected movie
        :param time:  selected time
        :param button:  clicked button
        :return:
        '''

        # change the color of button clicked
        self._seat_buttons[i][j].config(bg="red")

        # check if the seat is empty
        if self._theater.check_seats(movie, time, i, j) == 0:
            # make it unable to click it
            self._theater.update_seat(movie, time, i, j)

            # store data of the seat
            self._seat.append([i, j])
            self._movie_w_time_in_cart.clear()
            selected_title = self._theater.get_title(movie)
            self._movie_w_time_in_cart[selected_title] = time

        elif self._theater.check_seats(movie, time, i, j) == 1:
            self._theater.update_seat(movie, time, i, j)
            self._seat_buttons[i][j].config(bg="white")
            if [i, j] in self._seat:
                self._seat.remove([i, j])





    def pass_to_counter(self):
        '''
        save data to the counter
        :return:
        '''

        # getting a titles and quantities from the cart
        title_list = self._cart.get_title()
        quantity_list = self._cart.get_each_quantity()

        # if nothing to save
        if title_list is None or quantity_list is None:
            return

        # add information to the counter
        for i, j in zip(title_list, quantity_list):
            self._counter.add(i, j)

        # write it into counter text section
        self._counter_text.config(state=tk.NORMAL)
        self._counter_text.delete('1.0', tk.END)
        for k, v in self._counter.get_movies().items():
            if v > 0:
                self._counter_text.insert(tk.INSERT, f"{k:<20} : {v}\n")
        self._counter_text.config(state='disabled')

        # write counter total to the text
        self._cnt_total_text.config(state=tk.NORMAL)
        self._cnt_total_text.delete('1.0', tk.END)
        self._cnt_total_text.insert(tk.INSERT, f"{self._counter.get_total()}")
        self._cnt_total_text.config(state='disabled')

        # clear the cart and class cart
        self.clear_cart_with_total()

    def clear_cart_with_total(self):
        '''
        clear text section when user clicked
        receipt or no receipt button
        '''
        self._cart.clear()
        self._cart_text.config(state=tk.NORMAL)
        self._cart_text.delete('1.0', tk.END)
        self._total_text.config(state=tk.NORMAL)
        self._total_text.delete('1.0', tk.END)

    def make_receipt(self):
        '''
        make a receipt and pass data to the counter
        '''
        self._cart.receipt()
        self.pass_to_counter()

    def pass_to_cart(self, new_window, clicked_movie, nst_time):
        '''
        show data to the cart text section

        :param new_window: new window
        :param clicked_movie: selected movie
        :param nst_time: order of the time clicked
        :return:
        '''

        # if at least one seat clicked
        if len(self._movie_w_time_in_cart) != 0:
            # get the first title in the dictionary
            title = list(self._movie_w_time_in_cart.keys())[0]
            # get the time which connected with the title
            time = self._movie_w_time_in_cart[title]

            self._cart_text.config(state=tk.NORMAL)

            num_of_tickets = len(self._seat)
            for i in range(num_of_tickets):
                # insert information about the movie selected to the cart
                self._cart_text.insert(tk.INSERT, f"{title}  {time} \n row: "
                                            f"{self._theater.int_to_char(self._seat[i][0]).upper()}, "
                                            f"col:{self._seat[i][1]}\n\n")
            self._cart_text.config(state="disabled")

            # store data into Cart class
            self._cart.set_time(time)
            self._cart.set_title(title)
            self._cart.set_seats(copy.deepcopy(self._seat))

            # show total on the window
            self._total_text.config(state=tk.NORMAL)
            self._total_text.delete('1.0', tk.END)
            self._total_text.insert(tk.INSERT, f"{self._cart.get_total()}")
            self._total_text.config(state="disabled")

            # update left seat on the button
            time_w_seats_num = self._theater.get_show_times(clicked_movie)
            clicked_time = list(time_w_seats_num.keys())[nst_time]

            # rewrite the text on the button
            self._time_btn_list[clicked_movie][nst_time].config(text=f"{clicked_time} ({time_w_seats_num[clicked_time]}left)")

            # if left seat is 0, make is unable to click it
            if time_w_seats_num[clicked_time] <= 0:
                self._time_btn_list[clicked_movie][nst_time].config(state="disabled")

            # clear the seat list to get a new seat
            self._seat.clear()

        new_window.destroy()



    def new_window(self, movie, time, nst_time):
        '''
        make a new window when user selected the movie
        and store data, update the seat, pass data to the cart

        :param movie: selected movie
        :param time: selected time
        :param nst_time: the order of time selected
        :return:
        '''
        new_root = tk.Tk()
        new_root.title("seat selector")
        new_root.resizable(False,False)
        # get a number of rows and columns
        row_n = self._theater.get_col(movie, time)
        col_n = self._theater.get_row(movie, time)

        # set a width and height of new window
        w = row_n * 35
        h = col_n * 45
        new_root.geometry(f"{w}x{h}")

        # show the place where screen at
        self._screen_lbl = ttk.Label(new_root, text="SCREEN", width=w)
        self._screen_lbl.configure(anchor="center")
        self._screen_lbl.pack()

        # 2 dimensional list
        self._seat_buttons = []
        for i in range(row_n):
            self._seat_buttons.append([])
            for j in range(col_n):

                # if the seat is available
                if self._theater.check_seats(movie, time, i, j) == 0:
                    seat_btn = tk.Button(new_root, width=3)

                # if the seat is occupied
                elif self._theater.check_seats(movie, time, i, j) == 1:
                    seat_btn = tk.Button(new_root, width=3, text="x")
                    seat_btn.config(state="disabled")

                self._seat_buttons[i].append(seat_btn)
                self._seat_buttons[i][j].config(bg="white")
                # when button clicked, call update function
                self._seat_buttons[i][j].config(command=lambda i=i, j=j: self.update(i, j, movie, time))
                self._seat_buttons[i][j].place(x=(j + 0.5) * 30, y=((i + 1) * 30))

        # when close button clicked, call the function pass_to_cart
        close_button = ttk.Button(new_root, text="DONE", command=lambda: self.pass_to_cart(new_root, movie, nst_time))
        close_button.place(x=w / 3.5, y=h - 30)

        new_root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    screen_width = 1000
    screen_height = 780

    root.title("Jenny's Theater")
    root.geometry(f"{screen_width}x{screen_height}")
    root.resizable(False, False)

    app = App(root)

    root.mainloop()
