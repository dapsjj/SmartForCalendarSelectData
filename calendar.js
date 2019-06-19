$(function() {

    initClear(); //tableを全部クリアする
    //点击"クエリー"按钮的时候
    $("#search").click(function() {
        //先清空以前的错误消息
        $(".errfont").text(""); //移除提示中的文字
        $("input[type='text']").removeClass("errbk"); //移除文本框红色背景
        $("select").removeClass("errbk"); //移除下拉列表红色背景
        //获取表单对象中的值
        var gmailList = $("#gmailList").val(); //メールアドレス
        var startDate = $("#startDate").val(); //開始日
        var endDate = $("#endDate").val(); //終了日
        //设置错误标记
        var errorFlag = false; //false代表没有错误
        var mustInputMessage = "必須項目です"
        //错误检验
        if ($.trim(gmailList) == "" || gmailList === "undefined") { //メールアドレス
            checkErrFunction("gmailList");
            setErrorMessage("gmailListMessage", mustInputMessage);
            setRedFont("gmailListMessage");
            errorFlag = true;
        }
        if ($.trim(startDate) == "" || startDate === "undefined") { //開始日
            checkErrFunction("startDate");
            setErrorMessage("startDateMessage", mustInputMessage);
            setRedFont("startDateMessage");
            errorFlag = true;
        }
        if ($.trim(endDate) == "" || endDate === "undefined") { //終了日
            checkErrFunction("endDate");
            setErrorMessage("endDateMessage", mustInputMessage);
            setRedFont("endDateMessage");
            errorFlag = true;
        }

        if (errorFlag == true) { //如果有错误
            return;
        } else {

            //没有错误就发送ajax
            $.ajax({
                type: "POST",
                url: "http://172.17.4.74:8082/TORASINNYOU/CGI/TORASINNYOU_CALENDAR.CGI",
                data: {
                    "gmailList": gmailList,
                    "startDate": startDate,
                    "endDate": endDate
                },
                dataType: "json",
				contentType: "application/json; charset=utf-8",
				async: false,
                success: function(responseText) {					
                    if (typeof(responseText) != "undefined" && responseText != "") {
                        var makeHtml = "";
                        var data = eval(responseText.data_result);
                        for (var i = 0; i < data.length; i++) {
                            calendarInfo = data[i];
                            makeHtml += "<tr>";
                            makeHtml += "<td class=\"text-left\" width=\"120px\">" + (calendarInfo.rootSummary || '') + "</td>";
                            makeHtml += "<td class=\"text-left\" width=\"120px\">" + (calendarInfo.status || '') + "</td>";
							makeHtml += "<td class=\"text-left\" width=\"120px\">" + (calendarInfo.summary || '') + "</td>";
                            makeHtml += "<td class=\"text-left\" width=\"120px\">" + (calendarInfo.startDate || '') + "</td>";
							makeHtml += "<td class=\"text-left\" width=\"120px\">" + (calendarInfo.startTime || '') + "</td>";
                            makeHtml += "<td class=\"text-left\" width=\"120px\">" + (calendarInfo.endDate || '') + "</td>";
							makeHtml += "<td class=\"text-left\" width=\"120px\">" + (calendarInfo.endTime || '') + "</td>";
                            makeHtml += "<td class=\"text-left\" width=\"120px\">" + (calendarInfo.visibility || '') + "</td>";
                            makeHtml += "</tr>";
                        }
                        if (data.length > 0) {
                            $("#tbBody").html("");
                            $("#tbBody").append(makeHtml);
                        }
                    }
					
                },
				
				error: function (xhr, ajaxOptions, thrownError) {
					//console.info(xhr.status);
					//console.info(thrownError);
				  }
            });

        }
    });

});

//err提示
var checkErrFunction = function(idval) {
    $("#" + idval).addClass("errbk");
}

var setErrorMessage = function(idval, content) {
    $("#" + idval).text(content);
}

var setRedFont = function(idval) {
    $("#" + idval).addClass("redFont");
}

var initClear = function() {
    $("#table_search tbody tr").remove();

}
