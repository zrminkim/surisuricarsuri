$(document).ready(function () {
    // MakerID
    $("button[name='maker']").click(function () {
        let makerId = $(this).attr('id');
        $('#model').empty();
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
                // alert('성공!')

                // 제조사 클릭시 제조사에 해당하는 자동차 종류 버튼 생성
                const car_model = document.getElementById('model');
                data.forEach((item, index) => {
                    const button = document.createElement('button');
                    button.className = "btn btn-danger btn-spacing";
                    button.id = item.pk;
                    button.value = item.fields.model_name;
                    button.textContent = item.fields.model_name;
                    button.setAttribute('name', 'model');
                    car_model.appendChild(button);
                });

            },
            error: function () { // 에러 발생시
                alert("젠장!")
            },
            complete: function () { // ajax 통기 끝났을 때
                // alert('끝')
            }
        })
    });

    $(document).on('click', '#model button', function() {
        let modelId = $(this).attr('id');
        $('#detail_model').empty();
        $.ajax({
            type: "GET", // GET, POST
            url: "detail", // 데이터를 전달할 url
            async: true, // 비동기화 동작 여부
            data: { modelId: modelId }, // 전달할 데이터
            dataType: "json", // 전달받을 데이터 타입
            beforeSend: function () { // ajax 통신 시작 전
                
            },
            success: function (data) {
                console.log(data)
                // alert('성공!')

                // 자동차 모델 클릭시 자동차 상세 모델 종류 버튼 생성
                const car_detail = document.getElementById('detail_model');
                data.forEach(item => {
                    const detail = document.createElement('button');
                    
                    detail.className = "btn btn-warning btn-spacing";
                    detail.id = item.pk;
                    detail.value = item.fields.detail_name;
                    detail.textContent = item.fields.detail_name;
                    detail.setAttribute('name', 'detail');
                    car_detail.appendChild(detail);
                });

            },
            error: function () { // 에러 발생시
                alert("젠장!")
            },
            complete: function () { // ajax 통기 끝났을 때
                // alert('끝')
            }
        })
    });
});

