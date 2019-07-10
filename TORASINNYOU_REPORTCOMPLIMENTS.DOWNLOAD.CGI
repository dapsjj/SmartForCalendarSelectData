#!/bin/bash -xv
#
# TORASINNYOU_REPORTCOMPLIMENTS.DOWNLOAD.CGI >>>TOP報告「いいね」データ生成
# Usage : TORASINNYOU_REPORTCOMPLIMENTS.DOWNLOAD.CGI 'TORASINNYOU_reportcompliments_20190710162801_118556_.csv'
#
# Written by cheng.guohui /Date : 20190710

#/////////////////////////////////////////////////////////////////////////
# 初期設定
#/////////////////////////////////////////////////////////////////////////

# 環境変数設定
export PATH=/home/SMART:/home/SMART_TRIAL:/usr/local/bin:${PATH}
export LANG=ja_JP.UTF-8


HOME=/home/trial
logd=/home/trial/AP/TORASINNYOU/LOG             # ログディレクトリ



# 走行ログの記録
echo   "${logd}/LOG.$(basename $0).$(date +%Y%m%d)_$(date +%H%M%S)_$$" &> /dev/null
exec 2> ${logd}/LOG.$(basename $0).$(date +%Y%m%d)_$(date +%H%M%S)_$$

# 変数の定義
semd=${HOME}/SEMAPHORE
tmp=/tmp/$$-$(basename $0)_$(date +%Y%m%d)_$(date +%H%M%S)
shld=/home/trial/AP/TORASINNYOU/CGI
downloadPath=/home/trial/AP/TORASINNYOU/DOWNLOAD



# エラー時の終了処理定義
ERROR_EXIT(){
  touch ${semd}/$(basename $0).${HOSTNAME}.ERROR.${sday}
  exit 1
}


#/////////////////////////////////////////////////////////////
#処理開始
#////////////////////////////////////////////////////////////
#１、パラメータ　
echo ${QUERY_STRING} | qsstr -i_ -l_ > ${tmp}-param

# パラメータ取得
csvFileName=$(readvalue -uparam $tmp-param)

#ヘッダ出力
echo "Accept-Ranges: bytes"
echo "Content-type:application/octet-stream;"
echo "Content-Disposition: attachment; filename=$csvFileName";
echo "Content-Length: $(wc -c $downloadPath/$csvFileName | awk '{print $1}')"
echo ""

cat $downloadPath/$csvFileName


#////////////////////////////////////////////////////////////
#処理終了
#////////////////////////////////////////////////////////////
rm -rf ${tmp}-* 2>/dev/null
exit 0
