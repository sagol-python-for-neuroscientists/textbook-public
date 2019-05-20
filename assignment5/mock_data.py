import pathlib
import json

import pandas as pd
import numpy as np
import mimesis
from mimesis.schema import Field, Schema
from mimesis.enums import Gender


def make_data(iterations=100):
    _ = Field('en')
    description = (
        lambda: {
            'id': _('numbers.between', minimum=100000000, maximum=999999999),
            'first_name': _('person.name'),
            'last_name': _('person.last_name'),
            'email': _('person.email', key=str.lower),
            'timestamp': _('timestamp', posix=False),
            'age': _('person.age'),
            'gender': _('person.gender'),
            'q1': _('numbers.rating', maximum=10.0),
            'q2': _('numbers.rating', maximum=10.0),
            'q3': _('numbers.rating', maximum=10.0),
            'q4': _('numbers.rating', maximum=10.0),
            'q5': _('numbers.rating', maximum=10.0),
        }
    )
    schema = Schema(schema=description)
    return schema.create(iterations=iterations)


def ruin_data(data):
    email_rows = np.random.randint(low=0, high=100, size=(15,))
    for row in email_rows:
        email = data[row]['email']
        new_email = email[:2] + email[4:7] + email[9:11] + email[18:-2]
        data[row]['email'] = new_email

    age_rows = np.random.randint(low=0, high=100, size=(31,))
    for row in age_rows:
        data[row]['age'] = "nan"

    field_rows = np.random.randint(low=0, high=100, size=(23,))
    whichq = np.random.randint(low=1, high=6, size=(23,))
    for row, q in zip(field_rows, whichq):
        data[row][f"q{q}"] = "nan"

    return data


def dump_data(fname, data):
    with open(fname, 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    length = 100
    data = make_data(length)
    fname = pathlib.Path('assignment5/data.json')
    data = ruin_data(data)
    dump_data(fname, data)
    d = pd.read_json(fname)
    print(d)