import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_ifEitherPriceIs0:
    self.assertEqual(getRatio(0, 1), 0) 
    self.assertEqual(getRatio(1, 0), None)
    self.assertEqual(getRatio(0, 0), None)

  def test_getRatio_priceAZero(self):
    price_a = 0
    price_b = 223.42
    self.assertEqual(getRatio(price_a, price_b), 0)

  def test_getRatio_samePrice(self):
     price_a = 223.42
     price_b = 223.42
     self.assertEqual(getRatio(price_a, price_b), 1)

  def test_getRatio_aGreater(self):
     price_a = 223.42
     price_b = 109.32
     self.assertGreater(getRatio(price_a, price_b), 1)
 
   def test_getRatio_bGreater(self):
     price_a = 109.32
     price_b = 223.42
     self.assertLess(getRatio(price_a, price_b), 1)

if __name__ == '__main__':
    unittest.main()
