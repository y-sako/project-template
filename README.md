
# プロジェクトテンプレート

## はじめに

- データ分析用のプロジェクトテンプレート

- 任意のワークステーション上にテンプレートリポジトリをクローンして使う想定

```{bash}
# for config
export GIT_EMAIL=YOUR-EMAIL
export GIT_USER=YOUR-USERNAME

# for git
git config --local user.email ${GIT_EMAIL}
git config --local user.name ${GIT_USER}

# clone
git clone ~~~
```

```{}
# ディレクトリ構成は以下

　project
    │
    ├── .github/           <- Gitの設定用
    │
    ├── .vscode/           <- VSCodeの設定用
    │
    ├── .docker/           <- 環境構築用ファイル
    │
    ├── data/              <- データ用(任意のファイルサーバーなど)
    │
    ├── eda/               <- 探索的分析用
    │
    ├── model/             <- モデリング用(モデルオブジェクトなど)
    │
    ├── output/            <- アウトプット用
    │
    ├── src/               <- ソースコード用
    │
    ├── share/             <- 結果共有用(htmlレポートやappを配置)
    │
    ├── .dockerignore
    │
    ├── .gitignore
    │
    └── README.md          <- プロジェクトテンプレートの説明はこちら
```

## 環境構築

- 以下の要領で.envファイルを.dcokerディレクトリ直下に作成

```{bash}
cd .docker
```

```{}
# .envファイル

# プロジェクト名
COMPOSE_PROJECT_NAME=xxxx
# データパス（任意のファイルサーバーなどをマウント）
PATH_DATA=xxxx
# ポート番号を指定（空きポートを選択）
PORTS_NUM_RSTUDIO=xxxx
PORTS_NUM_SHINY=xxxx
PORTS_NUM_JUPYTERLAB=xxxx
PORTS_NUM_STREAMLIT=xxxx
```

```{bash}
docker-compose up -d
```

## 分析

- project-dir直下にproject.qmd

- 汎用コードなどはsrcディレクトリに格納して読み出すイメージ

## 結果共有

- 分析結果はshareディレクトリに配置して共有

- 静的なレポート → htmlファイル

- 動的なアウトプット → Shiny or Streamlit アプリケーション

# 参考

Pythonの分析プロジェクトテンプレ

https://github.com/cvpaperchallenge/Ascender/blob/develop/README.md


