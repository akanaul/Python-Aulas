"""
Instruções de como rodar: python -m unittest discover testes

Testes unitários para o Mini-Projeto 1.5 - Sistema de Cadastro de Motoristas.
"""
import unittest

# Simulando as classes do módulo principal
class Vehicle:
    def __init__(self, plate, model):
        self.plate = plate
        self.model = model
        
    def to_dict(self):
        return {'plate': self.plate, 'model': self.model}

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Driver(Person):
    def __init__(self, name, age, license_number, vehicle=None):
        super().__init__(name, age)
        self.license_number = license_number
        self.vehicle = vehicle

    def to_dict(self):
        data = {
            'name': self.name,
            'age': self.age,
            'license_number': self.license_number,
            'vehicle': self.vehicle.to_dict() if self.vehicle else None
        }
        return data

    @classmethod
    def from_dict(cls, data):
        vehicle = Vehicle(**data['vehicle']) if data.get('vehicle') else None
        return cls(name=data['name'], age=data['age'], license_number=data['license_number'], vehicle=vehicle)


class TestSistemaMotoristas(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(plate="ABC-1234", model="Caminhão Baú")
        self.driver = Driver(name="Carlos", age=45, license_number="987654321", vehicle=self.vehicle)
        self.driver_dict = {
            'name': 'Carlos',
            'age': 45,
            'license_number': '987654321',
            'vehicle': {'plate': 'ABC-1234', 'model': 'Caminhão Baú'}
        }

    def test_instantiation(self):
        """Testa se as instâncias são criadas corretamente."""
        self.assertEqual(self.driver.name, "Carlos")
        self.assertEqual(self.driver.vehicle.plate, "ABC-1234")

    def test_to_dict(self):
        """Testa a conversão do objeto para dicionário."""
        self.assertEqual(self.driver.to_dict(), self.driver_dict)

    def test_from_dict(self):
        """Testa a criação do objeto a partir de um dicionário."""
        new_driver = Driver.from_dict(self.driver_dict)
        self.assertEqual(new_driver.name, "Carlos")
        self.assertEqual(new_driver.vehicle.plate, "ABC-1234")

if __name__ == '__main__':
    unittest.main()
