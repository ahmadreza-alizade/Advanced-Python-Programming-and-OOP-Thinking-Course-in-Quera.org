
class Strint(int):

    def __init__(self, number):
        self.number = str(int(number))
        self.persian_digits = {
            '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
            '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'
        }

    def __lt__(self, other):
        num_str = str(self.number)
        yekan = int(num_str[-1])

        other_str = str(int(other.number))
        other_yekan = int(other_str[-1])

        return yekan < other_yekan

    def __gt__(self, other):
        num_str = str(self.number)
        yekan = int(num_str[-1])

        other_str = str(int(other.number))
        other_yekan = int(other_str[-1])

        return yekan > other_yekan

    def __le__(self, other):
        num_str = str(self.number)
        yekan = int(num_str[-1])

        other_str = str(int(other.number))
        other_yekan = int(other_str[-1])

        return yekan <= other_yekan

    def __ge__(self, other):
        num_str = str(self.number)
        yekan = int(num_str[-1])

        other_str = str(int(other.number))
        other_yekan = int(other_str[-1])

        return yekan >= other_yekan

    def __eq__(self, other):
        num_str = str(self.number)
        yekan = int(num_str[-1])

        other_str = str(int(other.number))
        other_yekan = int(other_str[-1])

        return yekan == other_yekan

    def __ne__(self, other):
        num_str = str(self.number)
        yekan = int(num_str[-1])

        other_str = str(int(other.number))
        other_yekan = int(other_str[-1])

        return yekan != other_yekan

    def __add__(self, other):
        other_str = str(int(other.number))
        return int(str(self.number) + other_str)

    def __sub__(self, other):
        self_str = str(self.number)
        other_str = str(other.number)
        if self_str.endswith(other_str):
            result_str = self_str[:-len(other_str)] 
            if result_str == '':
                return 0
            return int(result_str)
        else:
            raise Exception('The subtraction is not valid!')


    def __len__(self):
        return (len(self.number))

    def __call__(self):
        fa_num = [self.persian_digits[num] for num in list(self.number)]
        return ("".join(fa_num))
