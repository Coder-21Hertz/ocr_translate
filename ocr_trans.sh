#!/bin/bash

#本地goldendict的OCR取词
cd /home/***/Software/OCR/Pictures # 监控和图片存储目录
while true;do
   num=$(find -name "*.png" -print)
   if [ ! -n "$num" ]; then
      sleep 1
   else
      mv *.png 1.png # 重命名

      # 识别图片中的文字
      var=$(python3 /home/***/Software/OCR/baiduocr/python_ocr/baiduocr.py)
      # 调用goldendict软件翻译文字
      goldendict "$var"
      # 在终端输出图片中的文字
      echo -e "$\nvar"
      rm *.png
      #rm *.txt
      sleep 1
   fi
done