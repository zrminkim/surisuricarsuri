var mapContainer = document.getElementById('map'), // 지도를 표시할 div 
    mapOption = { 
        center: new kakao.maps.LatLng(37.498847, 127.031724), // 지도의 중심좌표
        level: 3, // 지도의 확대 레벨
        mapTypeId : kakao.maps.MapTypeId.ROADMAP // 지도종류
    };

var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다

// 마커들을 담을 배열을 만든다.
var markers = [];

// 지도 드래그 이벤트    
kakao.maps.event.addListener(map, 'dragend', setMarker());

// 지도가 처음 생기는 경우 마커를 나타내기 위해 함수를 직접 실행
window.onload = setMarker();

// 마커를 나타내는 함수
function setMarker(){
    //addListener에 넣기 위해서는 return function 타입의 매개변수가 필요
    return function(){
     //그려진 마커를 맵에서 지우는 함수
        removeMarker();

        //맵의 중심점의 위도와 경도를 받아오는 변수
        var lat = map.getCenter().getLat();
        var lng = map.getCenter().getLng();

        //마스크 데이터를 받아오는 URL
        var url = "C:/Users/ii818/git/surinam3/DB/전국자동차정비업체표준데이터.json";

        // 이미지 관련 변수
        // 마커 이미지의 URL
        var imageSrc = "http://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png"; 
        // 마커 이미지의 이미지 크기 입니다
        var imageSize = new kakao.maps.Size(24, 35); 
        // 마커 이미지를 생성합니다    
        var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize); 

        $.ajax({
            url : url,
            dataType : "json", //데이터 타입은 json형태로 받아옵니다.
            success: function(result){
                for(var i=0; i< result.count; i++){// json 데이터를 분석하며 각 데이터 분석마다 Marker를 찍어줍니다.
                    console.log('result.stores['+i+'].addr : ' + result.stores[i].addr);
                    console.log('result.stores['+i+'].code : ' + result.stores[i].code);
                    console.log('result.stores['+i+'].created_at : ' + result.stores[i].created_at);
                    console.log('result.stores['+i+'].lat : ' + result.stores[i].lat);
                    console.log('result.stores['+i+'].lng : ' + result.stores[i].lng);
                    console.log('result.stores['+i+'].name : ' + result.stores[i].name);
                    console.log('result.stores['+i+'].remain_stat : ' + result.stores[i].remain_stat);
                    console.log('result.stores['+i+'].stock_at : ' + result.stores[i].stock_at);
                    console.log('result.stores['+i+'].type : ' + result.stores[i].type);

                    var marker = new kakao.maps.Marker({//맵에 표현 될 마커들을 표시
                        map : map,
                        position : new kakao.maps.LatLng(result.stores[i].lat, result.stores[i].lng),
                        title : result.stores[i].name,
                        image : markerImage 
                    });
                //마커를 배열에 추가한다.
                markers.push(marker);
                }
            }
        });
    };
};

//그려진 마커를 맵에서 없애는 함수
function removeMarker(){
    for (var i = 0; i < markers.length; i++) {
            markers[i].setMap(null);
        }       
        markers = [];
}




// 일반 지도와 스카이뷰로 지도 타입을 전환할 수 있는 지도타입 컨트롤을 생성합니다
var mapTypeControl = new kakao.maps.MapTypeControl();

// 지도에 컨트롤을 추가해야 지도위에 표시됩니다
// kakao.maps.ControlPosition은 컨트롤이 표시될 위치를 정의하는데 TOPRIGHT는 오른쪽 위를 의미합니다
map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);

// 지도 확대 축소를 제어할 수 있는  줌 컨트롤을 생성합니다
var zoomControl = new kakao.maps.ZoomControl();
map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);


// 마커가 표시될 위치입니다 
var markerPosition  = new kakao.maps.LatLng(37.498847, 127.031724); 

// 마커를 생성합니다
var marker = new kakao.maps.Marker({
    position: markerPosition
});

// 마커가 지도 위에 표시되도록 설정합니다
marker.setMap(map);

// 아래 코드는 지도 위의 마커를 제거하는 코드입니다
// marker.setMap(null);    
