# titanic_practic✅ 全体の処理シーケンス（概要）

データ取得 → 前処理 → 学習 → 評価 → 推論 → 提出ファイル作成


⸻

🔁 各ステップの詳細と関連ファイル

ステップ    説明    関連ファイル
① データ取得    Kaggle APIなどでデータを取得し、data/raw/ に保存    手動 or ダウンロードスクリプト
② 前処理    データを読み込み、欠損値処理や特徴量エンジニアリングをして data/processed/ に保存    src/preprocess.py
③ モデル学習    訓練用データを使ってモデル学習。モデルを models/ に保存し、ログや設定を experiments/ に保存    src/train.py, configs/train_config.yaml
④ モデル評価    バリデーションデータで評価。評価結果を result.log や experiments/ に記録    src/evaluate.py, src/utils/metrics.py
⑤ 推論（予測）    テストデータに対して学習済みモデルで推論。結果を submissions/ にCSV出力    src/predict.py
⑥ 提出ファイル管理    作成した提出用CSVを Kaggle に提出するための準備    submissions/, scripts/run_infer.sh 等


⸻

🔁 シーケンス図（簡略フロー）

【START】
   │
   ├─▶ ① データ取得（data/raw/）
   │
   ├─▶ ② 前処理（src/preprocess.py）
   │       └── 保存先: data/processed/
   │
   ├─▶ ③ 学習（src/train.py）
   │       ├── 入力: data/processed/
   │       ├── config: configs/trainconfig.yaml
   │       ├── 保存先: models/, experiments/
   │
   ├─▶ ④ 評価（src/evaluate.py）
   │       └── ログ出力: experiments/exp***/result.log
   │
   ├─▶ ⑤ 推論（src/predict.py）
   │       └── 保存先: submissions/sub_001.csv
   │
   └─▶ ⑥ 提出 or 分析（notebooks/EDA.ipynbなど）
【END】


⸻

🖥️ 実行例（Dockerコンテナ内で）

① 前処理
python src/preprocess.py --config configs/train_config.yaml

② 学習
python src/train.py --config configs/train_config.yaml

③ 評価（必要なら）
python src/evaluate.py --model models/model.pkl

④ 推論
python src/predict.py --model models/model.pkl --output submissions/sub_001.csv

※ 各ステップをシェルスクリプト化しておけばより便利（例：scripts/run_train.sh など）

⸻

💡補足：実験管理のために
    •    experiments/exp_001/ の中に：
    •    使用した config.yaml
    •    学習ログ result.log
    •    学習済みモデル model.pkl
を保存して、再現性・比較を保つようにするのが理想です。