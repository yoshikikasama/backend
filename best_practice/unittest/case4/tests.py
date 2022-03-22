"""
test用のデータはtest終了後に削除する
"""

class TestImportCSV:

    def setup_method(self, method):
        import tempfile

        self.test_fp = tempfile.NamedTemporaryFile(mode="W", encoding="utf-8")
        self.test_csv = self.test_fp.name
        self.test_fp.writelines([
            "Spam,Ham,Eggg¥n",
            "Spam,Ham,Eggg¥n",
            "Spam,Ham,Eggg¥n",
            "Spam,Ham,Eggg¥n",
        ])
        self.test_fp.seek(0)
    
    def teardown_method(self, method):
        # クローズすると自動削除される
        self.test_fp.close()
    
    def test_import(self):
        from spam.hoge import import_csv
        import_csv(self.test_csv)