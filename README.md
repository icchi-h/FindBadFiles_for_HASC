# HASC Corpusの中にあるダメファイルを探すプログラム
HASC Corpusのstayフォルダにあるファイルから標準偏差を利用して, 問題があると思われるファイルを見つけ出すプログラム

## 使い方
1. pythonファイルと同ディレクトリにdataディレクトリを用意.
2. dataディレクトリにHASCコーパスのデータを入れる.
3. 以下のコマンドを実行
4. 結果がファイル出力される.

##### コマンド
```
python3 InvestigateHASCCorpus.py
```


### データのディレクトリ構成
```
.  
data  
├── 1_stay  
│  ├── person0001  
│  │   ├── HASCXXXXXX-acc.csv  
│  │   ├── HASCXXXXXX-gyro.csv  
│  │   ├── HASCXXXXXX-mag.csv  
│  │   └── ...  
│  ├── person0002  
│  └── ...  
├── 2_walk  
│　├── person0001  
│　│   ├── HASCXXXXXX-acc.csv  
│　│   ├── HASCXXXXXX-gyro.csv  
│　│   ├── HASCXXXXXX-mag.csv  
│　│   └── ...  
│　├── person0002  
│　└── ...  
└── ...
```


### 　
Developed by icchi  
2016/06/14
