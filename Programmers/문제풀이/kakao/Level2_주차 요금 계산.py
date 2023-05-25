# 기본 시간(분)	기본 요금(원)	단위 시간(분)	단위 요금(원)
#   180       	5000	      10	       600

# 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 정수 배열

from collections import defaultdict as dd
from datetime import datetime
from math import ceil

def solution(fees, records):
    answer = []
    
    default_time, default_fee, unit_time, unit_fee = fees
    
    car_dict = dd(list)
    car_list = []
    for record in records:
        time, car, status = record.split(' ')
        car_dict[car].append(time)

    print(car_dict)

    for k, v in car_dict.items():
        if len(v)%2 != 0:
            v.append('23:59')
        print("---")
        print(k)
        m = 0
        for idx, t in enumerate(v):
            if idx != 0 and idx%2 == 1:
                tt = datetime.strptime(t, '%H:%M')
                vv = datetime.strptime(v[idx-1], '%H:%M')
                m += int((tt-vv).seconds/60)
        f = default_fee
        if m > default_time:
            f += ceil((m-default_time) / unit_time ) * unit_fee

        car_list.append([k, f])
    
    car_list.sort(key=lambda x: x[0])
    
    return [x[1] for x in car_list]

fees=[180, 5000, 10, 600]	
records=["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))