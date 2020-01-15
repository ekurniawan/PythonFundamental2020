class Flight:

    def __init__(self,firstname):
        self.firstname = firstname

    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname

    def GetFullName(self):
        return self.firstname + " " + self.lastname

    def Add(bil1,bil2):
        return bil1+bil2


class Flight:
    def __init__(self,number):
        if not number[:2].isalpha():
            raise ValueError("No airline code {}".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code {}".format(number))
        if not number[2:].isdigit():
            raise ValueError("Invalid route number {}".format(number))
        self._number = number

    def number(self):
        return self._number
    
    def airline(self):
        return self._number[:2]

class Aircraft:
    def __init__(self,registration,model,num_rows,num_seats_per_row):
        self._registration=registration
        self._model=model
        self._num_row=num_rows
        self._num_seats_per_row
    
    def registration(self):
        return self._registration

    def model(self):
        return self._model


try:
    f=Flight("IW123")
    print(f.number())
    print(f.airline())    
except ValueError as e:
    print("Kesalahan {0}".format(e))



        



