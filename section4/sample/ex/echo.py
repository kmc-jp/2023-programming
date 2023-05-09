while True:
    input_data = input('何か入力してください．:qを入力すると終了します．> ')
    if input_data == ':q':
        break
    print(input_data * 2)