<script setup>
import { ref, onMounted } from "vue";
 
let latitude = 33.450701; // 기본 위도
let longitude = 126.570667; // 기본 경도

const KAKAOMAP_API_KEY=import.meta.env.VITE_KAKAOMAP_API_KEY
const keyword = ref('')

const bank_count = ref(0)


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

        bank_count.value = result.length

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
  <div class="min-h-screen bg-gradient-to-b from-blue-50 to-indigo-50 p-4 md:p-8">
    <div class="max-w-7xl mx-auto">
      <!-- 헤더 섹션 -->
      <div class="text-center mb-8">
        <h1 class="text-3xl md:text-4xl font-bold text-gray-800 mb-3">
          <span class="text-indigo-600">내 주변</span> 은행 찾기
        </h1>
        <p class="text-gray-600 md:text-lg">가장 가까운 은행을 쉽고 빠르게 찾아보세요</p>
      </div>

      <!-- 메인 컨테이너 -->
      <div class="bg-white rounded-2xl shadow-xl overflow-hidden">
        <!-- 검색 섹션 -->
        <div class="p-6 md:p-8 bg-gradient-to-r from-indigo-500 to-purple-600">
          <div class="flex flex-col md:flex-row items-center space-y-4 md:space-y-0 md:space-x-4">
            <div class="relative w-full md:w-2/3">
              <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
              </div>
              <input 
                type="text" 
                v-model="keyword" 
                placeholder="은행명 또는 지역을 입력하세요" 
                class="w-full pl-12 pr-4 py-3 rounded-xl border-2 border-transparent bg-white/90 backdrop-blur-sm focus:border-indigo-300 focus:ring-2 focus:ring-indigo-300 transition duration-200 text-gray-800 placeholder-gray-400"
              />
            </div>
            <button 
              @click="initMap" 
              class="w-full md:w-auto px-8 py-3 rounded-xl bg-white text-indigo-600 font-semibold hover:bg-indigo-50 transition duration-300 ease-in-out focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-indigo-600 shadow-lg hover:shadow-xl"
            >
              검색하기
            </button>
          </div>

          <!-- 빠른 필터 -->
          <div class="flex flex-wrap gap-2 mt-4">
            <button
              v-for="bank in ['전체', 'KB국민', '신한', '우리', 'NH농협']" 
              :key="bank"
              class="px-4 py-1.5 rounded-full bg-white/20 text-white text-sm hover:bg-white/30 transition duration-200"
            >
              {{ bank }}  
            </button>
          </div>
        </div>

        <!-- 지도 컨테이너 -->
        <div class="relative">
          <div id="map" class="w-full h-[500px] md:h-[600px]"></div>
          
          <!-- 현재 위치 버튼 -->
          <button 
            class="absolute bottom-6 right-6 p-3 rounded-full bg-white shadow-lg hover:shadow-xl transition duration-300 text-gray-700 hover:text-indigo-600"
            @click="getCurrentLocation"
          >
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
          </button>
        </div>
      </div>

      <!-- 검색 결과 요약 -->
      <div class="mt-6 px-4 py-3 bg-white rounded-xl shadow-lg">
        <p class="text-gray-600">
          현재 위치에서 <span class="text-indigo-600 font-semibold">3km</span> 반경 내
          <span class="text-indigo-600 font-semibold">23개</span>의 은행이 검색되었습니다.
        </p>
      </div>
    </div>
  </div>
</template>



<style scoped>
html {
  scroll-behavior: smooth;
}

/* 지도 컨테이너에 부드러운 그림자 효과 */
#map {
  box-shadow: inset 0 2px 4px 0 rgb(0 0 0 / 0.05);
}

/* 호버 효과를 위한 트랜지션 */
.transition {
  transition-property: all;
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-duration: 300ms;
}
</style>
