$(document).ready(function () {
    // 화면 새로고침시 상위로 스크롤이 올라감
    $(window).scrollTop(0);
    // MakerID
    $("button[name='maker']").click(function () {
        let makerId = $(this).attr('id');
        $('#model').empty();
        $('#detail_model').empty();
        // $("#image-up").empty();
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
                car_model.innerHTML = '';
                // 기존 버튼 지우기
                data.forEach(item => {
                    const button = document.createElement('button');
                    button.className = "btn-hover color-5 btn-spacing fade-in-box";
                    button.id = item.pk;
                    button.value = item.fields.model_name;
                    button.textContent = item.fields.model_name;
                    button.setAttribute('name', 'model');
                    car_model.appendChild(button);
                });
                // 새 버튼에 페이드 인 효과 적용
                $('.fade-in-box').fadeIn();
            },
            error: function (error) { // 에러 발생시
                alert(error)
            },
            complete: function () { // ajax 통기 끝났을 때
                // alert('끝')
            }
        })
    });

    // Model ID
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
                car_detail.innerHTML = ''; // 이전 버튼 지우기

                data.forEach(item => {
                    const detail = document.createElement('button');
                    
                    detail.className = "btn-hover color-6 btn-spacing fade-in-model";
                    detail.id = item.pk;
                    detail.value = item.fields.detail_name;
                    detail.textContent = item.fields.detail_name;
                    detail.setAttribute('name', 'detail');
                    car_detail.appendChild(detail);
                });
                // 새 버튼에 페이드 인 효과 적용
                $('.fade-in-model').fadeIn();
            },
            error: function (error) { // 에러 발생시
                alert(error)
            },
            complete: function () { // ajax 통기 끝났을 때
                // alert('끝')
            }
        })
    });
    $("div[name=estimate]").click(function(){
        $('#maker_hide').show();
        $("#scroll-move")[0].scrollIntoView({ behaviro: "smooth"});
    });
    $("#maker_hide").click(function(){
        $('#model_hide').show();
    });
    $("#model_hide").click(function(){
        $('#detail_hide').show();
    });
    $("#detail_hide").click(function(){
        $('#image_up_hide').show();
    });
});

