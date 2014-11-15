[中文](README_CN.md)

FlashlightPlugins
=================

4th-party plugins of Flashlight (https://github.com/nate-parrott/Flashlight/)

##Install##

- Install and enable Flashlight (https://github.com/nate-parrott/Flashlight/releases)
- Copy plugin bundle to `~/Library/FlashlightPlugins`

If you are familiar with command lines, you can use `ln -s bundle_name.bundle ~/Library/FlashlightPlugins` for easier update via git.

##Usage##

###Timestamp###

- `timestamp` for current timestamp
- `timestamp 1400000000` to convert timestamp into human redable time string

`ts` is short for `timestamp`, you can also use `ts 1400000000` for less typing.

###Haomatong###

- `haomatong 10086` to fetch info from haomatong for specified phone number

`hmt` is short for `haomatong`, use `hmt 10086` for less typing.

![Haomatong](images/haomatong.png)

###Kuaidi###

- `kuaidi 100033892580` to fetch express info from kuaidi100.com

![Kuaidi](images/kuaidi.png)

###YoudaoDic (by [Hyde Wang](https://github.com/callmewhy))###

- `youdao one` to translate `one` from English to Chinese.
- `youdao 汪` to translate `汪` from Chinese to English.

`yd` is short for `youdao`, you can also use `yd flower` for less typing.

Press ENTER to see translation on dic.youdao.com in browser

![](images/youdao.png)
