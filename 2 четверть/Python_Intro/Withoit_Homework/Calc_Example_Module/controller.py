import mult
import view

def button_click():
    value_a = view.get_value()#получаем данные двух чисел
    value_b = view.get_value()
    #module.init(value_a, value_b)
    #result = module.sum()
    mult.init(value_a, value_b)
    result = mult.mult()
    view.view_data(result)
