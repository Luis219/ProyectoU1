import unittest
from app import index, validar_usuarios_empresa
from flask import render_template, url_for

class validacion(unittest.TestCase):
     def test_validar_usuarios_empresa(self):
        b=validar_usuarios_empresa()
        self.assertEqual(b, url_for('index') )

if __name__=="__main__":
    unittest.main()