<script setup>
import { ref, onMounted } from "vue";
 
let latitude = 33.450701; // 기본 위도
let longitude = 126.570667; // 기본 경도
const KAKAOMAP_API_KEY='926349250f468b8c77a38c112f1bef98'
const keyword = ref('')




// Kakao Maps API 스크립트 로드 함수
const loadKaKaoPostcodeScript = () => {
  return new Promise((resolve, reject) => {
    if (document.querySelector('script[src*="dapi.kakao.com"]')) {
      return resolve();
    }
    
    const script = document.createElement("script");
    script.type = "text/javascript";
    script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${KAKAOMAP_API_KEY}&libraries=services,clusterer&autoload=false`;

    script.onload = resolve;
    script.onerror = reject;
    document.head.appendChild(script);
    navigator.geolocation.getCurrentPosition(pos => {
      latitude = pos.coords.latitude;
      longitude = pos.coords.longitude;
  })
  });
};


// 지도 초기화 및 검색
const initMap = async () => {
  const mapContainer = document.getElementById("map");

  if (!mapContainer) {
    console.error("Map container element not found!");
    return;
  }

  kakao.maps.load(async () => {
    try {
      // 현재 위치 가져오기
      const currentCoordinate = await getCurrentCoordinate();
      console.log("현재 위치:", currentCoordinate);

      // 지도 옵션 설정
      const mapOption = {
        center: currentCoordinate, // 현재 위치를 중심 좌표로 설정
        level: 3, // 지도 확대 레벨
      };

      // 지도 생성
      const map = new kakao.maps.Map(mapContainer, mapOption);
      var imageSrc = "https://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markerStar.png"; 
      var imageSize = new kakao.maps.Size(24, 35); 
      var markerImage = new kakao.maps.MarkerImage(imageSrc, imageSize); 
      console.log(currentCoordinate)
      // 현재 위치에 마커 표시
      const currentMarker = new kakao.maps.Marker({
        map: map,
        position: currentCoordinate,
        title: "현재위치",
        image : markerImage
      });
      const infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });

      // 인포윈도우 내용 설정
      const latitude = currentCoordinate.getLat().toFixed(6); // 위도
      const longitude = currentCoordinate.getLng().toFixed(6); // 경도
      const contentDiv = document.createElement('div');
      contentDiv.innerHTML = 
        `<div style="
                  padding: 15px 18px; 
                  font-size: 13px; 
                  line-height: 1.6; 
                  color: #333; 
                  background-color: #fff; 
                  border-radius: 10px; 
                  box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.1); 
                  max-width: 300px; 
                  word-wrap: break-word;
                  word-break: break-word;
                  ">
            <strong style="font-size: 16px; color: #2c3e50; font-weight: 600; letter-spacing: 0.5px;">현재 위치</strong><br>
            <span style="color: #7f8c8d; font-size: 13px; margin-top: 8px; font-style: italic; display: block;"></span>
            <button id="closeBtn" style="
                            background-color: #3498db; 
                            color: #fff; 
                            border: none; 
                            padding: 8px 15px; 
                            border-radius: 5px; 
                            font-size: 14px;
                            cursor: pointer;
                            margin-top: 10px;
                            width: 100%;">닫기</button>
        </div>`;
        infowindow.setContent(contentDiv);
        const closeButton = contentDiv.querySelector('#closeBtn');
                closeButton.addEventListener('click', () => {
                    infowindow.close();
                });

// 마커 클릭 시 인포윈도우 열기
kakao.maps.event.addListener(currentMarker, "click", function () {
  infowindow.open(map, currentMarker);
});



      // Kakao Places API 객체 생성
      const places = new kakao.maps.services.Places();

      const callback = function (result, status) {
    if (status === kakao.maps.services.Status.OK) {
        console.log("검색 결과:", result);

        const bounds = new kakao.maps.LatLngBounds();
        const infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });

        result.forEach((place) => {
            const marker = new kakao.maps.Marker({
                map: map,
                position: new kakao.maps.LatLng(place.y, place.x),
            });

            kakao.maps.event.addListener(marker, "click", function () {
                infowindow.close();

                // div 요소 생성
                const contentDiv = document.createElement('div');
                contentDiv.innerHTML = `
                    <div style="
                        padding: 15px 18px; 
                        font-size: 13px; 
                        line-height: 1.6; 
                        color: #333; 
                        background-color: #fff; 
                        border-radius: 10px; 
                        box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.1); 
                        max-width: 300px; 
                        word-wrap: break-word;
                        word-break: break-word;">
                        <strong style="font-size: 16px; color: #2c3e50; font-weight: 600; letter-spacing: 0.5px;">
                            ${place.place_name}
                        </strong><br>
                        <span style="color: #7f8c8d; font-size: 13px; margin-top: 8px; font-style: italic; display: block;">
                            📍 ${place.address_name}
                        </span><br>
                        <span style="color: #95a5a6; font-size: 12px; font-weight: 500; margin-top: 6px; display: block;">
                            🚗 거리: ${place.distance}m
                        </span><br>
                        <button id="closeBtn" style="
                            background-color: #3498db; 
                            color: #fff; 
                            border: none; 
                            padding: 8px 15px; 
                            border-radius: 5px; 
                            font-size: 14px;
                            cursor: pointer;
                            margin-top: 10px;
                            width: 100%;">닫기</button>
                    </div>`;

                // InfoWindow 내용 설정
                infowindow.setContent(contentDiv);
                
                // InfoWindow 열기
                infowindow.open(map, marker);

                // 닫기 버튼에 이벤트 리스너 추가
                const closeButton = contentDiv.querySelector('#closeBtn');
                closeButton.addEventListener('click', () => {
                    infowindow.close();
                });
            });
            
            bounds.extend(new kakao.maps.LatLng(place.y, place.x));
        });

        map.setBounds(bounds);
    } else {
        console.error("검색 결과가 없습니다.");
    }
};
      
      // 키워드 검색 실행
      const options = {
        location: currentCoordinate, // 현재 위치를 기반으로 검색
        radius: 10000, // 반경 10km
        sort: kakao.maps.services.SortBy.DISTANCE, // 거리순 정렬
      };

      console.log("검색 옵션:", options);
      places.keywordSearch(keyword.value, callback, options);
    } catch (error) {
      console.error("지도 초기화 중 오류 발생:", error.message);
    }
  });
};

const getCurrentCoordinate = () => {
  console.log("getCurrentCoordinate 함수 실행!");

  return new Promise((resolve, reject) => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const lat = position.coords.latitude; // 위도
          const lon = position.coords.longitude; // 경도
          const coordinate = new kakao.maps.LatLng(lat, lon);
          console.log("현재 좌표:", coordinate);
          resolve(coordinate);
        },
        (error) => {
          reject(new Error("위치 정보를 가져오는 데 실패했습니다."));
        }
      );
    } else {
      reject(new Error("GeoLocation을 지원하지 않습니다."));
    }
  });
};


// 컴포넌트 마운트 시 Kakao Maps 스크립트 로드
onMounted(async () => {
  try {
    await loadKaKaoPostcodeScript();
    initMap();
  } catch (error) {
    console.error("Error loading Kakao Maps:", error);
  }
});
</script>

<template>
  <div class="map-container">
    <!-- 검색 입력 -->
    <div style="margin-bottom: 10px;">
      <input 
        type="text" 
        v-model="keyword" 
        placeholder="은행명을 작성하세요" 
        style="width: 60%; padding: 10px; margin-right: 10px;"
      />
      <button @click="initMap" style="padding: 10px 20px; background-color: #007bff; color: white; border: none; cursor: pointer;">
        검색
      </button>
    </div>
    <!-- 지도 영역 -->
    <div id="map" style="width: 100%; height: 350px;"></div>
  </div>
</template>

<style scoped>
.map-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}
</style>
