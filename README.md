# ocr-translate
这是一个利用百度ocr接口实现的截图识别并翻译的脚本。

工作流程：截图->百度ocr识别->GoldenDict软件翻译。

后续如果有时间我会封装一个有UI界面的截图ocr识别翻译软件。

Windows上已经有这种软件：[https://github.com/AnyListen/tianruoocr](https://github.com/AnyListen/tianruoocr)

苦于自己在Linux上开发，没有好用的。

### 使用方法

1. 必备环境

   Python3，baidu-aip包(pip3 install baidu-aip )，当然你还要联网。

2. 安装截图软件

   这个选择很多，Linux下推荐[https://github.com/lupoDharkael/flameshot](https://github.com/lupoDharkael/flameshot)

3. 去百度智能云中申请一个文字识别接口，之后会得到创建的三个连接密钥：AppID、API Key、Secret Key，并填到baiduocr.py文件中

   [https://ai.baidu.com/tech/ocr/general](https://ai.baidu.com/tech/ocr/general)

4. 安装**GoldenDict**词典翻译软件

   [https://github.com/goldendict/goldendict](https://github.com/goldendict/goldendict)

   向其添加谷歌整句翻译程序[https://blog.csdn.net/clksjx/article/details/86775819](https://blog.csdn.net/clksjx/article/details/86775819)

   这个软件很强大，本身是一个划词翻译的软件，可配置性很强。

5. 修改文件夹配置

   创建一个用来存储你截图图片的文件夹，并配置ocr_tasns.sh和baiduocr.py中变量的路径(baiduocr.py的image变量，ocr_tasns.sh中的第4行监控目录和var变量)

6. 完成

   启动GoldenDict软件，命令行执行脚本ocr_trans.sh，之后你就可以愉快的实现截图识别翻译了。

   你也可以把ocr_trans.sh放到/bin中，从而把他当做一个命令使用。

