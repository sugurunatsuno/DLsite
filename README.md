DLsite
======

A python package that get information of products in DLsite.

Installing
----------
~~pip install dlsite~~

Example
-------
```python
from DLsite import Product

# set url
product = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ252835.html')
 
# get each info
print(product)
# output: 夢ノ濡色: じょぶじゅん。(じゃじゅじょ)
print(product.genre)
# output: ['ヘタレ攻め', 'ネコミミ']
```

License
-------

Refer to the LICENSE file.