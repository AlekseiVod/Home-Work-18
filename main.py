# Правильный вызов
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()


test_function()


# Вызов функции inner_function вне функции test_function
def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()


inner_function()
test_function()
