import datetime
data = {
            "id": [1, 1, 2, 2, 2, 3],
            "value": ["1", "1", "2", "2", "-1", "3"],
            "effective_start": [
                datetime.date(2020, 1, 1),
                datetime.date(2020, 2, 2),
                datetime.date(2020, 1, 1),
                datetime.date(2020, 2, 2),
                datetime.date(2020, 2, 3),
                datetime.date(2020, 1, 1),
            ],
            "effective_end": [
                datetime.date(2020, 2, 2),
                datetime.date(2020, 2, 3),
                datetime.date(2020, 2, 2),
                datetime.date(2020, 2, 3),
                datetime.date(2020, 2, 4),
                datetime.date(2020, 2, 2),
            ],
        }
