// 이미지 업로드
function getImageFiles(e) {
    $('.yes-no-display').show();
    const uploadFiles = [];
    const files = e.target.files;
    const $imagePreview = $('.image-preview');
    
    if (files.length + $imagePreview.children().length > 6) {
    // if (uploadFiles.length >= 7) {
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
        // if (files.length < 7) {
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
    });

    // 저장 버튼 클릭 이벤트 핸들러
    $('.save-button').on('click', function(){
        const uploadedImages = $('.image-preview .image-container');
        if(uploadedImages.length === 0){
            alert('업로드 된 이미지가 없습니다.');
            return;
        }
        else{
            const form = $("#image-up");
            form.submit();
        };
    });
});
