from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase


import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        # self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):

        #伊丽丝听说有一个在线待办事项应用
        #她去看了这个应用的首页

        # self.browser.get('http://localhost:8000')
        self.browser.get(self.live_server_url)

        #她注意到网页的标题和头部都包含了"To-Do"这个词

        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        # self.fail('Finish the test!')

        #应用邀请她输入一个待办事项

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )


        #她在一个文本框中输入了"Buy peacock feethers"
        inputbox.send_keys('Buy peacock feathers')


        #她按回车键后,页面更新了

        #待办事项表格中显示了"1:Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1:Buy peacock feathers')

        # import time
        # time.sleep(10)


        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        #     any(row.text == '1:Buy peacock feathers' for row in rows),'没有找到任何可显示的条目'
        #     '--its text was:\n%s' % (table.text,)
        # )
        # self.assertIn('1:Buy peacock feathers',[row.text for row in rows])

        #页面中又显示了一个文本框,可以输入其它的待办事项
        #她输入了"Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(u'Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)


        #页面再次更新,她的清单中显示了这两个待办事项

        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn('1:Buy peacock feathers',[row.text for row in rows])
        # self.assertIn(
        #     '2:Use peacock feathers to make a fly',
        #     [row.text for row in rows]
        # )
        self.check_for_row_in_list_table('1:Buy peacock feathers')
        self.check_for_row_in_list_table('2:Use peacock feathers to make a fly')


        #伊丽丝想知道这个网站是否会记住她的清单

        #她看到网站为她生成了一个唯一的URL

        #而且页面中有一些文字解说这个功能

        #她访问那个URL,发现她的待办事项列表还在

        #她很满意,去睡觉了

        self.fail('Finish the test!')

# if __name__ == '__main__':
#     unittest.main(warnings='ignore')