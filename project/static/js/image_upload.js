

// 이미지 업로드
function getImageFiles(e) {
    // const uploadFiles = [];
    // const files = e.target.files;
    const uploadFiles = e.target.files;
    const $imagePreview = $('.image-preview');
    if (uploadFiles.length >= 7) {
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
        if (uploadFiles.length < 7) {
            uploadFiles.push(file);
            const reader = new FileReader();
            reader.onload = (e) => {
                const preview = createJQueryElement(e, file);
                $imagePreview.append(preview);
            };
            reader.readAsDataURL(file);
        }
    });
}

function createJQueryElement(e, file) {
    const $li = $('<div>').addClass('image-li');
    const $img = $('<img>').attr('src', e.target.result);
    const $fileName = $('<span>').text(file.name);

    $li.append($img);
    $li.append($fileName);

    return $li;
}
$(document).ready(function () {
    // 동적으로 생성된 버튼에 이미지 업로드 기능 첨부
    $(document).on('click', 'button[name="detail"]', function() {

        // 이미지 업로드 화면 표시
        $('.image-display').show();

        // 동적으로 이미지 업로드 버튼 생성
        const $uploadBtn = $('<input>')
            .attr({
                type: 'file',
                class: 'bi bi-images real-upload',
                accept: 'image/*',
                multiple: true
            })
            .on('change', getImageFiles);

            // 컨테이너에 이미지 업로드 버튼 추가
            $('#detail_model').append($uploadBtn);
    });

    // 저장 버튼 클릭 이벤트 핸들러
    $('.save-button').on('click', function(){
        const uploadedImages = $('.image-preview .image-container');

        if(uploadedImages.length === 0){
            alert('업로드 된 이미지가 없습니다.');
            return;
        };
    });
});
// const $realUpload = $('.real-upload');
// const $upload = $('.upload');

// $upload.on('click', () => $realUpload.click());

// $realUpload.on('change', getImageFiles);
