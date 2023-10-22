q = [
    {'id': 1, 'full_name': 'Алекберов Рамиль Русланович'},
    {'id': 2, 'full_name': 'Бобровская Анастасия Дмитриевна'},
    {'id': 3, 'full_name': 'Винговатов Але Олегович'}
    ]
w = [q['full_name'] for q in q if len(q['full_name'].split()[1]) > 6]
print(w)