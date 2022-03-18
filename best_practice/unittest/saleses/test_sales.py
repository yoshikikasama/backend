import pytest
from sales import Sale, Sales

# class TestLoadSales:
#     def test_invalid_row(self, tmpdir):
#         test_file = tmpdir.join('test.csv')
#         test_file.write("""id,item_id,price
#         1,1,100
#         2,1,100
#         """)
        
#         sum_price, actual_sales = load_sales(test_file.strpath)
#         assert sum_price == 0
#         assert len(actual_sales) == 0

#     def test_invalid_type_amount(self, tmpdir):
#         # テストのたびにCSVファイルを毎度用意する必要がある。
#         test_file = tmpdir.join('test.csv')
#         test_file.write("""id,item_id,price,amount
#         1,1,100,foobar
#         2,1,100,2
#         """)
#         sum_price, actual_sales = load_sales(test_file.strpath)
#         assert sum_price == 400
#         assert len(actual_sales) == 1


class TestSale:
    def test_validate_invalid_price(self):
        # 値の確認をするテストでCSVを用意する必要がなくなった
        sale = Sale(1, 1, 2, 0)
        with pytest.raises(ValueError):
            sale.validate()

    def test_validate_invalid_amount(self):
        sale = Sale(1, 1, 0, 1000)
        with pytest.raises(ValueError):
            sale.validate()
    

class TestSales:
    def test_from_assert_invalid_row(self):
        sales = Sales([])
        sales = sales.from_assert()
        print(sales)

    def test_validate_price(self):
        sale1 = Sale(1, 1, 2, 1)
        sale2 = Sale(1, 1, 2, 10)
        sales = Sales([sale1, sale2])
        assert sales.price == 11
