# 分层配置工具

在此目录使用Python3.12运行，无需安装额外依赖。

resolver.py处理配置，__init__.py导出resolve和ConfigError，__main__.py提供单文档JSON入口。example.json提供一份小型输入，运行方式为：

```sh
python -m layerconf < example.json
```

具体功能与接口要求见包根proposal.json。本目录提供起始实现，扩展后保持上述入口可用。
