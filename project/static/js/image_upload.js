// 이미지 업로드
function getImageFiles(e) {
    const uploadFiles = [];
    const files = e.target.files;
    const $imagePreview = $('.image-preview');
    if (files.length >= 7) {
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
        if (files.length < 7) {
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
    const $li = $('<li></li>');
    const $img = $('<img />', {
        'src': e.target.result, 
        'data-file': file.name
    });
    const $fileName = $('<span></span>');
    $fileName.text(file.name);

    $li.append($img);
    $li.append($fileName);

    return $li;
}

const $realUpload = $('.real-upload');
const $upload = $('.upload');

$upload.on('click', () => $realUpload.click());

$realUpload.on('change', getImageFiles);
