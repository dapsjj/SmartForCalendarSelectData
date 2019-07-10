#!/bin/bash -xv
#
# TORASINNYOU_REPORTCOMPLIMENTS.MAKECSV.CGI >>>TOP報告「いいね」データ生成
# Usage : TORASINNYOU_REPORTCOMPLIMENTS.MAKECSV.CGI '201909' '201910' '2200107,10040783,10144899' '10108708,10123238,10120236' or TORASINNYOU_REPORTCOMPLIMENTS.MAKECSV.CGI '201909' '201910' '2200107,10040783,10144899' '0' or TORASINNYOU_REPORTCOMPLIMENTS.MAKECSV.CGI '201909' '201910' '0' '10108708,10123238,10120236' or TORASINNYOU_REPORTCOMPLIMENTS.MAKECSV.CGI '201909' '201910' '0' '0'  
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



# パラメータ取得
startDate=$(readvalue -ustartDate $tmp-param)
endDate=$(readvalue -uendDate $tmp-param)
authorEmployeeCDList=$(readvalue -uauthorEmployeeCDList $tmp-param)
praiseEmployeeCDList=$(readvalue -upraiseEmployeeCDList $tmp-param)


#/////////////////////////////////////////////////////////////
#処理開始
#////////////////////////////////////////////////////////////
shl=TORASINNYOU_REPORTCOMPLIMENTS.MAKECSV
csvfile=$(${shld}/${shl} ${startDate} ${endDate} ${authorEmployeeCDList} ${praiseEmployeeCDList})
[ $? -eq 0 ] || ERROR_EXIT


echo '{"successFlag":"'${csvfile}'"}'
#/////////////////////////////////////////////////////////////////////////
# 終了処理
#/////////////////////////////////////////////////////////////////////////
# 終了
rm -rf ${tmp}-* 2>/dev/null
exit 0
