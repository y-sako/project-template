# ベースイメージ
FROM rocker/verse:4.3.0

# OS環境設定
## ロケール
ENV LANG ja_JP.UTF-8
ENV LC_ALL ja_JP.UTF-8
RUN sed -i '$d' /etc/locale.gen \
      && echo "ja_JP.UTF-8 UTF-8" >> /etc/locale.gen \
      && locale-gen ja_JP.UTF-8 \
      && /usr/sbin/update-locale LANG=ja_JP.UTF-8 LANGUAGE="ja_JP:ja"
RUN /bin/bash -c "source /etc/default/locale"
RUN ln -sf  /usr/share/zoneinfo/Asia/Tokyo /etc/localtime
## フォント
RUN apt-get update && apt-get install -y \
      fonts-ipaexfont \
      fonts-noto-cjk \
      fonts-firacode

# パッケージのインストール
## 汎用
RUN install2.r --error --deps TRUE --ncpus -1 \
      languageserver \
      pacman \
      rmdformats \
      systemfonts \
      janitor \
      data.table \
      progress \
      RVerbalExpressions \
      png \
      reticulate \
      markdown \
      svglite \
      DT \
      gt \
      gtExtras \
      plotly \
      zipangu
      
## モデリング用
RUN install2.r --error --ncpus -1\
      performance \
      parameters \
      see \
      rstan \
      tidybayes \
      brms \
      Robyn

# Quartoのインストール
RUN sudo rm -rf /opt/quarto
ENV QUARTO_VERSION 1.3.361
RUN /rocker_scripts/install_quarto.sh
RUN quarto install extension quarto-ext/fontawesome  --no-prompt

# Shinyのインストール
# ENV SHINY_SERVER_VERSION 1.5.20.1002
RUN /rocker_scripts/install_shiny_server.sh
RUN install2.r --error --ncpus -1\
      flexdashboard \
      bs4Dash \
      bslib \
      thematic \
      shinyWidgets 

# Pythonのインストール
RUN apt-get update && apt-get install -y python3 python3-pip

# ライブラリのインストール
## 汎用
RUN pip install -U pip \
      && pip install --no-cache-dir jupyter \
      && pip install --no-cache-dir jupyterlab \
      && pip install --no-cache-dir pandas \
      && pip install --no-cache-dir numpy \
      && pip install --no-cache-dir streamlit \
      && pip install --no-cache-dir shiny \
      && pip install --no-cache-dir lightweight_mmm