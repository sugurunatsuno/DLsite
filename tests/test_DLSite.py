from ..DLsite import Product, ProductArgmentException, ProductNotFoundException
import pytest

# テスト項目列挙

# 正常なURI
def test_001():
    p = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ218142.html')
    assert p.status_code == 200

# DLSiteではないURI
def _get_not_found_uri():
    p = Product('https://tweetdeck.twitter.com')

def test_002():
    with pytest.raises(ProductNotFoundException):
        _get_not_found_uri()

# 対象の作品が存在しない場合のURI
def test_003():
    p = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ999999.html')
    assert p.status_code == 404

# print文でタイトルなどが取得できる
# 作品名が正しく取得できている
# 販売日が正しく取得できている
# 最終更新日が正しく取得できている
# 最終更新日が正しく取得できている(最終更新日が存在しない)
# 作者が正しく取得できている
# 年齢指定が正しく取得できている
# 作品形式が正しく取得できている
# ファイル形式が正しく取得できている
# イベントが正しく取得できている
# イベントが正しく取得できている(イベントが存在しない)
# ジャンルが正しく取得できている
# ファイル容量が正しく取得できている
# シナリオが正しく取得できている
# シナリオが正しく取得できている(シナリオが存在しない)
# イラストが正しく取得できている
# イラストが正しく取得できている(イラストが存在しない)
# シリーズが正しく取得できている
# シリーズが正しく取得できている(シリーズが存在しない)
# 声優が正しく取得できている
# 声優が正しく取得できている(声優が存在しない)