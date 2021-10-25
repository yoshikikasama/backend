import os
import pytest
import calculation

is_release = False

class TestCalc():
    # class全体が実行される前に呼ばれる
    @classmethod
    def setup_class(cls):
        print('start')
        cls.cal = calculation.Calc()
        cls.test_file_name = 'test.txt'
    @classmethod
    def teardown_class(cls):
        print('end')
        del cls.cal
    # 関数test前に呼ばれる関数
    def setup_method(self, method):
        print(f'method={method.__name__}')
        # self.cal = calculation.Calc()
    # test後に呼ばれる関数
    def teardown_method(self, method):
        print(f'method={method.__name__}')
        # del self.cal
    # @pytest.mark.skip(reason='skip!')
    @pytest.mark.skipif(is_release==True, reason='skip!')
    def test_add_num_and_double(self, request, csv_file):
        print(csv_file)
        os_name = request.config.getoption('--os-name')
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        assert self.cal.add_num_and_double(1, 1) == 4
    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double('1', '1')
