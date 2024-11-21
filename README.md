# 2D Game Programming Term Project

##Title: Guilty and Rain
---
### 게임 소개
만드려고 하는 작품으로 모방할 게임은 **ENDER LILES: Quietus of the Knights**이며,
장르는 **메트로배니아 장르의 액션 RPG**다.

![ENDER LILIES 스크린 샷](https://github.com/user-attachments/assets/00237f02-fb62-471e-b416-3c883a1a06db)

[ENDER LILES: Quietus of the Knights 플레이 영상](https://youtu.be/4IAgZRLtg-Q?si=yXSfOJwddHiKzfuY)

메트로배니아 장르의 게임들처럼 **여러 개의 작은 맵**들이 유기적으로 **연결**되어 **하나의 큰 맵**을 만들고, 이 **맵을 탐색**하는 게임이다.
플레이어는 각 맵마다 존재하는 적들을 물리쳐야 다음 맵으로 이동할 수 있다.
(이 설명에서는 큰 맵을 **'월드'**, 작은 맵을 **'스테이지'** 로 정의함.)

![map](https://github.com/user-attachments/assets/aebdd865-060d-4776-9723-7ad9571c2042)

**게임 초반에 갈 수 없을 것 같은 장소**는 게임을 진행하면서 얻을 수 있는 **새로운 능력**을 얻고 나면 갈 수 있게 된다. 
이 새로운 능력은 탐색 뿐 아니라 **전투**에도 영향을 끼칠 수 있는 능력이다.

모든 스테이지를 탐색하는 것이 필수는 아니지만 탐색을 통해 여러 아이템을 얻을 수 있다.
클리어 조건은 여러 스테이지를 탐색을 하면서 **보스방이 나오는 스테이지를 찾고, 보스방에서 나오는 보스를 물리치면 게임을 클리어한다.**

세계관은 대략적으로 중세 판타지(ENDER LILES와 같은 느낌으로 생각하고 있으면 된다.)로 꾸려나갈 예정. 

**조작 방법**은 **키보드**와 **마우스**를 이용한다.
기본적으로 **마우스 좌클릭 - 공격(주인공은 검을 사용하는 캐릭터), wasd - 이동, space - 점프, shift - 회피** 등이 있으며, 
새로운 능력을 얻을 때마다 그에 해당하는 해당 조작 키를 알려준다.

다른 게임과 차별을 두려는 요소는 연출로 나오는 타격감이다.
이에 관련해서는 아래에서 스케치 그림과 함께 간단하게 설명.

---
### 예상 게임 실행 흐름
---
![전체적인 맵 구성(예)](https://github.com/user-attachments/assets/f0dd1005-5a1f-4c86-a9cd-db99ac1219c3)
---
월드 구성을 예로 들면 이렇게 생겼다. 그림의 위 쪽은 월드, 아래 쪽은 스테이지의 생김새이다. 

플레이어는 스테이지들을 탐색하면서 새로운 능력을 얻고, 보스방을 깨면 다음 스테이지로도 넘어갈 수 있다.
월드의 구조에 따라 스테이지에서 다른 스테이지로 이동할 때의 입구 위치가 조정되어있다.

---
![UI와 더블 점프 활용](https://github.com/user-attachments/assets/fd4ce426-aea3-4a72-bb6e-dd10e9dd1105)
---
이 그림은 UI의 구성과 메트로배니아 방식의 게임 진행 중 한가지를 보여준다. 
UI의 구성은 대략 이렇다. 왼쪽 상단에는 레벨, HP와 같은 자원을 표시하고, 왼쪽 하단에는 스킬 UI가 있다. 스킬 UI는 쿨타임을 보는 용도로 사용.
오른쪽 상단에는 월드의 구조를 보여주는 미니맵이 있는데, 키를 통해 열거나 닫을 수 있다.

메트로배니아 방식의 게임 진행 중 게임 초반에 갈 수 없을 것 같은 장소는 게임을 진행하면서 얻을 수 있는 새로운 능력을 얻고 나면 갈 수 있게 된다.
즉, 검은색 화살표를 진행하고 있는 플레이어는 더블 점프 능력이 없어 높은 위치의 스테이지를 갈 수 없지만, 빨간색 화살표 진행 방향으로 진행하면서
더블 점프 능력을 얻으면 파란색 화살표처럼 높은 위치의 스테이지로 이동할 수 있다.

---
![슈퍼 회피, 작살 클러치](https://github.com/user-attachments/assets/ff70fd33-5985-4970-9159-efe8ed3c71ad)
---
이 그림은 타격감과 관련된 연출을 보여주기 위해 자주 사용되는 새로운 능력 2가지를 보여준다. 1번은 슈퍼 회피, 2번과 3번은 작살 클러치다.

슈퍼 회피는 적이 공격할 타이밍에 회피를 하면 자동으로 발동된다.
슈퍼 회피가 발동되면, 시간이 느려지는 연출과 함께 다음 공격은 치명타로 발동된다.

작살 클러치는 휠 클릭으로 작살을 발사하고, 좌클릭 또는 우클릭을 누르면 사용할 수 있고, 휠 클릭을 다시 누르면 해제가 가능하다.
좌클릭은 플레이어가 움직이고, 우클릭은 오브젝트가 당겨진다. 우클릭의 경우에는 각 오브젝트마다 차이점이 있으므로, 아래 오브젝트 상호작용에서 다룸.

능력을 사용하는 과정에서 타격감을 살리는 연출(개발 내용 참고)을 더 추가해준다.
그 외 추가적인 연출은 아래 개발 내용 부분에서 다룰 예정.

---
### 개발할 내용(나중에 추가가 필요한 부분은 *)(1차 발표 전 활동)
---
#### 1. Scene의 종류 및 구성, 전환 규칙(*)
---
+ 타이틀 화면
---
![타이틀 화면](https://github.com/user-attachments/assets/93e14b74-a5f8-4eb6-8eee-92b9023cab39)
---
+ 스테이지(예상 게임 실행 흐름 사진 참고)
	1. 게임 클리어
		+ 보스 격파 시
		
  ![게임 클리어](https://github.com/user-attachments/assets/24af5dff-5d84-4596-a044-7628f324b89b)

	2. 게임 오버
		+ HP가 0이 될 시
		
  ![게임 오버](https://github.com/user-attachments/assets/673b546b-4a85-411f-ab79-db0208006502)

	3. 일시정지 메뉴(인벤토리, 스킬 관리, 옵션 등)
		+ 메뉴 키를 눌렀을 때
		![menu](https://github.com/user-attachments/assets/f995e179-734d-42ac-be48-7adb15941c0b)

	4. 다른 스테이지
		+ 다른 스테이지 이동 장소로 이동했을 때
---
#### 2. 각 Scene에 등장하는 GameObject의 종류 및 구성, 상호작용
---
![플레이어](https://github.com/user-attachments/assets/0689fe7a-0b54-41b2-8b01-d718904fb3ea)
##### 플레이어(Player)
+ 무기(Weapon)
	+ 검(Sword)
	+ 작살 클러치(Harpoon Clutch)

+ 스킬(Skill)(*)
	+ 더블 점프(Double Jump)
	+ 슈퍼 회피(Super Step)
	+ 올려베기(Upper Slash)

+ 체력(HP)
+ 공격력(Atk)
+ 레벨(Level)
+ 경험치 자원(Exp)
+ 골드 자원(Gold)

+ 위치(position)
	+ x 좌표
	+ y 좌표
	+ 크기(scale)
	+ 움직임(move)
 
+ 아이템(Item)(*)
	+ 포션(Potion)
---
![몬스터](https://github.com/user-attachments/assets/3b8a5cc8-1181-4333-bd53-3fb890d5bc80)
##### 몬스터(Monster)
+ 체력(HP)
+ 공격력(Atk)
+ 레벨(Level)
+ 골드 드랍(Gold)
+ 경험치 드랍(EXP)

+ 위치(position)
	+ x 좌표(x)
	+ y 좌표(y)
	+ 크기(scale)
	+ 움직임(move)

+ 종류(type)
	+ 일반 몬스터(Normal Monster)(*)
	+ 보스(BOSS)(*)
---
##### 스테이지(Stage)
+ 상호작용이 가능한 지형 지물 또는 구조물(각각 위치(position) 추가)
	+ 구조물(Structure)
		+ 벽과 바닥(wall and floor)		
		+ 가시(danger)
		+ ![가시](https://github.com/user-attachments/assets/aafb46e0-739c-4143-84f4-cded163b0c68)
		+ 나무상자(box)
	+ 스킬 획득(Skill Acquire)
		+ ![스킬 획득](https://github.com/user-attachments/assets/fc11342d-094a-4936-b274-d72ff14ad058)
	+ 다음 스테이지 이동 장소(next stage)
---
##### 각종 상호작용(Interaction)
+ 플레이어와 몬스터
	+ 공격
	+ 피격
	+ 경험치
	+ 돈
	+ 스킬
+ 플레이어와 지형 지물
	+ 벽과 바닥 충돌(몬스터)
	+ 스킬
	+ 스킬 획득 충돌
	+ 가시 충돌 의한 피격
	+ 박스(고정 x)
	+ 다음 스테이지 이동 장소 충돌
---
#### 3. 사용한/사용할 개발 기법들에 대한 간단한 소개
---
+ 패럴랙스 스크롤링(Parallax Scrolling)
	+ 시차 스크롤링(parallax scrolling, 패럴랙스 스크롤링)은 사용자가 마우스를 스크롤할 때, 원거리에 있는 배경 이미지는 느리게 움직이게 하고, 근거리에 있는 사물 이미지는 빠르게 움직이도록 함으로써 입체감을 느낄 수 있게 만든 디자인 기법이다. 
	+ 하나의 이미지를 여러 개의 레이어(layer)로 분리한 후 스크롤에 반응하는 속도를 다르게 조정하는 방식으로 구현한다.
+ 더블 버퍼링(Double Buffering)
	+ 주로 컴퓨터 그래픽에서 사용되는 용어로서 비디오 메모리만을 사용한 싱글 버퍼링으로 그래픽을 그릴 경우 데이터를 저장하는 동안에는 다음 그림의 데이터를 전송할 수 없기 때문에 지우고 그리고 지우고 그리고 할 경우 필연적으로 발생하는 깜빡임, 찢어짐 등의 상황을 막기 위해서 사용되는 기법이다.
	+ 더블 버퍼링을 통해 Animation을 효과적으로 그린다.
+ 행동 트리(Behavior Tree)
	+ 주로 게임 AI나 로봇 제어에서 사용되는 계층적 모델로, 특정 목표를 수행하기 위해 다양한 행동을 순차적 또는 병렬적으로 실행하는 구조다.
	+ 몬스터의 인공지능 구현을 위해 사용	

+ GFW
	+ 출력
	+ 키 입력
	+ 애니메이션(time)
	+ Scene(stack)
	+ 게임 월드
	+ 충돌 감지
	+ 게임 인공지능
	+ 파일 입출력
	+ 맵 에디터
---
### 개발 진행 상황
---
+ 1주차: GFW 구현 완료, 플레이어와 몬스터 객체 속성 추가와 생성, 상호작용 추가 - 90% 완료
	+ 몬스터가 플레이어를 공격하는 것은 4주차 몬스터 인공지능 때 추가할 것
	+ 애니메이션 추가해야함.
	
+ 2주차: 계획대로 스테이지 객체를 만들고 10개의 스테이지를 생성해서 플레이어와 몬스터의 위치를 정함 - 100% 완료  
	+ ![대략적인 스테이지 구성](https://github.com/user-attachments/assets/35b14f86-8d95-4e42-9e2d-0e2100a8ce36)
	+ 대략적인 스테이지를 구성해보았다.
	
	+ ![Scene 다이어그램](https://github.com/user-attachments/assets/927ab2a4-5a3f-4e95-b8e6-311071d9720f)
	+ Scene 상태 다이어그램도 그렸지만, 현재 완성시킬 수는 없었다.
	+ Stage를 Scene으로 관리하는 것이 맞는 지 확실하게 알 수 없고,
	+ save, load의 기능도 함께 생각해보아야 한다. 조금 더 고민을 해봐야 함.

	+ 10개의 스테이지 구성 후 스테이지 생성 완료

+ 3주차: 추가 Scene들은 아직 만들지 못했다. 아이템 구현도 아직 하지 않았다. 스킬 구현도 부족하다. - 50% 완료
	+ 추가적으로 배경도 Scroll 해본다.

+ 4주차:

---
### 일정
---
#### 1. 준비 사항
---
+ 대략적인 스테이지 구성
	+ 맵 에디터를 배운 후 먼저 그림판으로 그려 볼 예정 (11/6)
	+ Scene 상태 다이어그램도 같이 그릴 예정(11/6)

---
#### 2. 세부 일정
---
+ 기간: 10/29(화) ~ 11/26(화)
	+ 1주차: GFW 구현 후 플레이어와 몬스터 생성
		+ 11/2(토) - GFW 구현, 플레이어, 몬스터 그리면서 pico2D에 적응, 객체 속성 추가, 상호작용(스킬 제외).
	
	+ 2주차: 스테이지 구성
		+ 11/6(수) - 대략적인 스테이지 구성, 스테이지 객체 선언
		+ 11/9(토) - 맵 에디터로 스테이지 구성 후 스테이지 생성(플레이어, 몬스터 x)
	
	+ 3주차: 스테이지 구성 완성 후 Scene 구성 및 전환
		+ 11/13(수) - 플레이어 스킬 구현 및 몬스터와 스테이지 상호작용
		+ 11/16(토) - 스테이지에 플레이어와 몬스터 생성. 아이템 구현, Scene 구성 및 전환.

	+ 4주차 : Save, Load, 몬스터 인공지능, 이미지, 사운드 구현
		+ 11/20(수) - 저장, 불러오기 구현, 전투 연출.
		+ 11/23(토) - 몬스터의 종류, 인공지능, BOSS 구현. 리소스 구해서 이미지, 사운드 구현.
		+ 11/24(일) - 2차 발표 전 점검 및 발표 준비

+ 기간: 11/26(화) ~ 12/13(금)
	+ 11/27(수) - 아이템, 스테이지, 스킬, 몬스터 종류 추가
	+ 11/30(토) - 보완, 추가 및 유지보수
	+ 12/4(수) - 보완, 추가 및 유지보수
	+ 12/12(목) - 마지막 점검 및 발표 준비
---
### Youtube Link
---
+ 1차 발표: [1차 발표 영상](https://youtu.be/jYb6tdUZK7g?si=7oV2OZMaJpzY8354)
