"""
Нужно изолировать тест от реального интернета, иначе тесты будут нестабильными и замедлятся.
"""

import unittest
from unittest.mock import patch, Mock
from collections import defaultdict
from task_2 import get_counts, save_to_csv

# Пример фрагмента HTML из Википедии
MOCK_HTML = """
<div id="mw-pages">
  <div class="mw-category-group">
    <ul>
      <li><a href="/wiki/Акула" title="Акула">Акула</a></li>
      <li><a href="/wiki/Бобр" title="Бобр">Бобр</a></li>
    </ul>
  </div>
  <a href="/wiki/Следующая_страница">Следующая страница</a>
</div>
"""

MOCK_HTML_LAST = """
<div id="mw-pages">
  <div class="mw-category-group">
    <ul>
      <li><a href="/wiki/Волк" title="Волк">Волк</a></li>
    </ul>
  </div>
</div>
"""

class TestBeastsScraper(unittest.TestCase):

    @patch('task_2.requests.get')
    def test_get_counts(self, mock_get):
        # Настраиваем поведение mock: две страницы — первая и последняя
        mock_get.side_effect = [
            Mock(status_code=200, content=MOCK_HTML.encode('utf-8')),
            Mock(status_code=200, content=MOCK_HTML_LAST.encode('utf-8')),
        ]

        result = get_counts()
        expected = defaultdict(int, {'А': 1, 'Б': 1, 'В': 1})
        self.assertEqual(dict(result), dict(expected))

    def test_save_to_csv(self):
        counts = {'А': 3, 'Б': 2}
        import os
        test_filename = 'test_beasts.csv'
        save_to_csv(counts, test_filename)

        with open(test_filename, 'r', encoding='utf-8') as f:
            content = f.read()
        os.remove(test_filename)

        self.assertIn('А,3', content)
        self.assertIn('Б,2', content)


if __name__ == '__main__':
    unittest.main()
