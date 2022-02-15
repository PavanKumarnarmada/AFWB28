from AFWB28.generic.base_test import BaseTest


class Test_Demo1(BaseTest):

    def test_demo1(self):
         print(self.driver.title)
         v=excel.get_data(self.xl_path,"sheet1",1,1)
         print("from excel:",v)