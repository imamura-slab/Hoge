## openvino (handwritten_japanese_recognition_demo on Mac) の実行に詰まったのでメモ

### エラー内容
```
Cannot load library '/opt/intel/openvino_2020.4.287/deployment_tools/inference_engine/lib/intel64/libMKLDNNPlugin.dylib': dlopen(/opt/intel/openvino_2020.4.287/deployment_tools/inference_engine/lib/intel64/libMKLDNNPlugin.dylib, 1): Library not loaded: @rpath/libinference_engine_lp_transformations.dylib
  Referenced from: /opt/intel/openvino_2020.4.287/deployment_tools/inference_engine/lib/intel64/libMKLDNNPlugin.dylib
  Reason: image not found
```

### エラー対処 結論
以下のコマンドを実行すれば良い
```
sudo install_name_tool -change @rpath/libinference_engine_lp_transformations.dylib /opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libinference_engine_lp_transformations.dylib libMKLDNNPlugin.dylib
```



***
***
### めもめも

- handwritten_japanese_recognition_demo を実行すると以下のようなエラーが発生
```
Cannot load library '/opt/intel/openvino_2020.4.287/deployment_tools/inference_engine/lib/intel64/libMKLDNNPlugin.dylib': dlopen(/opt/intel/openvino_2020.4.287/deployment_tools/inference_engine/lib/intel64/libMKLDNNPlugin.dylib, 1): Library not loaded: @rpath/libinference_engine_lp_transformations.dylib
  Referenced from: /opt/intel/openvino_2020.4.287/deployment_tools/inference_engine/lib/intel64/libMKLDNNPlugin.dylib
  Reason: image not found
```
- `@rpath/libinference_engine/lib/intel64/libinference_engine_lp_transformations.dylib` が `/opt/intel/openvino_2020.4.287/deployment_tools/inference_engine/lib/intel64/libMKLDNNPlugin.dylib` から参照できない, ロードできないよーってことっぽい
  - `@rpath` が悪さをしている(機能していない?)らしく, リンクしている別のライブラリが読めていない.
    - リンクしている別のライブラリを確認 (otoolコマンド)
  ```
  $ otool -L libMKLDNNPlugin.dylib
  libMKLDNNPlugin.dylib:
        @rpath/libMKLDNNPlugin.dylib (compatibility version 0.0.0, current version 0.0.0)
        @rpath/libtbb.dylib (compatibility version 0.0.0, current version 0.0.0)
        @rpath/libtbbmalloc.dylib (compatibility version 0.0.0, current version 0.0.0)
        @rpath/libinference_engine_lp_transformations.dylib (compatibility version 0.0.0, current version 0.0.0)
        @rpath/libinference_engine.dylib (compatibility version 0.0.0, current version 0.0.0)
        @rpath/libinference_engine_legacy.dylib (compatibility version 0.0.0, current version 0.0.0)
        @rpath/libinference_engine_transformations.dylib (compatibility version 0.0.0, current version 0.0.0)
        @rpath/libngraph.dylib (compatibility version 0.0.0, current version 0.0.0)
        /usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 400.9.4)
        /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1252.250.1) 
  ```
  - @rpath ではなく, 場所を直接指定する(正しい対処法かは知りません)
  ```
  install_name_tool -change OLD NEW TARGET
  ```
  ```
  sudo install_name_tool -change @rpath/libinference_engine_lp_transformations.dylib /opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libinference_engine_lp_transformations.dylib libMKLDNNPlugin.dylib
  ```
  - リンクしている別のライブラリを再確認. しっかり変更できている. 
  ```
  $ otool -L libMKLDNNPlugin.dylib
  libMKLDNNPlugin.dylib:
        @rpath/libMKLDNNPlugin.dylib (compatibility version 0.0.0, current version 0.0.0)
        @rpath/libtbb.dylib (compatibility version 0.0.0, current version 0.0.0)
        @rpath/libtbbmalloc.dylib (compatibility version 0.0.0, current version 0.0.0)
        /opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libinference_engine_lp_transformations.dylib (compatibility version 0.0.0, current version 0.0.0)
        @rpath/libinference_engine.dylib (compatibility version 0.0.0, current version 0.0.0)
        @rpath/libinference_engine_legacy.dylib (compatibility version 0.0.0, current version 0.0.0)
        @rpath/libinference_engine_transformations.dylib (compatibility version 0.0.0, current version 0.0.0)
        @rpath/libngraph.dylib (compatibility version 0.0.0, current version 0.0.0)
        /usr/lib/libc++.1.dylib (compatibility version 1.0.0, current version 400.9.4)
        /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1252.250.1)
  ```
  
- この状態で実行すると, エラーが出なかった

