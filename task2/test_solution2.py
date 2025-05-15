import unittest
from unittest.mock import patch, MagicMock
from collections import defaultdict
import os
from solution import get_animals_count, write_to_csv

class TestAnimalCounter(unittest.TestCase):

    def setUp(self):
        self.html = '''
        <div class="mw-category-group">
            <h3>А</h3>
            <ul>
                <li>Архар</li>
                <li>Антилопа</li>
            </ul>
        </div>
        <div class="mw-category-group">
            <h3>Б</h3>
            <ul>
                <li>Бобр</li>
            </ul>
        </div>
        <a href="/wiki/Категория:Животные_по_алфавиту?pagefrom=Г" title="Следующая страница">Следующая страница</a>
        '''

        self.html_last_page = '''
        <div class="mw-category-group">
            <h3>В</h3>
            <ul>
                <li>Волк</li>
            </ul>
        </div>
        <!-- Нет ссылки Следующая страница -->
        '''

    @patch('requests.get')
    def test_get_animals_count(self, mock_get):
        mock_get.side_effect = [
            MagicMock(status_code=200, text=self.html),
            MagicMock(status_code=200, text=self.html_last_page),
        ]

        counts = get_animals_count()
        self.assertEqual(counts['А'], 2)
        self.assertEqual(counts['Б'], 1)
        self.assertEqual(counts['В'], 1)
        self.assertNotIn('Г', counts)

    def test_write_to_csv(self):
        counts = defaultdict(int, {'А': 5, 'Б': 2})
        filename = 'beasts.csv'
        write_to_csv(counts)

        self.assertTrue(os.path.exists(filename))
        with open(filename, encoding='utf-8') as f:
            lines = f.read().strip().split('\n')
        self.assertEqual(lines[0], 'А,5')
        self.assertEqual(lines[1], 'Б,2')
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()
