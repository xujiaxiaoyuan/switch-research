import pyautogui
import webbrowser

# 设置搜索引擎的URL
search_engines = {
    'baidu': 'https://www.baidu.com/s?wd=',
    'google': 'https://www.google.com/search?q='
}

# 当前搜索引擎
current_engine = 'baidu'

def switch_search_engine():
    global current_engine
    if current_engine == 'baidu':
        current_engine = 'google'
        print('切换至谷歌搜索')
    else:
        current_engine = 'baidu'
        print('切换至百度搜索')

# 注册鼠标点击事件处理函数
def on_mouse_click(x, y, button, pressed):
    if button == pyautogui.MouseButton.left and pressed:
        switch_search_engine()
        search_keyword = input('请输入搜索关键词：')
        # 打开新的浏览器窗口进行搜索
        webbrowser.open(search_engines[current_engine] + search_keyword)

# 监听鼠标点击事件
pyautogui.listen(on_click=on_mouse_click)