CASOS_LOGIN = [
    ("standard_user", "secret_sauce", True), # usuario y contraseña válidos, login exitoso.
    ("locked_out_user", "secret_sauce", False), # usuario bloqueado, login falla.
    ("usuario_malo", "password_incorrecta", False), # usuario y contraseña inválidos, login falla.
]