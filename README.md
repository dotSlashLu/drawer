采用tkinter的简单GUI抽奖程序。

随机过程使用python内置`random.choice`，若关注公平性，可以查看`choose.py`。

## 使用

编辑`assets/employee_list.txt`即可使用，内容格式应为空白(whitespace / tab) 
分隔的两项，行尾以unix line ending结尾。

例如

```
000001 马化腾
000002 张志东
```

也可以替换`assets/`下的icon 和banner 图片进一步个性化。

可以使用空格键开始暂停抽奖过程。
