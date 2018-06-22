from django import template

register= template.Library()

def cut(value,arg):
    """
    this cuts all values of arg from the string
    """
    return value.replace(arg,'')

register.filter('cut',cut)
# C:\Users\dell pc\Desktop\My_Django_Stuff\IlearnDjango\learning_templates\basic_app\templatetags\my_extras.py
