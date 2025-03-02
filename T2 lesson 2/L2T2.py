from string import ascii_lowercase, digits

class TextInput:
    @classmethod
    def __init__(self, name, size = 10):
        self.name = name
        self.size = size
        self.check_name = name

    def get_html(self):
        return f"<p class = 'login'> {self.name} : <input type = 'text' size = {self.size} />"

    @classmethod
    def check_name(cls, name):
        CHARS = "йцукенгшщзхъёфывапролджэячсмитьбю " + ascii_lowercase
        CHARS_CORRECT = set(CHARS + CHARS.upper() + digits)
        if cls.size > 50 or cls.size < 3:
            raise ValueError("некорректное поле name")
        if not(set(name).issubset(CHARS_CORRECT)):
            raise ValueError("некорректное поле name")

class PasswordInput:
    @classmethod
    def __init__(self, name, size = 10):
        self.name = name
        self.size = size
        self.check_name(name)

    def get_html(self):
        return f"<p class = 'password'> {self.name} : <input type = 'text' size ] {self.size} />"
    
    @classmethod
    def check_name(cls, name):
        CHARS = "ёйцукенгшщзхъфывапролджэячсмитьбю " + ascii_lowercase
        CHARS_CORRECT = set(CHARS + CHARS.upper() + digits)
        if cls.size > 50 or cls.size < 3:
            raise ValueError("некорректное поле name")
        if not(set(name).issubset(CHARS_CORRECT)):
            raise ValueError("некорректное поле name")
        
class Formlogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw
    
    def render_template(self):
        return "\n".join(['<form action = "#" >', self.login.get_html(), self.password.get_html(), '</form>'])

login = Formlogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
print(html)