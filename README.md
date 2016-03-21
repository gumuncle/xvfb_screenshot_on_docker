# screenshot and test on xvfb on docker

It is a sample taking screenshot using any font on docker.

```
docker build -t test_xvfb_with_alpine .
docker run -it -v `pwd`:/host test_xvfb_with_alpine
```

The font used the thing of the following sites.
Thank you for a splendid font!

+ [女子高生風？の可愛い極細フォント「JKゴシックL」のダウンロード ｜ ふぉんときゅーとがーる](http://font.cutegirl.jp/jk-font-light.html)  
+ [ふぉんときゅーとがーる](http://font.cutegirl.jp/category/about)
