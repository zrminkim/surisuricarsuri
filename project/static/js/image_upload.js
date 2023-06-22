// 이미지 업로드
function getImageFiles(e) {
    $('.yes-no-display').show();
    const uploadFiles = [];
    const files = e.target.files;
    const $imagePreview = $('.image-preview');
    $imagePreview.empty();

    if (files.length + $imagePreview.children().length > 6) {
        alert('이미지는 최대 6개 까지 업로드가 가능합니다.');
        
        return;
    }
    
    // 파일 타입 검사
    Array.from(files).forEach(file => {
        if (!file.type.match("image/.*")) {
            alert('이미지 파일만 업로드가 가능합니다.');
            return;
        }
    
        // 파일 갯수 검사
        if ($imagePreview.children().length >= 6) {
            alert('최대 6개의 이미지만 업로드가 가능합니다.');
            return;
        }
        uploadFiles.push(file);
        const reader = new FileReader();
        reader.onload = (e) => {
            const preview = createJQueryElement(e, file);
            $imagePreview.append(preview);
        };
        reader.readAsDataURL(file);
    });
    $('html, body').animate({ scrollTop: $(document).height() }, 300);
}

function createJQueryElement(e, file) {
    const $container = $('<div>').addClass('image-container');
    const $img = $('<img>', {
        'src': e.target.result,
        'data-file':file.name
    });
    const $fileName = $('<span>').text(file.name).addClass('file-name');

    $container.append($img);
    $container.append($fileName);

    return $container;
}
$(document).ready(function () {
    // 동적으로 생성된 버튼에 이미지 업로드 기능 첨부
    $(document).on('click', 'button[name="detail"]', function() {

        // 이미지 업로드 화면 표시
        $('.image-display').show();
        let detailId = $(this).attr('id');
        $('#detail_est').val(detailId.replace('detail', ''));
        $('#image_up_hide').show();

        // 버튼 클릭시 화면이 하단으로 이동
        var $button = $(this);
        var $parentContainer = $button.parent();
        var $lastButton = $parentContainer.children().last();

        // 버튼 위치로 스크롤?
        $('html, body').animate({
            scrollTop: $lastButton.offset().top
        }, 300);
    });

    // 저장 버튼 클릭 이벤트 핸들러
    $('#btn_yes').on('click', function(){
        alert('견적서를 계산중입니다.')
        const uploadedImages = $('.image-container');
        console.log($('.image-container').length)
        if(uploadedImages.length === 0){
            alert('업로드 된 이미지가 없습니다.');
            return;
        }
        else if(uploadedImages.length >= 7){
            alert('이미지가 너무 많습니다. 6개 이하만 올려주세요');
            return;
        }
        else{
            const form = $("#image-up");
            form.submit();
        };
    });
    $('#btn_no').on('click', function(){
        alert('다시 이용해주시기 바랍니다.');
        location.replace('/')
        
    });
});
