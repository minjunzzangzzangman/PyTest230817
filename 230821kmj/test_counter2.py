# 순서, 작은 따옴표3개
# 그 안에 큰 따옴표 안에
# 해당 가사 또는 기사, 또는 문장을 넣기.
from collections import Counter
text = '''
2022 LCK 스프링부터 양측은 세 번 연달아 결승전에서 맞붙었다. 이번까지 포함하면 4연속이다.

2022 LCK 스프링 정규리그 전승이라는 대기록을 작성한 T1은 세트스코어 3대1로 젠지를 꺾고 우승컵을 들어올렸다. LCK 출범 10주년을 기념하는 특별한 자리에서 T1은 V10이라는 대업을 달성했다.

2022년 여름부터는 젠지의 반격이 시작됐다. 강릉에서 열린 2022 LCK 서머 결승전 젠지는 T1을 상대로 세트스코어 3대0 승리를 거두며 우승컵을 들어올렸다. 2015년 단일 팀 체제 전환 이후 첫 번째 우승이었다.

지난 3월 펼쳐진 2023 LCK 스프링 결승전에서 젠지는 사상 처음으로 '올 프로 퍼스트 팀'에 선정된 T1을 3대1로 꺾고 2연속 우승을 차지했다. 특히 프랜차이즈 스타 '룰러' 박재혁을 보내고 신인 원거리 딜러 '페이즈' 김수환을 콜업하고 이룬 성과였기에, 더욱 의미가 컸다.
'''.lower().split()
print(f"text의 결과값:{text}")
print(f"Counter 모듈이용 출력:{Counter(text)}")
