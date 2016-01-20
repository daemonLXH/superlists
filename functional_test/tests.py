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


        #她按回车键后,被带到了一个新的url

        #待办事项表格中显示了"1:Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url,'/lists/.+')
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

        #现在另一个新用户访问了网站

        ##我们使用一个新浏览器会话

        self.browser.quit()
        self.browser = webdriver.Firefox()

        #他访问首页
        #页面中看不到伊迪丝的清单
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertNotIn('make a fly',page_text)


        #他输入一个新待办事项,新建一个清单
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        #他获取了他的唯一URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url,'/lists/.+')
        self.assertNotEqual(francis_list_url,edith_list_url)

        #这个页面还是没有伊迪丝的清单
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',page_text)
        self.assertIn('Buy milk',page_text)


        #伊丽丝想知道这个网站是否会记住她的清单

        #她看到网站为她生成了一个唯一的URL

        #而且页面中有一些文字解说这个功能

        #她访问那个URL,发现她的待办事项列表还在

        #她很满意,去睡觉了

        # self.fail('Finish the test!')

# if __name__ == '__main__':
#     unittest.main(warnings='ignore')
    def test_layout_and_styling(self):
        #伊迪丝访问首页
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024,768)

        #她看到输入框完美的居中显示
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(inputbox.location['x'] + inputbox.size['width']/2,
                               512,
                               delta=5
                               )

        #她新建了一个清单,看到输入框仍完美地居中显示
        inputbox.send_keys('testing\n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )
