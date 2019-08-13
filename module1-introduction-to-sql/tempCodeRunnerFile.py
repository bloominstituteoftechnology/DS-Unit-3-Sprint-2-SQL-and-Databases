    rows_result = [x[0] for x in rows2]
    labels = ['mages','clerics','necromancers','thiefs','fighters']
    for label, row in zip(labels, rows_result):
        print(f'Total number of {label}: {row}')