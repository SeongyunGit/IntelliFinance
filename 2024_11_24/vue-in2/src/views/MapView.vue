<script setup>
import { ref, onMounted } from "vue";

let userLat = 33.450701; // 기본 위도
let userLng = 126.570667; // 기본 경도

const keywordSearch = ref('')



// Kakao Maps API 스크립트 로드 함수
const loadKaKaoPostcodeScript = () => {
  return new Promise((resolve, reject) => {
    if (document.querySelector('script[src*="dapi.kakao.com"]')) {
      return resolve();
    }

    const script = document.createElement("script");
    script.type = "text/javascript";
    script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=926349250f468b8c77a38c112f1bef98&libraries=services,clusterer&autoload=false`;

    script.onload = resolve;
    script.onerror = reject;
    document.head.appendChild(script);
  });
};


// 지도 초기화 및 검색
const initMap = () => {
  const mapContainer = document.getElementById("map");

  if (!mapContainer) {
    console.error("Map container element not found!");
    return;
  }

  kakao.maps.load(() => {
    const mapOption = {
      center: new kakao.maps.LatLng(userLat, userLng), // 기본 중심 좌표
      level: 3, // 지도 확대 레벨
    };

    const map = new kakao.maps.Map(mapContainer, mapOption);

    // Kakao Places API 객체 생성
    const places = new kakao.maps.services.Places();

    // 콜백 함수
    const callback = function (result, status) {
      if (status === kakao.maps.services.Status.OK) {
        console.log("검색 결과:", result);

        // LatLngBounds 객체 생성
        const bounds = new kakao.maps.LatLngBounds();
        const infowindow = new kakao.maps.InfoWindow({zIndex:1});
        result.forEach((place) => {
          // 마커 생성
          const marker = new kakao.maps.Marker({
            map: map,
            position: new kakao.maps.LatLng(place.y, place.x),
          });

          
          kakao.maps.event.addListener(marker, 'click', function() {
            // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
          infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
          infowindow.open(map, marker);
        });

          // Bounds에 위치 추가
          bounds.extend(new kakao.maps.LatLng(place.y, place.x));
        });

        // 생성된 Bounds를 기반으로 지도 영역 조정
        map.setBounds(bounds);
      } else {
        console.error("검색 결과가 없습니다.");
      }
    };

    // 키워드 검색 (예: "판교 치킨")
    places.keywordSearch(keywordSearch.value, callback);
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
        v-model="keywordSearch" 
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
