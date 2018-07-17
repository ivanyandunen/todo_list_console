def choose_action():
    commands = ['list', 'new', 'exit']
    action = input('Input your command: (list|new|exit): ')
    while action not in commands:
        print('Please, choose a command from list')
        action = input('(list|new|exit): ')
    return action


def choose_item():
    items = {'0': 'ToDoItem', '1': 'ToBuyItem', '2': 'ToReadItem'}
    print('Select item type:\n0: ToDoItem\n1: ToBuyItem\n2: ToReadItem')
    selected = input('Input number: ')
    while selected not in items:
        print(
            'Please, choose a correct type:\n0: ToDoItem\n1: ToBuyItem\n2: ToReadItem'
            )
        selected = input('Input number: ')
    print('Selected: {}\n'.format(items[selected]))
    return selected


def add_new_item(list, item_type):
    if item_type == '0':
        new_item = input('Input heading: ')
        list.append('ToDo: ' + new_item)
        print('Added ToDo: {}'.format(new_item))
    elif item_type == '1':
        new_item = input('Input heading: ')
        price = input('Input price: ')
        list.append('ToBuy: ' + new_item + ' for ' +price)
        print('Added ToBuy: {} for {}'.format(new_item, price))
    elif item_type == '2':
        new_item = input('Input header: ')
        url = input('Input URL: ')
        list.append('ToRead: ' + new_item + ' here ' + url)
        print('Added ToRead {} here {}'.format(new_item, url))
    return list


def print_list(list):
    if not list:
        print('There are no items in storage.')
    else:
        for i in range(len(list)):
            print('{}: {}'.format(i, list[i]))


if __name__ == '__main__':
    list = []
    action = choose_action()
    while action != 'exit':
        if action == 'new':
            add_new_item(list, choose_item())
        elif action == 'list':
            print_list(list)
        action = choose_action()
