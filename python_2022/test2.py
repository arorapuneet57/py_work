# Design an efficient algorithm for removing all first-name duplicates from an array
# Input [('Ian', 'Botham'),('David', 'Gower'),('Ian', 'Bell'),('Ian', 'Chappell')]
# output 1 (Ian, Bell), (David, Gower));
#or
# output 2 ((David, Gower), (Ian, Botham))

#('Ian', 'Bell'),('Ian', 'Chappell')

class Sample(object):
    def __init__(self):
        self.test = [('David', 'xx'),
                     ('Ian', 'Botham'),
                     ('David', 'Gower'),
                     ('David', 'pp'),
                     ('Ian', 'Bell'),
                     ('Ian', 'Chappell')]
    def remove_first_name(self):
        test = self.test
        test.sort()
        count = 0
        final_test = test
        for name in test:
            for found in test[1:]:
                if name[0] == found[0]:
                    final_test.remove(found)
                    break
                else:
                    continue
        return final_test

obj = Sample()
print(obj.remove_first_name())