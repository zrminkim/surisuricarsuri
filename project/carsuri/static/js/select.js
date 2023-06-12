$(document).ready(function () {
    $("button[name='maker']").click(function () {
        let makerId = $(this).attr('id');
        $.ajax({
            type: "GET", // GET, POST
            url: "model", // 데이터를 전달할 url
            async: true, // 비동기화 동작 여부
            data: { makerId: makerId }, // 전달할 데이터
            dataType: "json", // 전달받을 데이터 타입
            beforeSend: function () { // ajax 통신 시작 전

            },
            success: function (data) {
                console.log(data)
            },
            error: function () { // 에러 발생시
                alert("젠장!")
            },
            complete: function () { // ajax 통기 끝났을 때

            }
        })
    });
});