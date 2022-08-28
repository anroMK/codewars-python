class List(object):
    def count_spec_digits(self, integers_list, digits_list):
        integers_string = ''.join([str(abs(i)) for i in integers_list])
        return [(i,integers_string.count(str(i))) for i in digits_list]

l = List()


print(l.count_spec_digits([-18, -31, 81, -19, 111, -888],[1, 8, 4]))





