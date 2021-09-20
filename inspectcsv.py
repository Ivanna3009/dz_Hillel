import csv

from collections import defaultdict
from math import ceil

'''
def int_field(data):
    for i in data:
        int(i)
    return 'Int_Field()'


def float_field(data):
    for i in data:
        float(i)
    return 'Float_Field()'
'''

def name_field(type_f, field):
    def _inner(data):
        for i in data:
            type_f(val)
        return field
    return _inner


def char_field(data):
    max_length = ceil(max(map(len, data)) * 1.25 / 10) * 10
    return f'CharField(max_length={max_length})'


def gen_field(name, data):
    validators = [
        name_field(int, 'IntField()'),
        name_field(float, 'FloatField()'),
        char_field,
    ]
    for i in validators:
        try:
            field = i(data)
            break
        except:
            pass

    print(f'{name} = model.{field}')


def gen_model(fname, col_data):
    print(f'class {fname}(model.Model):')
    for k, i in col_data.items():
        gen_field(k, i)


def process_file(fname):
    with open(fname) as csvfile:
        reader = csv.DictReader(csvfile)
        col_data = defaultdict(set)
        for row in reader:
            for k, i in row.items():
                col_data[k].add(i)
        return col_data


if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    print(args)
    if args:
        gen_model(args[0], process_file(args[0]))
    else:
        print('....')
