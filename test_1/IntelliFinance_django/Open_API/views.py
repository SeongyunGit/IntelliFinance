from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import (
    companyList, companyListOption,
    DepositProduct, DepositProductOption,
    SavingProduct, SavingProductOption,
    annuitySavingProduct, annuitySavingProductOption,
    mortgageLoanProduct, mortgageLoanProductOption,
    rentHouseLoanProduct, rentHouseLoanProductOption,
    creditLoanProduct, creditLoanProductOption
    )
from datetime import datetime
from django.conf import settings


@api_view(['GET'])
def company(request):
    # API URL과 필요한 파라미터
    url = "http://finlife.fss.or.kr/finlifeapi/companySearch.json"
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': '1'
    }

    try:
        # 외부 API 호출
        response = requests.get(url, params=params)
        response.raise_for_status()  # 오류가 있으면 예외를 발생시킴

        # API에서 받은 JSON 데이터
        data = response.json()

        # 데이터의 구조가 맞는지 확인
        if 'result' not in data or 'baseList' not in data['result'] or 'optionList' not in data['result']:
            return Response({'error': 'API 응답에서 예상된 키를 찾을 수 없습니다.'}, status=500)

        base_list = data['result']['baseList']
        option_list = data['result']['optionList']

        # 기존 데이터 삭제 (리셋)
        companyList.objects.all().delete()
        companyListOption.objects.all().delete()

        # 데이터베이스에 저장
        for item in base_list:
            # companyList 저장
            product = companyList.objects.create(
                dcls_month=item.get('dcls_month', ''),
                fin_co_no=item.get('fin_co_no', ''),
                kor_co_nm=item.get('kor_co_nm', ''),
                dcls_chrg_man=item.get('dcls_chrg_man', ''),
                homp_url=item.get('homp_url', ''),
                cal_tel=item.get('cal_tel', '')
            )

            # companyListOption 저장 (baseList의 fin_co_no와 optionList의 fin_co_no로 매칭)
            for option in option_list:
                if option.get('fin_co_no') == item.get('fin_co_no'):
                    companyListOption.objects.create(
                        deposit_product=product,
                        dcls_month=option.get('dcls_month', ''),
                        fin_co_no=option.get('fin_co_no', ''),
                        area_cd=option.get('area_cd', ''),
                        area_nm=option.get('area_nm', ''),
                        exis_yn=option.get('exis_yn', '')
                    )

        # 성공적으로 데이터를 저장한 후, API 응답을 그대로 반환
        return Response(data)

    except requests.exceptions.RequestException as e:
        # API 요청에 실패한 경우 오류 메시지 반환
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
def Deposit(request):
    # API URL과 필요한 파라미터
    url = "http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json"
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': '1'
    }

    try:
        # 외부 API 호출
        response = requests.get(url, params=params)
        response.raise_for_status()  # 오류가 있으면 예외를 발생시킴

        # 전체 응답 데이터 출력 (디버깅용)
        # print(response.json())

        # API에서 받은 JSON 데이터
        data = response.json()

        # 데이터의 구조가 맞는지 확인
        if 'result' not in data or 'baseList' not in data['result'] or 'optionList' not in data['result']:
            return Response({'error': 'API 응답에서 예상된 키를 찾을 수 없습니다.'}, status=500)

        base_list = data['result']['baseList']
        option_list = data['result']['optionList']

        # 기존 데이터 삭제 (리셋)
        DepositProduct.objects.all().delete()
        DepositProductOption.objects.all().delete()

        # 데이터베이스에 저장
        for item in base_list:
            # DepositProduct 저장
            product = DepositProduct.objects.create(
                dcls_month=item['dcls_month'],
                fin_co_no=item['fin_co_no'],
                fin_prdt_cd=item['fin_prdt_cd'],
                kor_co_nm=item['kor_co_nm'],
                fin_prdt_nm=item['fin_prdt_nm'],
                join_way=item['join_way'],
                mtrt_int=item['mtrt_int'],
                spcl_cnd=item['spcl_cnd'],
                join_deny=item['join_deny'],
                join_member=item['join_member'],
                etc_note=item['etc_note'],
                max_limit=item['max_limit'],
                dcls_strt_day=datetime.strptime(item['dcls_strt_day'], '%Y%m%d').date(),
                dcls_end_day=datetime.strptime(item['dcls_end_day'], '%Y%m%d').date() if item['dcls_end_day'] else None,
                fin_co_subm_day=datetime.strptime(item['fin_co_subm_day'], '%Y%m%d%H%M')
            )

            # DepositProductOption 저장 (baseList의 fin_prdt_cd와 optionList의 fin_prdt_cd로 매칭)
            for option in option_list:
                if option['fin_prdt_cd'] == item['fin_prdt_cd']:
                    DepositProductOption.objects.create(
                        deposit_product=product,
                        dcls_month=option['dcls_month'],
                        fin_co_no=option['fin_co_no'],
                        fin_prdt_cd=option['fin_prdt_cd'],
                        intr_rate_type=option['intr_rate_type'],
                        intr_rate_type_nm=option['intr_rate_type_nm'],
                        save_trm=option['save_trm'],
                        intr_rate=option['intr_rate'],
                        intr_rate2=option['intr_rate2']
                    )

        # 성공적으로 데이터를 저장한 후, API 응답을 그대로 반환
        return Response(data)

    except requests.exceptions.RequestException as e:
        # API 요청에 실패한 경우 오류 메시지 반환
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
def saving(request):
    # API URL과 필요한 파라미터
    url = "http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json"  # 적금 API URL
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '020000',  # 적금 상품 그룹 번호
        'pageNo': '1'
    }

    try:
        # 외부 API 호출
        response = requests.get(url, params=params)
        response.raise_for_status()  # 오류가 있으면 예외를 발생시킴

        # 전체 응답 데이터 출력 (디버깅용)
        # print(response.json())

        # API에서 받은 JSON 데이터
        data = response.json()

        # 데이터의 구조가 맞는지 확인
        if 'result' not in data or 'baseList' not in data['result'] or 'optionList' not in data['result']:
            return Response({'error': 'API 응답에서 예상된 키를 찾을 수 없습니다.'}, status=500)

        base_list = data['result']['baseList']
        option_list = data['result']['optionList']

        # 기존 데이터 삭제 (리셋)
        SavingProduct.objects.all().delete()
        SavingProductOption.objects.all().delete()

        # 데이터베이스에 저장
        for item in base_list:
            # SavingProduct 저장
            product = SavingProduct.objects.create(
                dcls_month=item['dcls_month'],
                fin_co_no=item['fin_co_no'],
                fin_prdt_cd=item['fin_prdt_cd'],
                kor_co_nm=item['kor_co_nm'],
                fin_prdt_nm=item['fin_prdt_nm'],
                join_way=item['join_way'],
                mtrt_int=item['mtrt_int'],
                spcl_cnd=item['spcl_cnd'],
                join_deny=item['join_deny'],
                join_member=item['join_member'],
                etc_note=item['etc_note'],
                max_limit=item['max_limit'],
                dcls_strt_day=datetime.strptime(item['dcls_strt_day'], '%Y%m%d').date(),
                dcls_end_day=datetime.strptime(item['dcls_end_day'], '%Y%m%d').date() if item['dcls_end_day'] else None,
                fin_co_subm_day=datetime.strptime(item['fin_co_subm_day'], '%Y%m%d%H%M')
            )

            # SavingProductOption 저장 (baseList의 fin_prdt_cd와 optionList의 fin_prdt_cd로 매칭)
            for option in option_list:
                if option['fin_prdt_cd'] == item['fin_prdt_cd']:
                    SavingProductOption.objects.create(
                        installment_product=product,
                        dcls_month=option['dcls_month'],
                        fin_co_no=option['fin_co_no'],
                        fin_prdt_cd=option['fin_prdt_cd'],
                        intr_rate_type=option['intr_rate_type'],
                        intr_rate_type_nm=option['intr_rate_type_nm'],
                        rsrv_type=option['rsrv_type'],
                        rsrv_type_nm=option['rsrv_type_nm'],
                        save_trm=option['save_trm'],
                        intr_rate=option['intr_rate'],
                        intr_rate2=option['intr_rate2']
                    )

        # 성공적으로 데이터를 저장한 후, API 응답을 그대로 반환
        return Response(data)

    except requests.exceptions.RequestException as e:
        # API 요청에 실패한 경우 오류 메시지 반환
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
def annuitySaving(request):
    # API URL과 필요한 파라미터
    url = "http://finlife.fss.or.kr/finlifeapi/annuitySavingProductsSearch.json"
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '060000',
        'pageNo': '1'
    }

    try:
        # 외부 API 호출
        response = requests.get(url, params=params)
        response.raise_for_status()  # 오류가 있으면 예외를 발생시킴

        # API에서 받은 JSON 데이터
        data = response.json()

        # 데이터의 구조가 맞는지 확인
        if 'result' not in data or 'baseList' not in data['result'] or 'optionList' not in data['result']:
            return Response({'error': 'API 응답에서 예상된 키를 찾을 수 없습니다.'}, status=500)

        base_list = data['result']['baseList']
        option_list = data['result']['optionList']

        # 기존 데이터 삭제 (리셋)
        annuitySavingProduct.objects.all().delete()
        annuitySavingProductOption.objects.all().delete()

        # 데이터베이스에 저장
        for item in base_list:
            # annuitySavingProduct 저장
            product = annuitySavingProduct.objects.create(
                dcls_month=item['dcls_month'],
                fin_co_no=item['fin_co_no'],
                fin_prdt_cd=item['fin_prdt_cd'],
                kor_co_nm=item['kor_co_nm'],
                fin_prdt_nm=item['fin_prdt_nm'],
                join_way=item['join_way'],
                prdt_type=item['prdt_type'],
                prdt_type_nm=item['prdt_type_nm'],
                avg_prft_rate=item['avg_prft_rate'],
                btrm_prft_rate_1=item['btrm_prft_rate_1'],
                btrm_prft_rate_2=item.get('btrm_prft_rate_2', None),
                btrm_prft_rate_3=item.get('btrm_prft_rate_3', None),
                sale_co=item['sale_co'],
                sale_strt_day=datetime.strptime(item['sale_strt_day'], '%Y%m%d') if item.get('sale_strt_day') else None,
                dcls_strt_day=datetime.strptime(item['dcls_strt_day'], '%Y%m%d'),
                dcls_end_day=datetime.strptime(item['dcls_end_day'], '%Y%m%d') if item.get('dcls_end_day') else None,
                fin_co_subm_day=datetime.strptime(item['fin_co_subm_day'], '%Y%m%d%H%M')
            )

            # annuitySavingProductOption 저장 (baseList의 fin_prdt_cd와 optionList의 fin_prdt_cd로 매칭)
            for option in option_list:
                if option['fin_prdt_cd'] == item['fin_prdt_cd']:
                    annuitySavingProductOption.objects.create(
                        deposit_product=product,
                        dcls_month=option['dcls_month'],
                        fin_co_no=option['fin_co_no'],
                        fin_prdt_cd=option['fin_prdt_cd'],
                        pnsn_recp_trm=option['pnsn_recp_trm'],
                        pnsn_recp_trm_nm=option['pnsn_recp_trm_nm'],
                        pnsn_entr_age=option['pnsn_entr_age'],
                        pnsn_entr_age_nm=option['pnsn_entr_age_nm'],
                        mon_paym_atm=option['mon_paym_atm'],
                        mon_paym_atm_nm=option['mon_paym_atm_nm'],
                        paym_prd=option['paym_prd'],
                        paym_prd_nm=option['paym_prd_nm'],
                        pnsn_strt_age=option['pnsn_strt_age'],
                        pnsn_strt_age_nm=option['pnsn_strt_age_nm'],
                        pnsn_recp_amt=option['pnsn_recp_amt']
                    )

        # 성공적으로 데이터를 저장한 후, API 응답을 그대로 반환
        return Response(data)

    except requests.exceptions.RequestException as e:
        # API 요청에 실패한 경우 오류 메시지 반환
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
def mortgageLoan(request):
    # API URL과 필요한 파라미터
    url = "http://finlife.fss.or.kr/finlifeapi/mortgageLoanProductsSearch.json"
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '050000',
        'pageNo': '1'
    }

    try:
        # 외부 API 호출
        response = requests.get(url, params=params)
        response.raise_for_status()  # 오류가 있으면 예외를 발생시킴

        # API에서 받은 JSON 데이터
        data = response.json()

        # 데이터의 구조가 맞는지 확인
        if 'result' not in data or 'baseList' not in data['result'] or 'optionList' not in data['result']:
            return Response({'error': 'API 응답에서 예상된 키를 찾을 수 없습니다.'}, status=500)

        base_list = data['result']['baseList']
        option_list = data['result']['optionList']

        # 기존 데이터 삭제 (리셋)
        mortgageLoanProduct.objects.all().delete()
        mortgageLoanProductOption.objects.all().delete()

        # 데이터베이스에 저장
        for item in base_list:
            # mortgageLoanProduct 저장
            loan_product = mortgageLoanProduct.objects.create(
                dcls_month=item['dcls_month'],
                fin_co_no=item['fin_co_no'],
                fin_prdt_cd=item['fin_prdt_cd'],
                kor_co_nm=item['kor_co_nm'],
                fin_prdt_nm=item['fin_prdt_nm'],
                join_way=item['join_way'],
                loan_inci_expn=item['loan_inci_expn'],
                erly_rpay_fee=item['erly_rpay_fee'],
                dly_rate=item['dly_rate'],
                loan_lmt=item['loan_lmt'],
                dcls_strt_day=datetime.strptime(item['dcls_strt_day'], '%Y%m%d'),
                dcls_end_day=datetime.strptime(item['dcls_end_day'], '%Y%m%d') if item.get('dcls_end_day') else None,
                fin_co_subm_day=datetime.strptime(item['fin_co_subm_day'], '%Y%m%d%H%M')
            )

            # mortgageLoanProductOption 저장 (baseList의 fin_prdt_cd와 optionList의 fin_prdt_cd로 매칭)
            for option in option_list:
                if option['fin_prdt_cd'] == item['fin_prdt_cd']:
                    mortgageLoanProductOption.objects.create(
                        loan_product=loan_product,
                        mrtg_type=option['mrtg_type'],
                        mrtg_type_nm=option['mrtg_type_nm'],
                        rpay_type=option['rpay_type'],
                        rpay_type_nm=option['rpay_type_nm'],
                        lend_rate_type=option['lend_rate_type'],
                        lend_rate_type_nm=option['lend_rate_type_nm'],
                        lend_rate_min=option['lend_rate_min'],
                        lend_rate_max=option['lend_rate_max'],
                        lend_rate_avg=option['lend_rate_avg']
                    )

        # 성공적으로 데이터를 저장한 후, API 응답을 그대로 반환
        return Response(data)

    except requests.exceptions.RequestException as e:
        # API 요청에 실패한 경우 오류 메시지 반환
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
def rentHouseLoan(request):
    # API URL과 필요한 파라미터
    url = "http://finlife.fss.or.kr/finlifeapi/rentHouseLoanProductsSearch.json"
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '050000',
        'pageNo': '1'
    }

    try:
        # 외부 API 호출
        response = requests.get(url, params=params)
        response.raise_for_status()  # 오류가 있으면 예외를 발생시킴

        # API에서 받은 JSON 데이터
        data = response.json()

        # 데이터의 구조가 맞는지 확인
        if 'result' not in data or 'baseList' not in data['result'] or 'optionList' not in data['result']:
            return Response({'error': 'API 응답에서 예상된 키를 찾을 수 없습니다.'}, status=500)

        base_list = data['result']['baseList']
        option_list = data['result']['optionList']

        # 기존 데이터 삭제 (리셋)
        rentHouseLoanProduct.objects.all().delete()
        rentHouseLoanProductOption.objects.all().delete()

        # 데이터베이스에 저장
        for item in base_list:
            # rentHouseLoanProduct 저장
            loan_product = rentHouseLoanProduct.objects.create(
                dcls_month=item['dcls_month'],
                fin_co_no=item['fin_co_no'],
                fin_prdt_cd=item['fin_prdt_cd'],
                kor_co_nm=item['kor_co_nm'],
                fin_prdt_nm=item['fin_prdt_nm'],
                join_way=item['join_way'],
                loan_inci_expn=item['loan_inci_expn'],
                erly_rpay_fee=item['erly_rpay_fee'],
                dly_rate=item['dly_rate'],
                loan_lmt=item['loan_lmt'],
                dcls_strt_day=datetime.strptime(item['dcls_strt_day'], '%Y%m%d'),
                dcls_end_day=datetime.strptime(item['dcls_end_day'], '%Y%m%d') if item.get('dcls_end_day') else None,
                fin_co_subm_day=datetime.strptime(item['fin_co_subm_day'], '%Y%m%d%H%M')
            )

            # rentHouseLoanProductOption 저장 (baseList의 fin_prdt_cd와 optionList의 fin_prdt_cd로 매칭)
            for option in option_list:
                if option['fin_prdt_cd'] == item['fin_prdt_cd']:
                    rentHouseLoanProductOption.objects.create(
                        loan_product=loan_product,
                        rpay_type=option['rpay_type'],
                        rpay_type_nm=option['rpay_type_nm'],
                        lend_rate_type=option['lend_rate_type'],
                        lend_rate_type_nm=option['lend_rate_type_nm'],
                        lend_rate_min=option['lend_rate_min'],
                        lend_rate_max=option['lend_rate_max'],
                        lend_rate_avg=option['lend_rate_avg']
                    )

        # 성공적으로 데이터를 저장한 후, API 응답을 그대로 반환
        return Response(data)

    except requests.exceptions.RequestException as e:
        # API 요청에 실패한 경우 오류 메시지 반환
        return Response({'error': str(e)}, status=500)

@api_view(['GET'])
def creditLoan(request):
    # API URL과 필요한 파라미터
    url = "http://finlife.fss.or.kr/finlifeapi/creditLoanProductsSearch.json"
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '050000',  # 개인신용대출 관련 그룹번호
        'pageNo': '1'
    }

    try:
        # 외부 API 호출
        response = requests.get(url, params=params)
        response.raise_for_status()  # 오류가 있으면 예외를 발생시킴

        # API에서 받은 JSON 데이터
        data = response.json()

        # 데이터의 구조가 맞는지 확인
        if 'result' not in data or 'baseList' not in data['result'] or 'optionList' not in data['result']:
            return Response({'error': 'API 응답에서 예상된 키를 찾을 수 없습니다.'}, status=500)

        base_list = data['result']['baseList']
        option_list = data['result']['optionList']

        # 기존 데이터 삭제 (리셋)
        creditLoanProduct.objects.all().delete()
        creditLoanProductOption.objects.all().delete()

        # 데이터베이스에 저장
        for item in base_list:
            # creditLoanProduct 저장
            loan_product = creditLoanProduct.objects.create(
                dcls_month=item['dcls_month'],
                fin_co_no=item['fin_co_no'],
                fin_prdt_cd=item['fin_prdt_cd'],
                crdt_prdt_type=item['crdt_prdt_type'],
                kor_co_nm=item['kor_co_nm'],
                fin_prdt_nm=item['fin_prdt_nm'],
                join_way=item['join_way'],
                cb_name=item['cb_name'],
                crdt_prdt_type_nm=item['crdt_prdt_type_nm'],
                dcls_strt_day=datetime.strptime(item['dcls_strt_day'], '%Y%m%d'),
                dcls_end_day=datetime.strptime(item['dcls_end_day'], '%Y%m%d') if item.get('dcls_end_day') else None,
                fin_co_subm_day=datetime.strptime(item['fin_co_subm_day'], '%Y%m%d%H%M')
            )

            # creditLoanProductOption 저장 (baseList의 fin_prdt_cd와 optionList의 fin_prdt_cd로 매칭)
            for option in option_list:
                if option['fin_prdt_cd'] == item['fin_prdt_cd']:
                    creditLoanProductOption.objects.create(
                        loan_product=loan_product,
                        crdt_lend_rate_type=option['crdt_lend_rate_type'],
                        crdt_lend_rate_type_nm=option['crdt_lend_rate_type_nm'],
                        crdt_grad_1=option.get('crdt_grad_1'),
                        crdt_grad_4=option.get('crdt_grad_4'),
                        crdt_grad_5=option.get('crdt_grad_5'),
                        crdt_grad_6=option.get('crdt_grad_6'),
                        crdt_grad_10=option.get('crdt_grad_10'),
                        crdt_grad_11=option.get('crdt_grad_11'),
                        crdt_grad_12=option.get('crdt_grad_12'),
                        crdt_grad_13=option.get('crdt_grad_13'),
                        crdt_grad_avg=option['crdt_grad_avg']
                    )

        # 성공적으로 데이터를 저장한 후, API 응답을 그대로 반환
        return Response(data)

    except requests.exceptions.RequestException as e:
        # API 요청에 실패한 경우 오류 메시지 반환
        return Response({'error': str(e)}, status=500)
