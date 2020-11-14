import pickle


def add_user(id):
    user_id = set()
    with open('user_base.pickle', 'rb') as f:
        user_id.add(pickle.load(f))
        print(user_id)
        if id not in user_id:
            print(f'Пользователя {id} нет в базе.')
            user_id.add(id)
            with open('user_base.pickle', 'ab') as f:
                pickle.dump(user_id, f)
                print(f'Пользователь {id} добавлен в базу.')
        else:
            print(f'Пользователь {id} уже давно в базе.')