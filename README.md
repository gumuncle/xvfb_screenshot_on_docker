# screenshot and test on xvfb on docker

```
docker build -t test_xvfb_with_alpine .
docker run -it -v `pwd`:/host test_xvfb_with_alpine
```


フォントは以下のサイトのものを使用させていただきました。  
すばらしいフォントをありがとう御座います！  

+ [女子高生風？の可愛い極細フォント「JKゴシックL」のダウンロード ｜ ふぉんときゅーとがーる](http://font.cutegirl.jp/jk-font-light.html)  
+ [ふぉんときゅーとがーる](http://font.cutegirl.jp/category/about)
