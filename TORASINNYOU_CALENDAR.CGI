#!/bin/bash -xv
#
# TORASINNYOU_CALENDAR.CGI >>>カレンダー指定日と人員抽出画面の表示
# Usage : TORASINNYOU_CALENDAR.CGI
#
# Written by song.jiajun /Date : 20190613

#/////////////////////////////////////////////////////////////////////////
# 初期設定
#/////////////////////////////////////////////////////////////////////////

# 環境変数設定
export PATH=/home/SMART:/home/SMART_TRIAL:/usr/local/bin:${PATH}
export LANG=ja_JP.UTF-8


#ログディレクトリ定義
logd=/home/trial/AP/TORASINNYOU/LOG             # ログディレクトリ

# 走行ログの記録
echo   "${logd}/LOG.$(basename $0).$(date +%Y%m%d)_$(date +%H%M%S)_$$" &> /dev/null
exec 2> ${logd}/LOG.$(basename $0).$(date +%Y%m%d)_$(date +%H%M%S)_$$

# ディレクトリ定義
tmp=/tmp/$$-$(basename $0)_$(date +%Y%m%d)_$(date +%H%M%S)
shld=/home/trial/AP/TORASINNYOU/CGI

# ヘッダ出力
echo "Content-type:text/xml;charset=UTF-8"
echo ""


#１、パラメータ　
dd bs=$CONTENT_LENGTH                            |
qsstr -l_ -i_                                    >${tmp}-param

# パラメータ取得
#gmailList=$(readvalue -u "gmailList" $tmp-param)
#startDate=$(readvalue -u "startDate" $tmp-param)
#endDate=$(readvalue -u "endDate" $tmp-param)


#test
gmailList=$1
startDate=$2
endDate=$3
#

# 検索実行
if [ $# == 3 ];then
   shl=TORASINNYOU_CALENDAR.SEARCH
fi
${shld}/${shl} ${gmailList} ${startDate} ${endDate}>${tmp}-result
[ $? -eq 0 ] || ERROR_EXIT

# 結果表示
cat ${tmp}-result

#/////////////////////////////////////////////////////////////////////////
# 終了処理
#/////////////////////////////////////////////////////////////////////////
# 終了
rm -Rf ${tmp}-* &> /dev/null
exit 0
