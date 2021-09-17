from datetime import datetime
name = '강준호'
age = '7'

hello = f'제 이름은 {name}입니다. 나이는 {age}입니다.' # 제 이름은 홍길동입니다. 나이는 30입니다.


today = datetime.now()
mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
filename = f'file - {mytime}' # file - 2021-09-17-23-20-07
