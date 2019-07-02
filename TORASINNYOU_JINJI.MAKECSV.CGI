#!/bin/bash -xv
#
# TORASINNYOU_JINJI.MAKECSV.CGI >>>人事データ生成
# Usage : TORASINNYOU_JINJI.MAKECSV.CGI '10128204,10109664' '0' '0' or TORASINNYOU_JINJI.MAKECSV.CGI '0' '10005' '0' or TORASINNYOU_JINJI.MAKECSV.CGI '0' '10005' '10696'  
#
# Written by song.jiajun /Date : 20190701

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
employeeCDList=$(readvalue -uemployeeCDList $tmp-param)
companyCode=$(readvalue -ucompanyCode $tmp-param)
belong1Code=$(readvalue -ubelong1Code $tmp-param)


#test
#employeeCDList=$1
#companyCode=$2
#belong1Code=$3
#


#/////////////////////////////////////////////////////////////
#処理開始
#////////////////////////////////////////////////////////////
shl=TORASINNYOU_JINJI.MAKECSV
csvfile=$(${shld}/${shl} ${employeeCDList} ${companyCode} ${belong1Code})
[ $? -eq 0 ] || ERROR_EXIT


echo '{"successFlag":"'${csvfile}'"}'
#/////////////////////////////////////////////////////////////////////////
# 終了処理
#/////////////////////////////////////////////////////////////////////////
# 終了
rm -Rf ${tmp}-* &> /dev/null
exit 0
