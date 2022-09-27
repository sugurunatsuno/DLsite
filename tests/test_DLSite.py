from types import NoneType
from ..DLsite import Product, ProductArgmentException
import pytest

# テスト項目列挙

class TestManga():

    # 正常なURI
    def test_001(self):
        p = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ218142.html')
        assert p.status_code == 200

    # DLSiteではないURI
    def test_002(self):
        def _get_not_found_uri():
            p = Product('https://tweetdeck.twitter.com')
        
        with pytest.raises(ProductArgmentException) as e:
            _get_not_found_uri()
        
        assert str(e.value) == "DLSiteのドメインではありません"

    # 対象の作品が存在しない場合のURI
    def test_003(self):
        p = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ999999.html')
        assert p.status_code == 404

    # print文でタイトルなどが取得できる
    def test_004(self):
        p = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ218142.html')
        assert str(p) == "お兄ちゃんはおしまい!: ねことうふ(GRINP)"

    # 作品名が正しく取得できている
    def test_005(self):
        p = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ218142.html')
        assert p.title == "お兄ちゃんはおしまい!"

    # 販売日が正しく取得できている
    def test_006(self):
        p = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ218142.html')
        assert p.release_date == '2018年01月27日'

    # 更新情報が正しく取得できている
    def test_007(self):
        p = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ218142.html')
        assert p.last_updated == '2018年01月29日更新情報'

    # 最終更新日が正しく取得できている
    def test_008(self):
        p = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ218142.html')
        assert p.last_updated == '2018年01月29日更新情報'

    # 最終更新日が正しく取得できている(最終更新日が存在しない)
    def test_009(self):
        with pytest.raises(AttributeError) as e:
            p = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ398441.html')
            a = p.last_updated 
        assert str(e.value) == "'Product' object has no attribute 'last_updated'"

    # 作者が正しく取得できている
    def test_010(self):
        p = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ218142.html')
        assert p.author == ['ねことうふ']

    # 年齢指定が正しく取得できている
    def test_011(self):
        p = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ218142.html')
        assert p.rate == '全年齢'

    # 作品形式が正しく取得できている
    def test_012(self):
        p = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ218142.html')
        assert p.product_format == 'マンガ'

    # ファイル形式が正しく取得できている
    def test_013(self):
        p = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ218142.html')
        assert p.file_format == ['JPEG', 'PDF同梱']
    
    # イベントが正しく取得できている
    def test_014(self):
        p = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ398441.html')
        assert p.event == 'コミックマーケット99'

    # イベントが正しく取得できている(イベントが存在しない)
    def test_015(self):
        with pytest.raises(AttributeError) as e:
            p = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ218142.html')
            a = p.event 
        assert str(e.value) == "'Product' object has no attribute 'event'"

    # ジャンルが正しく取得できている
    def test_016(self):
        p = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ218142.html')
        assert p.genre == ['妹', '兄', 'コメディ', '日常/生活', '女体化', '性転換(TS)']

    # ファイル容量が正しく取得できている
    def test_017(self):
        p = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ218142.html')
        assert p.file_size == '64.93MB' 

    # シナリオが正しく取得できている
    # シナリオが正しく取得できている(シナリオが存在しない)
    # イラストが正しく取得できている
    # イラストが正しく取得できている(イラストが存在しない)

    # シリーズが正しく取得できている
    def test_022(self):
        p = Product('https://www.dlsite.com/maniax/work/=/product_id/RJ218142.html')
        assert p.series == 'お兄ちゃんはおしまい！' 
    
    # シリーズが正しく取得できている(シリーズが存在しない)
    # 声優が正しく取得できている
    # 声優が正しく取得できている(声優が存在しない)