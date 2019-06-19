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


HOME=/home/trial
logd=/home/trial/AP/TORASINNYOU/LOG             # ログディレクトリ



# 走行ログの記録
echo   "${logd}/LOG.$(basename $0).$(date +%Y%m%d)_$(date +%H%M%S)_$$" &> /dev/null
exec 2> ${logd}/LOG.$(basename $0).$(date +%Y%m%d)_$(date +%H%M%S)_$$

# 変数の定義
semd=${HOME}/SEMAPHORE
tmp=/tmp/$$-$(basename $0)_$(date +%Y%m%d)_$(date +%H%M%S)
shld=/home/trial/AP/TORASINNYOU/CGI

# ヘッダ出力
echo "Content-type:text/xml;charset=UTF-8"
echo ""


# エラー時の終了処理定義
ERROR_EXIT(){
  touch ${semd}/$(basename $0).${HOSTNAME}.ERROR.${sday}
  exit 1
}

#１、パラメータ　
dd bs=$CONTENT_LENGTH                            |
qsstr -l_ -i_                                    >${tmp}-param

#echo '{"test":"success"}'

#exit 0

# パラメータ取得
gmailList=$(readvalue -ugmailList $tmp-param)
startDate=$(readvalue -ustartDate $tmp-param)
endDate=$(readvalue -uendDate $tmp-param)


#test
#gmailList=$1
#startDate=$2
#endDate=$3
#

# 検索実行
#if [ $# == 3 ];then
   
#fi
shl=TORASINNYOU_CALENDAR.SEARCH
${shld}/${shl} ${gmailList} ${startDate} ${endDate}>${tmp}-result
[ $? -eq 0 ] || ERROR_EXIT

# 結果表示
# 

echo '{"data_result":' > $tmp-resultfile
cat ${tmp}-result >> $tmp-resultfile
echo '}' >> $tmp-resultfile
cat $tmp-resultfile

#/////////////////////////////////////////////////////////////////////////
# 終了処理
#/////////////////////////////////////////////////////////////////////////
# 終了
rm -Rf ${tmp}-* &> /dev/null
exit 0
