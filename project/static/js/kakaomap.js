var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png";
		var container = document.getElementById('map'); //지도를 담을 영역의 DOM 레퍼런스
		var options = { //지도를 생성할 때 필요한 기본 옵션
			center : new kakao.maps.LatLng(37.4987846719974, 127.031703595662), //지도의 중심좌표.
			level : 5

		//지도의 레벨(확대, 축소 정도)

		};

		var map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴

		kakao.maps.event.addListener(map, 'tilesloaded', function() {
			// 지도 영역정보를 얻어옵니다 
			var bounds = map.getBounds();
			// 영역정보의 남서쪽 정보를 얻어옵니다 
			var swLatlng = bounds.getSouthWest();
			// 영역정보의 북동쪽 정보를 얻어옵니다 
			var neLatlng = bounds.getNorthEast();

			var message = '<p>영역좌표는 남서쪽 위도, 경도는  ' + swLatlng.toString()
					+ '이고 <br>';
			message += '북동쪽 위도, 경도는  ' + neLatlng.toString() + '입니다 </p>';

			var resultDiv = document.getElementById('result');
			resultDiv.innerHTML = message;

			getMarkerData(swLatlng, neLatlng);
		});

		kakao.maps.event.addListener(map, 'bounds_changed', function() {
			// 지도 영역정보를 얻어옵니다 
			var bounds = map.getBounds();
			// 영역정보의 남서쪽 정보를 얻어옵니다 
			var swLatlng = bounds.getSouthWest();
			// 영역정보의 북동쪽 정보를 얻어옵니다 
			var neLatlng = bounds.getNorthEast();

			var message = '<p>영역좌표는 남서쪽 위도, 경도는  ' + swLatlng.toString()
					+ '이고 <br>';
			message += '북동쪽 위도, 경도는  ' + neLatlng.toString() + '입니다 </p>';

			var resultDiv = document.getElementById('result');
			resultDiv.innerHTML = message;

			getMarkerData(swLatlng, neLatlng);

		});

		function getMarkerData(swLatlng, neLatlng) {
			// Ajax 요청을 보낼 URL
			var url = 'your_endpoint_url';

			// Ajax 요청 데이터 설정
			var requestData = {
				swLat : swLatlng.getLat(),
				swLng : swLatlng.getLng(),
				neLat : neLatlng.getLat(),
				neLng : neLatlng.getLng()
			};
			console.log(requestData);
			
			// Ajax 요청 보내기
			$.ajax({
				url : '/map',
				method : 'GET',
				data : requestData,
				dataType : 'json',
				success : function(response) {
					
					var positions = [];
					
					for (var i = 0; i < response.length; i++) {
					  var item = response[i].fields;
					  		var position = {
							title : item.name,
							latlng : new kakao.maps.LatLng(item.latitude,
									item.longitude)
						};
						positions.push(position);
					}
					var clusterer = new kakao.maps.MarkerClusterer({
						map : map, // 마커들을 클러스터로 관리하고 표시할 지도 객체 
						averageCenter : true, // 클러스터에 포함된 마커들의 평균 위치를 클러스터 마커 위치로 설정 
						minLevel : 3
					// 클러스터 할 최소 지도 레벨 
					});
					// 응답 데이터를 처리하여 마커 표시
					console.log(positions.length)

					for (var i = 0; i < positions.length; i++) {

						// 마커 이미지의 이미지 크기 입니다
						var imageSize = new kakao.maps.Size(24, 35);

						// 마커 이미지를 생성합니다    
						var markerImage = new kakao.maps.MarkerImage(imageSrc,
								imageSize);

						// 마커를 생성합니다
						
						
						var marker = new kakao.maps.Marker({
							map : map, // 마커를 표시할 지도
							position : positions[i].latlng, // 마커를 표시할 위치
							title : positions[i].title, // 마커의 타이틀, 마커에 마우스를 올리면 타이틀이 표시됩니다
							image : markerImage
						// 마커 이미지 
						});
						
					}

				},
				error : function(xhr, status, error) {
					// 에러 처리
					console.error(error);
				}
			});
		}